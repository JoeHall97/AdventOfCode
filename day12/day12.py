directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
]


def boundsCheck(x: int, y: int, input: list[list[any]]) -> bool:
    return y >= 0 and y < len(input) and x >= 0 and x < len(input[y])


def getFenceCost(input: list[str],
                 row: int,
                 column: int) -> tuple[int, set[tuple[int, int]]]:
    fence_count = 0
    symbol_count = 0
    positions = set()
    frontier = [(row, column)]
    curr_symbol = input[row][column]
    while frontier:
        curr_row, curr_column = frontier.pop()
        for d in directions:
            pos = (curr_row + d[0], curr_column + d[1])
            if pos in frontier or pos in positions:
                continue
            if (boundsCheck(pos[1], pos[0], input) and
                    input[pos[0]][pos[1]] == curr_symbol):
                frontier.append(pos)
                continue
            fence_count += 1
        symbol_count += 1
        positions.add((curr_row, curr_column))
    print(f'Symbol: {curr_symbol}, Fence: {fence_count}, Cost: {fence_count * symbol_count}')
    return (fence_count * symbol_count, positions)


def puzzleOne():
    input = [line.strip() for line in open("puzzle.txt")]
    visited = set()
    total = 0
    for row in range(len(input)):
        for column in range(len(input[0])):
            if (row, column) in visited:
                continue
            cost, positions = getFenceCost(input, row, column)
            total += cost
            visited.update(positions)
    print(total)


puzzleOne()
