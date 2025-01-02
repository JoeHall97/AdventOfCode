import math
from functools import cache


@cache
def getNumStones(stone: int, curr_depth: int) -> int:
    if curr_depth == 75:
        return 1
    if stone == 0:
        return getNumStones(1, curr_depth + 1)
    elif int(math.log10(stone) + 1) % 2 == 0:
        div_pow = pow(10, (int(math.log10(stone) + 1) // 2))
        s = stone // div_pow
        left = getNumStones(s, curr_depth + 1)
        return left + getNumStones(stone - (s * div_pow), curr_depth + 1)
    else:
        return getNumStones(stone * 2024, curr_depth + 1)


def puzzleTwo():
    input = list(map(int, open('puzzle.txt').readline().split()))
    total_len = 0
    for i in input:
        total_len += getNumStones(i, 0)
    print(total_len)


def puzzleOne():
    input = list(map(int, open('puzzle.txt').readline().split()))
    for i in range(25):
        idx = 0
        while idx < len(input):
            if input[idx] == 0:
                input[idx] = 1
            elif int(math.log10(input[idx]) + 1) % 2 == 0:
                s = str(input[idx])
                input[idx] = int(s[:len(s)//2])
                input.insert(idx + 1, int(s[len(s)//2:]))
                idx += 1
            else:
                input[idx] *= 2024
            idx += 1
    print(len(input))


puzzleOne()
puzzleTwo()

