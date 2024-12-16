import re

def boundsCheck(x, y, con):
    return y >= 0 and y < len(con) and x >= 0 and x < len(con[y])


def puzzleTwo():
    input = []
    r = re.compile(r'\d|\w')
    # read in the input and grab the location of each station,
    # grouping them by their frequency
    stations: dict[int, list[tuple[int]]] = {}
    for idx, l in enumerate(open('puzzle.txt')):
        for m in r.finditer(l):
            station = l[m.start():m.end()]
            if station not in stations:
                stations[station] = [(m.start(), idx)]
            else:
                stations[station].append((m.start(), idx))
        input.append(l.strip())
    # loop through the sets of stations with the same frequency,
    # adding in the antinodes to the set if they are in bounds and
    # haven't already been added
    unique_antinodes: set[tuple[int]] = set()
    for s_positions in stations.values():
        if len(s_positions) < 2:
            continue
        for idx, i in enumerate(s_positions):
            for j in s_positions[idx+1:]:
                distance_x, distance_y = abs(i[0]-j[0]), abs(i[1]-j[1])
                i_offset_x, i_offset_y = 0, 0
                j_offset_x, j_offset_y = 0, 0

                if i[0] > j[0]:
                    i_offset_x = distance_x
                    j_offset_x = -distance_x
                else:
                    i_offset_x = -distance_x
                    j_offset_x = distance_x
                if i[1] > j[1]:
                    i_offset_y = distance_y
                    j_offset_y = -distance_y
                else:
                    i_offset_y = -distance_y
                    j_offset_y = distance_y
                anti_i = [i[0] + i_offset_x, i[1] + i_offset_y]
                anti_j = [j[0] + j_offset_x, j[1] + j_offset_y]

                while boundsCheck(anti_i[0], anti_i[1], input):
                    unique_antinodes.add((anti_i[0], anti_i[1]))
                    anti_i[0] += i_offset_x
                    anti_i[1] += i_offset_y
                while boundsCheck(anti_j[0], anti_j[1], input):
                    unique_antinodes.add((anti_j[0], anti_j[1]))
                    anti_j[0] += j_offset_x
                    anti_j[1] += j_offset_y
                unique_antinodes.add(i)
                unique_antinodes.add(j)
    print(len(unique_antinodes))


def puzzleOne():
    input = []
    r = re.compile(r'\d|\w')
    # read in the input and grab the location of each station,
    # grouping them by their frequency
    stations: dict[int, list[tuple[int]]] = {}
    for idx, l in enumerate(open('puzzle.txt')):
        for m in r.finditer(l):
            station = l[m.start():m.end()]
            if station not in stations:
                stations[station] = [(m.start(), idx)]
            else:
                stations[station].append((m.start(), idx))
        input.append(l.strip())
    # loop through the sets of stations with the same frequency,
    # adding in the antinodes to the set if they are in bounds and
    # haven't already been added
    unique_antinodes: set[tuple[int]] = set()
    for s_positions in stations.values():
        if len(s_positions) < 2:
            continue
        for idx, i in enumerate(s_positions):
            for j in s_positions[idx+1:]:
                distance_x, distance_y = abs(i[0]-j[0]), abs(i[1]-j[1])
                anti_i_x, anti_i_y = 0, 0
                anti_j_x, anti_j_y = 0, 0

                if i[0] > j[0]:
                    anti_i_x = i[0] + distance_x
                    anti_j_x = j[0] - distance_x
                else:
                    anti_i_x = i[0] - distance_x
                    anti_j_x = j[0] + distance_x
                if i[1] > j[1]:
                    anti_i_y = i[1] + distance_y
                    anti_j_y = j[1] - distance_y
                else:
                    anti_i_y = i[1] - distance_y
                    anti_j_y = j[1] + distance_y

                if boundsCheck(anti_i_x, anti_i_y, input):
                    unique_antinodes.add((anti_i_x, anti_i_y))
                if boundsCheck(anti_j_x, anti_j_y, input):
                    unique_antinodes.add((anti_j_x, anti_j_y))
    print(len(unique_antinodes))


puzzleOne()
puzzleTwo()