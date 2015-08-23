class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
        	if i > 0 and nums[i - 1] == nums[i]:
        		continue
        	a = nums[i]
        	start = i + 1
        	end = len(nums) - 1
        	while start < end:
        		b = nums[start]
        		c = nums[end]
        		if a + b + c == 0:
        			result.append([a, b, c])
        			while start < len(nums) - 1 and nums[start] == nums[start + 1]:
        				start += 1
        			while end > 0 and nums[end] == nums[end - 1]:
        				end -= 1
        			start = start + 1
        			end = end - 1
        		elif a + b + c > 0:
        			while end > 0 and nums[end] == nums[end - 1]:
        				end -= 1
        			end = end - 1
        		else:
        			while start < len(nums) - 1 and nums[start] == nums[start + 1]:
        				start += 1
        			start = start + 1
        return result