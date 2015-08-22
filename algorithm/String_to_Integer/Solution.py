class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
        	return 0
        sign = 1
        str = str.lstrip()
        if str[0] == '+':
        	str = str[1:]
        elif str[0] == '-':
        	str = str[1:]
        	sign = -1
        elif not str[0].isdigit():
        	return 0
        if not str:
        	return 0
        result = 0
        MAX_INT = 2147483647
        MIN_INT = - 2147483648
        for s in str:
        	if s.isdigit():
        		result = 10 * result + int(s)
        		if sign == 1:
        			if result > MAX_INT:
        				return MAX_INT
        		else:
        			if result > MAX_INT + 1:
        				return MIN_INT
        	else:
        		break
        return sign * result