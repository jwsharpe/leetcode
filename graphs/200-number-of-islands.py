class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() # tuple points
        res = 0 # number of islandcs

        def dfs(r, c):
            if(
                ROWS <= r or
                COLS <= c or
                r < 0 or
                c < 0 or
                grid[r][c] == "0" or
                (r,c) in visited
            ):
                return

            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (
                    (r,c) not in visited and
                    grid[r][c] == "1"
                ):
                    res += 1
                    dfs(r,c) 

        return res
