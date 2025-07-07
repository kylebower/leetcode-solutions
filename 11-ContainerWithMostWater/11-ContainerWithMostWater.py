# Last updated: 7/7/2025, 7:07:04 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r:
            cur = min(height[l], height[r]) * (r-l)
            res = max(cur, res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res