# def newStack():
#     stack = []
#     return stack

# def isEmpty(stack): # checking if the stack is empty
#     return len(stack) == 0


# # adding elements
# def push(stack,item):
#     stack.append(item)

# # popping elements
# def pop(stack):
#     if isEmpty(stack):
#         return("nothing to pop")
#     else:
#         stack.pop()

# stack = newStack()
# push(stack, "SR")
# push(stack, "AS")
# push(stack, "MC")
# push(stack, "PNM")
# push(stack, "SR")
# push(stack, "RP")
# push(stack, "SR")
# pop(stack)
# push(stack, "AS")
# print(stack)


#2valid parenthesis and non valid parenthesis
# def validParenthesis(s):
#     stack = []
#     mapping  = {
#         "}":"{",
#         ")":"(",
#         "]":"["
#     }

#     for bracket in s:
#         if bracket in mapping:
#             if stack:
#                 topElement = stack.pop()
#             else:
#                 return("invalid parenthesis")
            
#             if mapping[bracket] != topElement:
#                 return False
#         else:
#             stack.append(bracket)

#     if len(stack) == 0:
#         return("valid parenthesis")
        

# inputString = "()[]{[]}()"
# print(validParenthesis(inputString))

#3
# def twoSum(a,t):
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j] == target:
#                 return([i,j])
                
            
# arr = [8,9,1,3,4,5,6]
# target = 17
# callingTheFunc = twoSum(arr,target)
# print(callingTheFunc)
# time complexity O(n^2)

#4
# arr = [1,3,4,5,6,8,9]
# target = 9
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)
# if n is length of array what wil be the time complexity 
# O(n)
#Big O notation



#[1,3,4,5,6,8,9]

# 1+3     4+5
# 1+4     4+6
# 1+5     4+8
# 1+6     4+9
# 1+8
# 1+9     5+6
#         5+8
# 3+4     5+9
# 3+5    
# 3+6     6+8
# 3+8     6+9
# 3+9     8+9