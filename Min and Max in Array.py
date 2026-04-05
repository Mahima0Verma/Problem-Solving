# Given an array arr[]. Your task is to find the minimum and maximum elements in the array.

# Examples:

# Input: arr[] = [1, 4, 3, 5, 8, 6]
# Output: [1, 8]
# Explanation: minimum and maximum elements of array are 1 and 8.


# class Solution:
#     def getMinMax(self, arr):
#         # code here
#         min_num = arr[0]
#         max_num = arr[0]
#         for num in arr:
#             if num < min_num:
#                 min_num = num
                
#             elif num > max_num:
#                 max_num = num
                
#         return  min_num, max_num        