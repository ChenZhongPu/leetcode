import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        delta = sys.maxsize
        resultTarget = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
        	if i > 0 and nums[i] == nums[i - 1]:
        		continue
        	a = nums[i]
        	start = i + 1
        	end = n - 1
        	while start < end:
        		b = nums[start]
        		c = nums[end]
        		tempSum = a + b + c
        		if tempSum == target:
        			return target
        		else:
        			if abs(tempSum - target) < delta:
        				delta = abs(tempSum - target)
        				resultTarget = tempSum
        			if tempSum > target:
        				while end > 0 and nums[end] == nums[end - 1]:
        					end -= 1
        				end -= 1
        			if tempSum < target:
        				while start < n - 1 and nums[start] == nums[start + 1]:
        					start += 1
        				start += 1
        return resultTarget