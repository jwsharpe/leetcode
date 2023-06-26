class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        neighborSet = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in neighborSet:
                length = 0
                while n+length in neighborSet:
                    length += 1
                longest = max(length, longest)

        return longest
