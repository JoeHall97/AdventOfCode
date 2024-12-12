def puzzleTwo():
    res = [] 
    id = 0
    for idx, i in enumerate(list(open('test_input.txt').readline().strip())):
        if idx % 2 == 0:
            res.append([id, int(i)])
            id += 1
        else:
            res.append([-1, int(i)])
    print(res)
    idx = len(res) - 1
    while idx > 0:
        if res[idx][0] == -1:
            idx -= 1
            continue
        forward = 0
        while forward < idx:
            if res[forward][0] == -1 and res[forward][1] == res[idx][1]:
                res[forward][0] = res[idx][0]
                res[idx][0] = -1
                res[idx][1] = 0
                break
            forward += 1
        idx -= 1
    print(res)



def puzzleOne():
    input = list(map(int, list(open('test_input.txt').readline().strip())))
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
    print(res[:back+1])
    print(sum([idx * r for idx, r in enumerate(res[:back+1])]))


# puzzleOne()
puzzleTwo()