class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        y = 0
        if x < 0:
        	if x == MIN_INT:
        		return 0
        	isNegative = True
        	x = -x
        while x != 0:
        	n = x % 10
        	if isNegative:
        		if -y < (MIN_INT + n) / 10:
        			return 0
        	else:
        		if y > (MAX_INT - n) / 10:
        			return 0
        	y = y * 10 + n
        	x = x // 10
        return -y if isNegative else y