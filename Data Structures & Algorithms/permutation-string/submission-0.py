class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        element = dict()
        for i in range(0, len(s1)):
            element[s1[i]] = element.get(s1[i], 0) + 1
        if len(s1) > len(s2):
            return False
        
        for i in range(0, len(s2) - len(s1) + 1):
            temp = element.copy()
            for j in range(i, i + len(s1)):
                a = temp.get(s2[j], 0)
                if a != 0:
                    temp[s2[j]] -= 1
            if max(temp.values()) == 0:
                return True
        return False