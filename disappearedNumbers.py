class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

    # Extra space solution: hashing each value and then doing lookups
    # Linear runtime
        my_dict = {}
        res = []
        for i in range(len(nums)):
            my_dict[nums[i]] = nums[i]
        for x in range(1,len(nums)+1):
            if x not in my_dict:
                res.append(x)
        return res

        
    # O(n^2) runtime with no extra space (bad solution)
        '''
        res=[]
        for i in range(1,len(nums)+1):
            res.append(i)
        for x in range(len(nums)):
            if nums[x] in res:
                res.remove(nums[x])
        return res
        '''

    # Better solution: iterating and negating the values at index value of the current number, and returning all indices of pos. values.