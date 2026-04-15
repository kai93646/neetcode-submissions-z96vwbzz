class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for i in nums:
            res[i] += 1
        ans = sorted(res.keys(), key=lambda s: res[s], reverse=True)
        return ans[0:k]