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
        hayLen = len(haystack)
        needleLen = len(needle)
        i = 0
        j = 0
        while i < hayLen and j < needleLen:
        	if haystack[i] == needle[j]:
        		i += 1
        		j += 1
        	else:
        		i = i - j + 1
        		j = 0
        if j == needleLen:
        	return i - j
        else:
        	return -1

    # def strStr2(self, haystack, needle):
    # 	n = len(haystack)
    # 	m = len(haystack)
    # 	for i in range(0, n-m+1):
    # 		for j in range(0, m+1):
    # 			if j == m:
    # 				return i
    # 			if haystack[i+j] != needle[j]:
    # 				break
    # 	return -1
