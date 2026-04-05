# Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

# Note: Consider the array as circular.

# Examples :

# Input: arr[] = [1, 2, 3, 4, 5], d = 2
# Output: [3, 4, 5, 1, 2]
# Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.



class Solution:
    def rotateArr(self, arr, d):
        # Solution-1
        
        n=len(arr)
        for i in range(d):
            first = arr[0]
            for j in range(n-1):
                arr[j] = arr[j+1]
            
            arr[n-1] = first
        return arr        
        
        
        # Solution-2
        
        n=len(arr)
        d %= n
        new_arr = [0]*n
        
        for i in range(n-d):
            new_arr[i] = arr[d+i]
        
        for i in range(d):
            new_arr[n-d+i] = arr[i]
            
        for i in range(n):
            arr[i] = new_arr[i]
        
        return arr    
        
        
        # Solution-3
           
        n=len(arr)
        d %= n
        self.reverse(arr, 0, d-1)
         
        self.reverse(arr, d, n-1)
         
        self.reverse(arr, 0, n-1)
         
         
    def reverse(self, arr, start, end):
             while start < end:
                 arr[start], arr[end] = arr[end], arr[start]
                 start += 1
                 end -= 1
        