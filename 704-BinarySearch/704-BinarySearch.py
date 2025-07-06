# Last updated: 7/6/2025, 1:04:13 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r-l)//2
            cur = nums[mid]
            if cur == target:
                return mid
            elif cur > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
