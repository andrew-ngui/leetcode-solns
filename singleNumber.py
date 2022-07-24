# https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        itr = 0
        for i in range(len(nums)):
            itr ^= nums[i]
        return itr


# XOR all of the values together
# We know that XORing two identical values will return 0