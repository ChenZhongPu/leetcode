class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        valueMap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = valueMap[s[0]]
        for i in range(1, len(s)):
        	prev = valueMap(s[i - 1])
        	curr = valueMap(s[i])
        	if prev < curr:
        		result = result - prev + (curr - prev)
        	else:
        		result += curr
        return result