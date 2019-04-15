class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:












        # Procedures:
        #
        # grid = given
        # top/bottom = 1. transpose of grid, 2. max of the rows of new matrix in a new 1D matrix
        # left/right = Max of all rows of grid in new 1D matrix
        # newGrid = 1. if grid[i][j] < max[j] then newGrid[i][j] = max(grid[i][j]), 2. sum += newGrid[i][j] - grid[i][j]
