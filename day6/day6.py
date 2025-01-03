import re

# (x, y) offsets to move in a direction
move_directions: dict[str, tuple[int]] = { 
    'up': (0, -1),
    'down': (0, 1),
    'left': (-1, 0),
    'right': (1, 0)
}


def boundsCheck(x: int, y: int, l: list[list[int]]) -> bool:
    return x >= 0 and x < len(l[0]) and y >= 0 and y < len(l)


# adds an obstruction to a map and checks if it causes a loop
def causesLoop(pos: list[int], start: list[int], direction: str, checkMap: list[str]) -> bool:
    # add obstruction to the map
    m = checkMap.copy()
    curr_pos = start.copy()
    m[pos[1]] = m[pos[1]][:pos[0]] + '#' + m[pos[1]][pos[0]+1:]
    visited_obstructions:dict[str,list[tuple[int]]] = {
        'up': [],
        'down': [],
        'left': [],
        'right': []
    }
    while True:
        x_offset, y_offset = move_directions[direction]
        if not boundsCheck(curr_pos[0] + x_offset, curr_pos[1] + y_offset, m):
            return False
        if m[curr_pos[1]+y_offset][curr_pos[0]+x_offset] == '#':
            if (curr_pos[0], curr_pos[1]) in visited_obstructions[direction]:
                return True
            visited_obstructions[direction].append((curr_pos[0], curr_pos[1]))
            if direction == 'up':
                direction = 'right'
            elif direction == 'right':
                direction = 'down'
            elif direction == 'down':
                direction = 'left'
            else:
                direction = 'up'
            continue
        curr_pos[0] += x_offset
        curr_pos[1] += y_offset


def puzzleTwo():
    r = re.compile(r'\^|\>|\<|v')
    input = []
    # x, y
    pos: list[int] = [-1, -1]
    direction = ''
    for y, line in enumerate(open('puzzle.txt')):
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
    start_pos = pos.copy()
    start_direction = direction
    # get all positions the guard visits on his route, excluding the start position 
    visited: set[tuple[int]] = set()
    while True:
        x_offset, y_offset = move_directions[direction]
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
        if (pos[0], pos[1]) not in visited:
            visited.add((pos[0], pos[1]))
    visited.add((pos[0], pos[1]))
    # add an obstruction to each position the guard visits and check if it creates
    # a loop
    count = 0
    for v in visited:
        if causesLoop(v, start_pos, start_direction, input):
            count += 1
    print(count)


def puzzleOne():
    r = re.compile(r'\^|\>|\<|v')
    input = []
    # x, y
    pos: list[int] = [-1, -1]
    direction = ''
    for y, line in enumerate(open('puzzle.txt')):
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
        
        x_offset, y_offset = move_directions[direction]
        
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
puzzleTwo()