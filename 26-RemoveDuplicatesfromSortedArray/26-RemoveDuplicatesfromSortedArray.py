# Last updated: 7/9/2025, 10:46:28 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        res = 1
        n = len(nums)

        while k < n:
            if nums[k] == nums[res-1]:
                k += 1
            else:
                nums[res] = nums[k]
                k += 1
                res += 1
        return res


