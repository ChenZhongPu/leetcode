class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [0, 0]
        valueMap = {}
        for i, v in enumerate(nums):
        	if v not in valueMap:
        		valueMap[target - v] = i
        	else:
        		result[0] = valueMap[v] + 1
        		result[1] = i + 1
        		break
        return result