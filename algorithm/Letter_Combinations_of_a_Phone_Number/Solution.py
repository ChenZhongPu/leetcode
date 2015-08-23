class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits:
        	return res
        cand = []
        self.dfs(digits, 0, cand, res)
        return res

    def dfs(self, digits, n, cand, result):
    	m = {'2':'abc', '3':'def', '4':'ghi',
    	'5':'jkl', '6':'mno', '7':'pqrs',
    	'8':'tuv', '9':'wxyz'}
    	if n == len(digits):
    		result.append(''.join(cand))
    	else:
	    	for letter in m[digits[n]]:
	    		cand.append(letter)
	    		self.dfs(digits, n+1, cand, result)
	    		cand.pop()