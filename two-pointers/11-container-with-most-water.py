class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAr = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[r], height[l])
            maxAr = max(maxAr, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return maxAr
