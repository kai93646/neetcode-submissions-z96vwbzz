class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in nums:
            record.setdefault(i, 1)
        for i in range(0, len(nums)):
            temp = record.get(target - nums[i], 0)
            if temp == 1:
                for y in range(i+1, len(nums)):
                    if nums[y] == target - nums[i]:
                        ans = [i, y]
                        return ans