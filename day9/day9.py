# helper function for the second puzzle
def printDebugString(input: list[list[int]]):
    out = ''
    for i in input:
        if i[1] == 0:
            continue
        for x in range(i[1]):
            if i[0] != -1:
                out += str(i[0])
            else:
                out += '.'
    print(out)


# helper function for the second puzzle
def printFileCheckSum(res: list[list[int]]):
    file = []
    checksum = 0
    idx = 0
    for r in res:
        for x in range(r[1]):
            if r[0] != -1:
                checksum += r[0] * idx
            idx += 1
    print(checksum)


def puzzleTwo():
    res = [] 
    id = 0
    for idx, i in enumerate(list(open('puzzle_input.txt').readline().strip())):
        if idx % 2 == 0:
            res.append([id, int(i)])
            id += 1
        else:
            res.append([-1, int(i)])
    # printDebugString(res)
    idx = len(res) - 1
    while idx > 0:
        if res[idx][0] == -1:
            idx -= 1
            continue
        forward = 0
        while forward < idx:
            if res[forward][0] == -1 and res[forward][1] >= res[idx][1]:
                res[forward][1] -= res[idx][1]
                res.insert(forward, res[idx].copy())
                res[idx+1][0] = -1
                break
            forward += 1
        idx -= 1
    # printDebugString(res)
    printFileCheckSum(res)



def puzzleOne():
    input = list(map(int, list(open('puzzle.txt').readline().strip())))
    res = [] 
    id = 0
    for idx, i in enumerate(input):
        if idx % 2 == 0:
            res += [id for x in range(i)]
            id += 1
        else:
            res += [-1 for x in range(i)]
    forward = 0
    back = len(res) - 1
    while forward < back:
        if res[forward] != -1:
            forward += 1
            continue
        if res[back] == -1:
            back -= 1
            continue
        res[forward] = res[back]
        res[back] = -1
        back -= 1
        forward += 1
    print(sum([idx * r for idx, r in enumerate(res[:back+1])]))


puzzleOne()
puzzleTwo()