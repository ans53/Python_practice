'''a=5
print(a)'''
a=int(input("enter a number: "))
if a%2==0:
   print("even")
else:
   print("odd")
dict={"name":"Rohan", "age":67,"salary":89000};
list=["s",78,7,6,8,8]
for i in list:
      print(i)
print(list[0:3])
list.append(4)
list.extend([9,3])
list.remove("s")
list.reverse()
print(list.count(8))
print(dict)
print(list) 
str="      Lovely   ,girl    "
print(str.upper())
print(str.lower())
print(str.replace("o","g"))
print(str.strip())
print(str.strip().split(","))
print(str.capitalize())
print(str.title())
print(str[1:9])
print(len(str))
print(dict.values())
print(dict.keys())
print(dict["name"])