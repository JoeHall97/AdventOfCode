import re

# (x, y) offsets to move in a direction
move_directions: dict[str, tuple[int]] = { 
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0)
}


def boundsCheck(x: int, y: int, l: list[list[int]]) -> bool:
    return x >= 0 and x < len(l[0]) and \
            y >= 0 and y < len(l)


def puzzleOne():
    r = re.compile(r'\^|\>|\<|v')
    input = []
    # x, y
    pos: list[int] = [-1, -1]
    direction = ''
    for y, line in enumerate(open('puzzle_input.txt')):
        input.append(line.strip())
        search = r.search(line)
        if search:
            pos = [search.start(), y]
            char = line[search.start():search.end()]
            if char == '^':
                direction = 'up'
            elif char == '>':
                direction = 'right'
            elif char == '<':
                direction = 'left'
            else:
                direction = 'down'

    visited: set[tuple[int]] = set()
    while True:
        if (pos[0], pos[1]) not in visited:
            visited.add((pos[0], pos[1]))
        
        x_offset = move_directions[direction][0]
        y_offset = move_directions[direction][1]
        
        if not boundsCheck(pos[0] + x_offset, pos[1] + y_offset, input):
            break

        if input[pos[1]+y_offset][pos[0]+x_offset] == '#':
            if direction == 'up':
                direction = 'right'
            elif direction == 'right':
                direction = 'down'
            elif direction == 'down':
                direction = 'left'
            else:
                direction = 'up'
            continue

        pos[0] += x_offset
        pos[1] += y_offset
    print(len(visited))


puzzleOne()