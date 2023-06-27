class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)

            res = 0
            for d in str(n):
                res += pow(int(d),2)
            n = res
        return True
