# Sum of all the numbers from 1 to given number
# n=10
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# Multiplication table from given number
n=10
# i=1
# while i <= n:
#     print("10 x ",i,"=",10*i)
#     i=i+1

#Display number from a list using loop
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     print(i)

#Count total number of digits
# numbers=[1,2,3,4,5,6,7,8]
# count=0
# for i in numbers:
#     count=count+1
# print(count)

#Print list using reverse order
# list=[1,2,3,4,5,6,7,8]
# reversed_list=[]
# for value in list:
#     reversed_list=[value]+reversed_list
# print(reversed_list)

#Displa neagtive numbers from -10 to -1 
#n=10
#for i in range(n):
#    print(i-n)

#Use else block to display done message
# n=10
# for i in range(n):
#     print(i)
# else:
#     print("Done")

# print prime numbers from range
# n=20
# for i in range(2,n+1):
#     for j in range(2,i):
#         if(i%j) == 0:
#             break
#     else:print(i,end=" ")
    

#Fibonacci series
num=int(input("enter the number: "))
n1,n2=0,1
sum=0
if num<=0:
    print("please enter the greater than 0")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1=n2
        n2=sum
        sum=n1+n2




