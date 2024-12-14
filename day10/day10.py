def boundsCheck(x: int, y: int, input: list[list[any]]) -> bool:
    return y >= 0 and y < len(input) and x >= 0 and x < len(input[y])

# depth first search
def trailCount(
        trail: list[list[int]], 
        pos_x: int, 
        pos_y: int 
    ) -> int:
    sum = 0
    visited: set[tuple[int]] = set()
    frontier: list[tuple[int]] = [(pos_x, pos_y)]
    while len(frontier) > 0:
        curr = frontier.pop(0)
        visited.add(curr)
        char = trail[curr[1]][curr[0]]
        if trail[curr[1]][curr[0]] == 9: 
            sum += 1
            continue
        # check up
        if ((curr[0], curr[1] - 1) not in visited and boundsCheck(curr[0], curr[1] - 1, trail)
            and trail[curr[1] - 1][curr[0]] == trail[curr[1]][curr[0]] + 1):
            frontier.append((curr[0], curr[1] - 1))
        # check down
        if ((curr[0], curr[1] + 1) not in visited and boundsCheck(curr[0], curr[1] + 1, trail)
            and trail[curr[1] + 1][curr[0]] == trail[curr[1]][curr[0]] + 1):
            frontier.append((curr[0], curr[1] + 1))
        # check left
        if ((curr[0] - 1, curr[1]) not in visited and boundsCheck(curr[0] - 1, curr[1], trail)
            and trail[curr[1]][curr[0] - 1] == trail[curr[1]][curr[0]] + 1):
            frontier.append((curr[0] - 1, curr[1]))
        # check right
        if ((curr[0] + 1, curr[1]) not in visited and boundsCheck(curr[0] + 1, curr[1], trail)
            and trail[curr[1]][curr[0] + 1] == trail[curr[1]][curr[0]] + 1):
            frontier.append((curr[0] + 1, curr[1]))
    return sum


def puzzleOne():
    input = [list(map(int, list(l.strip()))) for l in open('test_input.txt')]
    sum = trailCount(input, 2, 0)
    print(input)
    print(sum)


puzzleOne()