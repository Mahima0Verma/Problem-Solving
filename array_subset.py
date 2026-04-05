# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

# Examples:

# Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# Output: true
# Explanation: b[] is a subset of a[]



class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
    
        # solution-1(but not handled duplicates)
        for i in b:
            if i not in a:
                return False
                
        return True  
        
        # solution-2 (O(n+m))
        freq = {}
        
        for i in a:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        
        for i in b:
            if i not in freq or freq[i] == 0:
                return False
                
            freq[i] -= 1    
        
        return True  