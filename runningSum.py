# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums

# We only need to iterate once through the list, and we are space efficient by calculating in-place