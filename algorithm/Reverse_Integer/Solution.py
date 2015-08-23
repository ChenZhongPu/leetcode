class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        magic = 214748364
        y = 0
        if x < 0:
        	if x == -2147483648:
        		return 0
        	isNegative = True
        	x = -x
        while x != 0:
        	n = x % 10
        	if isNegative:
        		if -y < - magic:
        			return 0
        	else:
        		if y > magic:
        			return 0
        	y = y * 10 + n
        	x = x // 10
        return -y if isNegative else y