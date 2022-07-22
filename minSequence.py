# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
# Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 
# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 
# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

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


# Start by sorting our numbers in descending order
# We want to find the index such that the sum before the specified index is greater than the sum of the values following the index
