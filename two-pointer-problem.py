# As we know, Ishaan has a love for chocolates. He has bought a huge chocolate bar that contains N chocolate squares. Each of the squares has a tastiness level which is denoted by an array A[].
# Ishaan can eat the first or the last square of the chocolate at once. Ishaan has a sister who loves chocolates too and she demands the last chocolate square. Now, Ishaan being greedy eats the more tasty square first. 
# Determine the tastiness level of the square which his sister gets.

# Example 1:

# Input : arr[ ] = {5, 3, 1, 6, 9}
# Output : 1
# Explanation:
# Initially: 5 3 1 6 9
# In first step: 5 3 1 6
# In Second step: 5 3 1
# In Third step: 3 1
# In Fourth step: 1
# Return 1



from typing import List


class Solution:
    def chocolates(self, n : int, arr : List[int]) -> int:
        
        # solution-1 (Naive)
        small = arr[0]
        for i in range(1,n):
            if arr[i]< small:
                small = arr[i]
        
        return small 
        
        # solution-2 (Two pointer)
        left = 0
        right = n-1
        
        while left < right:
            if arr[left] > arr[right]:
                left+=1
            
            else:
                right-=1
        return arr[left]        
            