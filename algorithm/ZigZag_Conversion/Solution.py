class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows <= 1 or numRows >= len(s):
			return s
		row = 0
		step = 1
		result = ['' for i in range(numRows)]
		for v in s:
			if row == numRows - 1:
				step = -1
			elif row == 0:
				step = 1
			result[row] += v
			row += step
		return ''.join(result)