class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        his = {}
        left = 0
        result = 0
        for right in range(0, len(s)):
            his[s[right]] = his.get(s[right], 0) + 1
            while (right - left + 1) - max(his.values()) > k:
                his[s[left]] -= 1
                left += 1
                
            result = max(result, (right - left + 1))
        
        return result