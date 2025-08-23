import json, jwt, datetime
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.contrib.auth.hashers import make_password, check_password


def generate_token(username):
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1) 
    }
    token = jwt.encode(payload, "mysecretkey", algorithm="HS256")
    return token 


def all_user(request):
    return HttpResponse("Hello from all the users")


@csrf_exempt
def registration(request):
    if request.method == "POST":
        try:

            data = json.loads(request.body.decode("utf-8"))
            username = data.get("username")
            email = data.get("email")
            password = data.get("password")

            if not username or not email or not password:
                return JsonResponse(
                    {"message": "All fields are required", "success": False},
                    status=400,
                )

            if User.objects.filter(username=username).exists():
                return JsonResponse(
                    {"message": "User already exists", "success": False},
                    status=400,
                )

            # Save user with hashed password
            user = User(username=username, email=email, password=make_password(password))
            user.save()

            return JsonResponse(
                {"message": "User created successfully", "success": True},
                status=201,
            )

        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse(
                {"message": "Internal Server Error", "error": str(e), "success": False},
                status=500,
            )

    elif request.method == "GET":  
        return HttpResponse("Registration endpoint is ready. Use POST to register.")

    else:
        return JsonResponse(
            {"message": "Request Method not allowed", "success": False},
            status=405,
        )


@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return JsonResponse(
                    {"message": "All fields are required", "success": False},
                    status=400,
                )

            # Find user
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return JsonResponse(
                    {"message": "Invalid User or Password", "success": False},
                    status=400,
                )

            # Verify password
            if check_password(password, user.password):
                token = generate_token(username)
                return JsonResponse({"token": token, "success": True})
            else:
                return JsonResponse(
                    {"message": "Invalid User or Password", "success": False},
                    status=400,
                )

        except Exception as e:
            import traceback
            traceback.print_exc()
            return JsonResponse(
                {"message": "Internal Server Error", "error": str(e), "success": False},
                status=500,
            )

    elif request.method == "GET":  # ✅ same for browser testing
        return HttpResponse("Login endpoint is ready. Use POST to login.")

    else:
        return JsonResponse(
            {"message": "Request Method not allowed", "success": False},
            status=405,
        )



def dashboard(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JsonResponse({"message": "Unauthorized, token missing", "success": False}, status=401)

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, "mysecretkey", algorithms=["HS256"])
        username = payload.get("username")
        return JsonResponse({
            "message": f"Welcome {username}, this is your dashboard!",
            "success": True
        })

    except jwt.ExpiredSignatureError:
        return JsonResponse({"message": "Token has expired", "success": False}, status=401)
    except jwt.InvalidTokenError:
        return JsonResponse({"message": "Invalid token", "success": False}, status=401)
