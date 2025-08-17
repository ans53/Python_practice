from add import Add
#list of only unique elements
def unique_elements(lst):
     lst1=[]
     for i in lst:
         if lst[i] not in lst1:
            lst1.append(i)
     return lst1
old=[1,2,2,3,4,4,2,5,1]
print(unique_elements(old))

# longest word in a string
def longest_word(sentence):
    str=""
    longest=""
    list=[]
    max=0
    for i in sentence: 
       str=str+i  
       if(i==" "):
          list.append(str)
          str=""
    for i in list:
         if len(i)>max:
            longest=i
    return longest
print(longest_word("Python is an amazing programming language")) 
       
#Sum of digits of a number
def sum_of_digits(num):
    sum=0
    while num>0:
          digit=int(num%10)  
          sum+=digit
          num=int(num/10) 
 
    return sum
print("Sum of digits:",sum_of_digits(12345))

# Check if a number is divisible by 3 or 5
def divisible_by_3or5():
    result = []
    for i in range(1, 101):
         if (i % 3 == 0 or i % 5 == 0):
            result.append(i)
    return result
print("Number divisible by 3 or 5",divisible_by_3or5())


#Count number of Consonants
vowels=["a","e","i","o","u","A","E","I","O","U"]
def count_consonant(str,vowels):
 count=0
 for ch in str:
   if ch not in vowels:
     count+=1
 return count

print(count_consonant("Ye mera India , I love my Indiyaaaaaaaaa",vowels))

#Reverse a String
def reverse_string_words(str): 
    reverse=""
    for i in str:
        if(str==" "):
           reverse=i+reverse
          
    return reverse
print("Reverse of String:",reverse_string_words("Python is Good"))
    

#Rotate a List
def rotate_list(lst, k):
    new_list=[]
    n = len(lst)
    k = k %n
    # take last k elements
    for i in range(n - k, n):
        new_list += [lst[i]]
    # take first n-k elements
    for i in range(0, n - k):
        new_list += [lst[i]]
    return new_list
print(rotate_list([1, 2, 3, 4, 5], 2))


#Count frequency of character
def char_frequency(s):
    freq = {}  
    for ch in s:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
    return freq

print(char_frequency("hello"))

#Diamond Pattern
def diamond_pattern(n):
    for i in range(1, n+1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

    for i in range(n-1, 0, -1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

diamond_pattern(5)
print(Add(2,3))