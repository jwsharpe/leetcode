class Solution(object):
    def containsDuplicate(self, nums):
        memo = set()
        for n in nums:
            if n in memo:
                return True
            memo.add(n)
        return False
