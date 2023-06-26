class Solution:
    def trap(self, height: List[int]) -> int:
        sumOfWater = 0
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0
        while l < r:
            maxL, maxR = max(maxL, height[l]), max(maxR, height[r])

            if maxL > maxR:
                r -= 1
                water = min(maxL, maxR) - height[r]
                if water < 0:
                    water = 0
                sumOfWater += water
            else:
                l += 1
                water = min(maxL, maxR) - height[l]
                if water < 0:
                    water = 0
                sumOfWater += water
        
        return sumOfWater
