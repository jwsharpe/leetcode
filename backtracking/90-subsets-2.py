class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        subset = []

        def dfs(i):
            if i >= len(nums):
                if subset not in res:
                    res.append(subset.copy())
                return

            # include
            subset.append(nums[i])
            dfs(i + 1)

            # dont include
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
