def numIslands(grid: list[list[str]]) -> int:
    if len(grid) == '0':
        return 0
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                cnt += 1
                markIslands(grid, i, j)
    return cnt


def markIslands(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
        return
    grid[i][j] = '0'
    markIslands(grid, i - 1, j)
    markIslands(grid, i + 1, j)
    markIslands(grid, i, j - 1)
    markIslands(grid, i, j + 1)


if __name__ == '__main__':
    print(numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
    print(numIslands(
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
