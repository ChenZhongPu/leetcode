class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
        	return s
        longest = ''
        for i in range(len(s) - 1):
        	temp = self.findPalindrome(s, i, i)
        	if len(temp) > len(longest):
        		longest = temp
        	temp = self.findPalindrome(s, i, i + 1)
        	if(len(temp) > len(longest)):
        		longest = temp
        return longest
        
    def findPalindrome(self, s, left, right):
    	while left >= 0 and right < len(s) and s[left] == s[right]:
    		left -= 1
    		right += 1
    	return s[left+1:right]