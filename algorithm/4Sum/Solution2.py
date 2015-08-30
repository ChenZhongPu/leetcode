class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numLen, res, dic = len(nums), set(), {}
        if numLen < 4:
        	return []
        nums.sort()
        for p in range(numLen):
        	for q in range(p+1, numLen):
        		if nums[p] + nums[q] not in dic:
        			dic[nums[p] + nums[q]] = [(p, q)]
        		else:
        			dic[nums[p] + nums[q]].append((p, q))
        for i in range(numLen):
        	for j in range(i+1, numLen-2):
        		t = target-nums[i]-nums[j]
        		if t in dic:
        			for k in dic[t]:
        				if k[0] > j:
        					res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [list[i] for i in res]