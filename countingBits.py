# https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        
        for i in range(n+1):
            x = 0
            binary = bin(i)[2:]
            for num in map(int,binary):
                if num is 1:
                    x+=1
            res.append(x)
        return res
            
# A naive solution: iterate up to n, generate the binary representation, and iterate the binary value looking for 1's
# A clever solution: https://leetcode.com/problems/counting-bits/discuss/79538/Simple-Python-Solution