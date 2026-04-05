# Given an array arr, rotate the array by one position in clockwise direction.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]
# Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.



class Solution:
    def rotate(self, arr):
        # solution-1
        n = len(arr)
        for i in range((n-1)//2):
            arr[i], arr[n-2-i] = arr[n-2-i], arr[i]
            
        for i in range(n//2):
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
            
        return arr  
        
        # solution-2
        n = len(arr)
        last = arr[n-1]
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1]
        
        arr[0] =   last
        return arr