# def maxSubArrayAndMaxSum(nums):
#     l = len(nums)
#     maxSum = -99999999999999999999 # float(-ve)
#     maxSubarray = []    

#     for i in range(l):
#         currentSum = 0
#         currentSubArray = []
#         for j in range(i,l):
#             currentSum=currentSum+nums[j]
#             currentSubArray.append(nums[j])

#             if maxSum<currentSum:
#                 maxSum = currentSum
#                 maxSubarray = currentSubArray.copy()

#     print(maxSum)
#     print(maxSubarray)


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
# maxSubArrayAndMaxSum(nums)