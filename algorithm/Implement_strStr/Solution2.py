class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
        	return 0
        if not haystack:
        	return -1
        m = len(haystack)
        n = len(needle)
        match = self.kmpPreprocessing(needle)
        j = -1
        for i in range(m):
        	while j >= 0 and haystack[i] != needle[j+1]:
        		j = match[j]
        	if haystack[i] == needle[j+1]:
        		j += 1
        	if j == n-1:
        		return i-n+1
        return -1

    def kmpPreprocessing(self, needle):
    	n = len(needle)
    	match = [-1 for i in range(n)]
    	j = -1
    	for i in range(1, n):
    		while j >= 0 and needle[i] != needle[j+1]:
    			j = match[j]
    		if needle[i] == needle[j+1]:
    			j += 1
    		match[i] = j
    	return match
