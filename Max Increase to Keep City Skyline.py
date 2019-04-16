class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        transposeGrid = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
        topView = list(map(max, transposeGrid))

        sideView = list(map(max, grid))

        sum = 0
        newGrid = []
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] <= sideView[i]:
                     if sideView[i] <= topView[j]:
                         newGrid.append(sideView[i])
                     else:
                         newGrid.append(topView[j])

        flatGrid = []
        for x in grid:
            for y in x:
                flatGrid.append(y)

        for l in range(0, len(newGrid)):
            sum += newGrid[l] - flatGrid[l]

        return sum
