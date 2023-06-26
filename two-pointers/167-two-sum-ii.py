class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sumTarget = numbers[l] + numbers[r]
            if target == sumTarget:
                return [l + 1, r + 1]
            if target > sumTarget:
                l += 1
            else:
                r -= 1
        
        return []
