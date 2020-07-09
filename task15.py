import numpy as np

def print_grid(grid: np.ndarray, just=False):
    max_len = len(str(max(grid.flatten())))
    for l in grid:
        for c in l:
            if just:
                print(str(c).ljust(max_len), end=' ')
            else:
                print(c, end=' ')
        print('\n')
    print()

if __name__ == "__main__":
    n = 20
    grid = np.zeros((n+1,n+1), dtype=object)

    # init boundary elements
    for l in range(n+1):
        for c in range(n+1):
            if l == n or c == n:
                grid[l][c] = 1
    
    # init others
    for l in reversed(range(n)):
        for c in reversed(range(n)):
            grid[l][c] = grid[l][c+1] + grid[l+1][c]

    print_grid(grid)

