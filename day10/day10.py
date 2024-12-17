def boundsCheck(x: int, y: int, input: list[list[any]]) -> bool:
    return y >= 0 and y < len(input) and x >= 0 and x < len(input[y])


# depth first search for unqiue trails
def trailCount2(
        trail: list[list[int]],
        pos_x: int,
        pos_y: int) -> int:
    sum = 0
    visited: set[tuple[int]] = set()
    frontier: list[tuple[int]] = [(pos_x, pos_y)]
    while len(frontier) > 0:
        curr_pos = frontier.pop(0)
        visited.add(curr_pos)
        curr_height = trail[curr_pos[1]][curr_pos[0]]
        if curr_height == 9:
            sum += 1
            continue
        # check up
        if ((curr_pos[0], curr_pos[1] - 1) not in visited 
                and boundsCheck(curr_pos[0], curr_pos[1] - 1, trail)
                and trail[curr_pos[1] - 1][curr_pos[0]] == curr_height + 1):
            frontier.append((curr_pos[0], curr_pos[1] - 1))
        # check down
        if ((curr_pos[0], curr_pos[1] + 1) not in visited 
                and boundsCheck(curr_pos[0], curr_pos[1] + 1, trail)
                and trail[curr_pos[1] + 1][curr_pos[0]] == curr_height + 1):
            frontier.append((curr_pos[0], curr_pos[1] + 1))
        # check left
        if ((curr_pos[0] - 1, curr_pos[1]) not in visited 
                and boundsCheck(curr_pos[0] - 1, curr_pos[1], trail)
                and trail[curr_pos[1]][curr_pos[0] - 1] == curr_height + 1):
            frontier.append((curr_pos[0] - 1, curr_pos[1]))
        # check right
        if ((curr_pos[0] + 1, curr_pos[1]) not in visited
                and boundsCheck(curr_pos[0] + 1, curr_pos[1], trail)
                and trail[curr_pos[1]][curr_pos[0] + 1] == curr_height + 1):
            frontier.append((curr_pos[0] + 1, curr_pos[1]))
    return sum


# depth first search for unqiue trail heads
def trailCount(
        trail: list[list[int]],
        pos_x: int,
        pos_y: int) -> int:
    sum = 0
    visited: set[tuple[int]] = set()
    frontier: list[tuple[int]] = [(pos_x, pos_y)]
    while len(frontier) > 0:
        curr_pos = frontier.pop(0)
        curr_height = trail[curr_pos[1]][curr_pos[0]]
        if curr_height == 9 and curr_pos not in visited:
            visited.add(curr_pos)
            sum += 1
            continue
        visited.add(curr_pos)
        # check up
        if ((curr_pos[0], curr_pos[1] - 1) not in visited 
                and boundsCheck(curr_pos[0], curr_pos[1] - 1, trail)
                and trail[curr_pos[1] - 1][curr_pos[0]] == curr_height + 1):
            frontier.append((curr_pos[0], curr_pos[1] - 1))
        # check down
        if ((curr_pos[0], curr_pos[1] + 1) not in visited 
                and boundsCheck(curr_pos[0], curr_pos[1] + 1, trail)
                and trail[curr_pos[1] + 1][curr_pos[0]] == curr_height + 1):
            frontier.append((curr_pos[0], curr_pos[1] + 1))
        # check left
        if ((curr_pos[0] - 1, curr_pos[1]) not in visited 
                and boundsCheck(curr_pos[0] - 1, curr_pos[1], trail)
                and trail[curr_pos[1]][curr_pos[0] - 1] == curr_height + 1):
            frontier.append((curr_pos[0] - 1, curr_pos[1]))
        # check right
        if ((curr_pos[0] + 1, curr_pos[1]) not in visited
                and boundsCheck(curr_pos[0] + 1, curr_pos[1], trail)
                and trail[curr_pos[1]][curr_pos[0] + 1] == curr_height + 1):
            frontier.append((curr_pos[0] + 1, curr_pos[1]))
    return sum


def puzzleOne():
    sum = 0
    input = [list(map(int, list(l.strip()))) for l in open('puzzle.txt')]
    for i, row in enumerate(input):
        for j, column in enumerate(row):
            if column == 0:
                sum += trailCount(input, j, i)
    print(sum)


def puzzleTwo():
    sum = 0
    input = [list(map(int, list(l.strip()))) for l in open('puzzle.txt')]
    for i, row in enumerate(input):
        for j, column in enumerate(row):
            if column == 0:
                sum += trailCount2(input, j, i)
    print(sum)


puzzleOne()
puzzleTwo()
