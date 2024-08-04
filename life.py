#!/usr/bin/python3

directions = [
    [-1, -1], [0, -1], [1, -1],
    [-1, 0], [1, 0],
    [-1, 1], [0, 1], [1, 1]
]

def in_bounds(grid, x, y) -> bool:
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)


# TODO: better func name
def rebound(grid, x, y):
    # This is an alternative way to handle out of bounds by having the out of 
    # bounds by looping the value back to the beginning to prevent the error
    # This would allow automata to cycle forever rather than stopping at the
    # map edges
    
    # w = 5
    # x = 7 -> x = 3
    raise NotImplementedError("See function source code")

def check_tile(grid, new, x, y):
    neighbours = 0

    for d in directions:
        dx = x + d[0]
        dy = y + d[1]
        if in_bounds(grid, dx, dy):
            neighbours += grid[dy][dx]

    if neighbours < 2 or neighbours > 3:
        new[y][x] = 0
    if not grid[y][x] and neighbours == 3:
        new[y][x] = 1

def check_grid(grid):
    w = len(grid[0])
    h = len(grid)

    new = [[c for c in line] for line in grid]

    for y in range(h):
        for x in range(w):
            check_tile(grid, new, x, y)

    return [[c for c in line] for line in new]

def print_grid(grid):
    for line in grid:
        line = map(str, line)
        print(" ".join(line).replace("0", ".").replace("1", "#"))

def make_grid(text):
    lines = text.strip().split("\n")
    grid = [list(map(int, line)) for line in lines]
    return grid

def main():
    import time

    text = """
10010000000000000000000000000000000000
00001000000000000000000000000000000000
10001000000000000000000000000000000000
01111000000000000000000000000000000000
00000000000000000000000000000000000000
00000000000000000000000000000000000000
00000000000000000000000000000000000000
00000000000000000000000000000000000000
00000000000000000000000000000000000000
00000000000000000000000000000000000000
00000000000000000000000000000000000000
00000000000000000000000000000000000000
"""
    grid = make_grid(text)

    while 1:
        print_grid(grid)
        grid = check_grid(grid)
        time.sleep(0.5)
        print(f"\033[{len(grid)}A", end="")

if __name__ == "__main__":
    main()
