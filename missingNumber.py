class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(len(nums)):
            if i+1 != len(nums):
                if nums[i+1] != nums[i] + 1:
                    return nums[i]+1
            else:
                return i+1

# Sort our input list and iterate to find the missing num
# To improve it: sum an iterator variable and compare to the sorted list

# Better solution: comparing sums of values
# Alternative: bitwise