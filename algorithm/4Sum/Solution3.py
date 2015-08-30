class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i-1]==nums[i]:
                continue
            temps = self.threeSum(nums[i+1:], target - nums[i])
            for temp in temps:
                temp.insert(0, nums[i])
                result.append(temp)
        return result     
        
    def threeSum(self, nums, target):
    	n = len(nums)
    	result = []
    	for i in range(n-2):
    		if i > 0 and nums[i-1]==nums[i]:
    			continue
    		a = nums[i]
    		left = i + 1
    		right = n - 1
    		while left < right:
    			b = nums[left]
    			c = nums[right]
    			if a + b + c == target:
    				result.append([a, b, c])
    				while left < n - 1 and nums[left] == nums[left + 1]:
    					left += 1
    				while right > 0 and nums[right] == nums[right - 1]:
    					right -= 1
    				left += 1
    				right -= 1
    			elif a + b + c > target:
    				while right > 0 and nums[right] == nums[right - 1]:
    					right -= 1
    				right -= 1
    			else:
    				while left < n - 1 and nums[left] == nums[left + 1]:
    					left += 1
    				left += 1
    	return result