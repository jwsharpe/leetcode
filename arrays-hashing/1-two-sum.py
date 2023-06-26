class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complimentIndex = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if None != complimentIndex.get(compliment):
                return [i, complimentIndex[compliment]]
            complimentIndex[nums[i]] = i
