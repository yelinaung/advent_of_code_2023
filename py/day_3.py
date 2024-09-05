f = "input/day_3.txt"


def grid() -> list[str]:
    return [line.strip() for line in open(f).readlines()]


g = grid()


def is_symbol(char):
    return char not in "0123456789."


def get_number(grid, row, column):
    left = column
    while left > 0 and grid[row][left - 1].isdigit():
        left -= 1
    right = column
    while right < len(grid[row]) - 1 and grid[row][right + 1].isdigit():
        right += 1
    return grid[row][left : right + 1], left, right


def is_adjacent(grid, row, column, left_bound, right_bound):
    for row_offset in range(-1, 2):
        for column_offset in range(-1, 2):
            for index in range(left_bound, right_bound + 1):
                adj_row = row + row_offset
                adj_col = column + column_offset + index - left_bound
                if 0 <= adj_row < len(grid) and 0 <= adj_col < len(grid[adj_row]):
                    if is_symbol(grid[adj_row][adj_col]):
                        return True
    return False


total = 0
visited = set()
for row in range(len(g)):
    for column in range(len(g[row])):
        if g[row][column].isdigit() and (row, column) not in visited:
            number, left, right = get_number(g, row, column)
            if number and is_adjacent(g, row, column, left, right):
                total += int(number)

            for index in range(left, right + 1):
                visited.add((row, index))

print(total)
