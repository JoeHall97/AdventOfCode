# is there no way to type annotate a lambda functions?
def compareLine(line: list[int], validLineFunc) -> bool:
    for i in range(len(line)-1):
        if not validLineFunc(line[i], line[i+1]):
            return False
    return True 


def compareLineTwo(line: list[int]):
    d = [x - y for x, y in zip(line, line[1:])]
    return all(1 <= x <= 3 for x in d) or all(-1 >= x >= -3 for x in d)


def puzzle_one():
    sum = 0
    for line in open('puzzle.txt'):
        l = list(map(int, line.split(' ')))
        if l[0] > l[1]:
            res = compareLine(l, lambda x, y: abs(x-y) <= 3 and x > y)
        else:
            res = compareLine(l, lambda x, y: abs(x-y) <= 3 and x < y)
        if res:
            sum += 1
    print(sum)


def puzzle_two():
    # ended up getting this solution from this yt video:
    # https://www.youtube.com/watch?v=DJhicnmb0ZA
    # pretty simple way to solve the problem.
    sum = 0
    for line in open('puzzle.txt'):
        l = list(map(int, line.split(' ')))
        if any(compareLineTwo(l[:n] + l[n+1:]) for n in range(len(l))):
            sum += 1
    print(sum)


puzzle_one()
puzzle_two()