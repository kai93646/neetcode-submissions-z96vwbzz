class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        check = 1000000
        a = 0
        while a < len(nums):
            b = a + 1
            c = len(nums) - 1
            while b < c:
                if nums[b] + nums[c] + nums[a] == 0:
                    ans.add(tuple([nums[a], nums[b], nums[c]]))
                    b += 1
                    c -= 1
                elif nums[b] + nums[c] + nums[a] < 0:
                    b += 1
                else:
                    c -= 1
            a += 1
        return list(ans)
            

