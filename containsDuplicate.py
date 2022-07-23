# https://leetcode.com/problems/contains-duplicate/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = i
            else:
                return True
        return False

# A dictionary functioning similar to a hashmap.
# We iterate through our numbers, and check if we have already hashed this value
# If not found, hash the current value and continue iterating