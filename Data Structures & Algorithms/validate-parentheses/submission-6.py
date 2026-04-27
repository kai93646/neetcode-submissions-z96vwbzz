class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']': '[', '}': '{'}
        result = list()
        for i in range(0, len(s)):
            if result and match.get(s[i], 0) == result[-1]:
                result.pop()
            else:
                result.append(s[i])
            print(result)
        if result:
            return False
        else:
            return True