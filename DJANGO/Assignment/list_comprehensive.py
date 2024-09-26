#Multiplication table by using list comprehensive
#1
# n=9
# s=["{} x {} = {}".format(n,x,n*x) for x in range(1,11)]
# print("\n".join(s))


#Star patter by using list comprehensive
#2
# s=[i*"* " for i in range(1,6)]
# print("\n".join(s))


# 3 Unique vowels by using list comprehensive
#A
# string=input("enter the string:")
# vowels="aeiouAEIOU"
# s=[vowel for vowel in vowels if vowel in string ]
# print(" ".join(s))


# Unique vowels by using normal method
#B
# string=input("enter the string:")
# vowels="aeiouAEIOU"
# adding=""
# for i in string:
#     if i in vowels:
#         adding+=i
# print(adding)


# Given input string is convert lower case to upper case
#4
# words=input("enter the string:")
# s=[word.upper() for word in words]
# print(s)

# Count of words
#5
# words=["a","a","f","g","g","h","h","p"]
# s=["{} repeated at {} times".format(i,words.count(i)) for i in words]
# a=set(s)
# n=list(s)
# print(n)





    
    
        
        
        








