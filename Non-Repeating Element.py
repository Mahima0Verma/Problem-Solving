# Find the first non-repeating element in a given array arr of integers and if there is not present any non-repeating element then return 0

# Note: The array consists of only positive and negative integers and not zero.

# Examples:

# Input: arr[] = [-1, 2, -1, 3, 2]
# Output: 3




class Solution:
    def firstNonRepeating(self, arr): 
        # Solution-1
        
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i!=j and arr[i]==arr[j]:
                    break
            else: 
                return arr[i]
        
        return 0  
        
        # Solution-2
        
        n = len(arr)
        freq ={}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i]=1
        
        for i in freq:
            if freq[i]==1:
                return i
        
        return 0 