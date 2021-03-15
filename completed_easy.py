# https://leetcode.com/problems/running-sum-of-1d-array/
def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]
    return nums

# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
def minSequence(nums):
    """
    nums: list[int]
    rtype: list[int]
    """
    nums.sort(reverse=True)

    if (len(nums) == 1):
        return nums
    before_i = 0
    after_i = sum(nums)
    for i in range(len(nums)):
        before_i += nums[i]
        after_i -= nums[i]

        if before_i > after_i:
            break
    return nums[:i+1]
