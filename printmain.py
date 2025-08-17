'''a=5
print(a)
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
print(dict["name"])'''

def func1(name,age):
    print("student",name,"Age:",age)
func1("Anshika",99999)
list1=[1,2,3,4,5,6]
for i in list1:
    print(i,end=" ")
print()
for i in range(1,9,2):
    print(i,end=" ")
print()
for i in range(0,10):
    print(i*2)

for i in range(1,4):
      print("Table of ",i)
      for j in range(1,5):
            print(i,"X",j,"=",i*j)
fruits=["apple","cherry","banana","mango"]
print("break")
for i in fruits:
   if i=="banana":
      print("fruit:",i)
      break
print("continue")
for i in fruits:
   if i=="banana":
       continue
   print("fruit:",i)
def sum_number(n):
  sum=0
  for i in range(1,n):
         sum=sum+i
  return sum
print("sum of numbers",sum_number(5))


def count_vowels(str):
 count=0
 for ch in str:
  if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
     count+=1
 return count

print(count_vowels("America ya"))

vowels=["a","e","i","o","u","A","E","I","O","U"]
def count_vowel(str,vowels):
 count=0
 for ch in str:
   if ch in vowels:
     count+=1
 return count

print(count_vowel("Ye mera India , I love my Indiyaaaaaaaaa",vowels))
list2=[]
def square(n):
  for i in n:
    list2.append(i*i)
  return list2
print(square(list1))

def reverse(str):
   str1=""
   for i in range(0,len(str)):
      str1=str[i]+str1
   return str1
print(reverse("apple"))
print(len([1,3,4,2,3,3,4]))
print("words and length")
def word_length(list):
  for i in list:
      print(i,len(i))
word_length(fruits)

def factorial(n):
    fact=1
    i=1
    while i<=n:
       fact=fact*i
       i=i+1
    return fact
print(factorial(-5))
