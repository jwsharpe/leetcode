class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minValue = 1_000_000_000
        while l <= r:
            m = (l + r) // 2
            minValue = min(nums[m], minValue)
            rv, lv, mv = nums[r], nums[l], nums[m]
            if rv > lv and rv > mv:
                r = m - 1
            elif rv < lv and rv > mv:
                r = m - 1
            else:
                l = m + 1
        return minValue
