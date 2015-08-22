class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        length = 0
        temp = x
        while temp > 0:
        	length += 1
        	temp = temp // 10
        if length <= 1:
        	return True
        i = 0
        rightHalf = 0
        while i < length // 2:
        	rightHalf = rightHalf * 10 + x % 10
        	x = x // 10
        	i += 1
        if length % 2 == 1:
        	x = x // 10
        if rightHalf == x:
        	return True
        else:
        	return False