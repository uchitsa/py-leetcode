def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    mxLoc = [[0] * (n - 2) for _ in range(n - 2)]
    for i in range(n - 2):
        for j in range(n - 2):
            mxLoc[i][j] = max(max(row[j:j + 3]) for row in (grid[i:i + 3]))
    return mxLoc


if __name__ == '__main__':
    print(largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
    print(largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
