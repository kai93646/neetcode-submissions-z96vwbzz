class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            sortS = ''.join(sorted(i))
            ans[sortS].append(i)
        return list(ans.values())