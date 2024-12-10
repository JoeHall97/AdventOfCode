def getAllSums(idx: int, factors: list[int], curr_sum: int, sums: list[int]):
    if idx+1 == len(factors):
        sums.append(curr_sum)
        return
    getAllSums(idx+1, factors, curr_sum+factors[idx+1], sums)
    getAllSums(idx+1, factors, curr_sum*factors[idx+1], sums)
    

def puzzleOne():
    final_total = 0
    for l in open('puzzle_input.txt'):
        numbers = l.split(' ')
        total = int(numbers[0][:len(numbers[0])-1])
        factors = list(map(int, numbers[1:]))
        sums = []
        getAllSums(0, factors, factors[0], sums)
        if total in sums:
            final_total += total
    print(final_total)


def getAllSums2(idx: int, factors: list[int], curr_sum: int, sums: list[int]):
    if idx+1 == len(factors):
        sums.append(curr_sum)
        return
    getAllSums2(idx+1, factors, curr_sum+factors[idx+1], sums)
    getAllSums2(idx+1, factors, curr_sum*factors[idx+1], sums)
    getAllSums2(idx+1, factors, int(f'{curr_sum}{factors[idx+1]}'), sums)
    

def puzzleTwo():
    final_total = 0
    for l in open('puzzle_input.txt'):
        numbers = l.split(' ')
        total = int(numbers[0][:len(numbers[0])-1])
        factors = list(map(int, numbers[1:]))
        sums = []
        getAllSums2(0, factors, factors[0], sums)
        if total in sums:
            final_total += total
    print(final_total)


puzzleOne()
puzzleTwo()