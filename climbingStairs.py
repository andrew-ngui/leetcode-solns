# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1 or n == 2:
            return n
    
        lst = []
        lst.append(1)
        lst.append(2)
        
        for i in range(2,n):
            lst.append(lst[i-1] + lst[i-2])
        return lst[n-1]
            
# Better solution: memoization: we only need the previous and current