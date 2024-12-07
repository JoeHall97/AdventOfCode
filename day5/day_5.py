def isValid(order_map: dict[int, list[int]], line: list[int]) -> bool:
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if line[j] in order_map and line[i] in order_map[line[j]]:
                return False
    return True


def sortLine(line: list[int], order_map: dict[int, list[int]]) -> list[int]:
    sorted = []
    for item in line:
        inserted = False
        for idx, sorted_item in enumerate(sorted):
            if item in order_map and sorted_item in order_map[item]:
                sorted.insert(idx, item)
                inserted = True
                break
        if not inserted:
            sorted.append(item) 
    return sorted


def puzzleTwo():
    order_map: dict[int, list[int]] = {}
    parsing_order = True
    sum = 0
    for line in open('puzzle_input.txt'):
        if parsing_order and '|' not in line:
            parsing_order = False
            continue
        if parsing_order:
            pair = list(map(int, line.split('|')))
            if pair[0] not in order_map:
                order_map[pair[0]] = [pair[1]]
            else:
                order_map[pair[0]].append(pair[1])
            continue
        line_list = list(map(int, line.strip().split(',')))
        if isValid(order_map, line_list):
            continue
        sorted_list = sortLine(line_list, order_map)
        sum += sorted_list[int(len(sorted_list)/2)]
    print(sum)


def puzzleOne():
    order_map: dict[int, list[int]] = {}
    parsing_order = True
    sum = 0
    for line in open('puzzle_input.txt'):
        if parsing_order and '|' not in line:
            parsing_order = False
            continue
        if parsing_order:
            pair = list(map(int, line.split('|')))
            if pair[0] not in order_map:
                order_map[pair[0]] = [pair[1]]
            else:
                order_map[pair[0]].append(pair[1])
            continue
        line_list = list(map(int, line.strip().split(',')))
        if isValid(order_map, line_list):
            sum += line_list[int(len(line_list)/2)]
    print(sum)


# puzzleOne()
puzzleTwo()
