class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastRepeatPos = -1
        length = 0
        m = {}
        for i, v in enumerate(s):
        	if v in m and lastRepeatPos < m[v]:
        		lastRepeatPos = m[v]
        	if i - lastRepeatPos > length:
        		length = i - lastRepeatPos
        	m[v] = i
        return length;