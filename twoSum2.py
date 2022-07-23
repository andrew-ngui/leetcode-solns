# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        my_dict = {}
        # key is the number; value is the index
        
        for i in range(len(numbers)):
            num1 = numbers[i]
            num2 = target - num1
            if num2 in my_dict:
                ind2 = my_dict[num2]
                lst = [i+1, ind2+1]
                return sorted(lst)
            my_dict[num1] = i


# A dictionary functioning similar to a hashmap.
# We iterate through our numbers, and check if we have hashed the other number we need to reach target
# If not found, hash the current value and continue iterating


# A different solution: two-pointers method