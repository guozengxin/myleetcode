class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) & 1 != 0:
            return False
        stack = []
        mymap = {'}':'{', ']':'[', ')': '('}

        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif c not in mymap:
                    return False
                elif mymap[c] != stack[-1]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

strs = [
    '()',
    '{()}[]',
    '{(})',
]

solu = Solution()
for s in strs:
    print s, solu.isValid(s)
