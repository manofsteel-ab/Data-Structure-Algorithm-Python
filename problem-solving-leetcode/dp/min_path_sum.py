class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0]*cols for i in range(rows)]

        dp[0][0] = grid[0][0]

        for i in range(1,cols):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for i in range(1,rows):
            dp[i][0] = dp[i-1][0]+grid[i][0]

        for i in range(1, rows):
            for j in range(1,cols):
                dp[i][j] = grid[i][j]+min(dp[i-1][j], dp[i][j-1])

        return dp[rows-1][cols-1]
