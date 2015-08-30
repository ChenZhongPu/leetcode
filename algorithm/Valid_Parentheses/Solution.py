class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pareStack = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                pareStack.append(p)
            elif p == ')':
                if not pareStack:
                    return False
                temp = pareStack.pop()
                if temp != '(':
                    return False
            elif p == ']':
                if not pareStack:
                    return False
                temp = pareStack.pop()
                if temp != '[':
                    return False
            elif p == '}':
                if not pareStack:
                    return False
                temp = pareStack.pop()
                if temp != '{':
                    return False
        if pareStack:
            return False
        return True