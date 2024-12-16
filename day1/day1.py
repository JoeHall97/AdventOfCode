import bisect

def puzzle_one():
    left_list, right_list = [], []
    for line in open('puzzle.txt'):
        l, r = line.split()
        bisect.insort(left_list, int(l))
        bisect.insort(right_list, int(r))
    print(sum(abs(l - r) for l, r in zip(left_list, right_list)))


def puzzle_two():
    left_list, right_list = [], []
    for line in open('puzzle.txt'):
        l, r = line.split()
        left_list.append(int(l))
        right_list.append(int(r))

    right_dict = {}
    for i in set(right_list):
        right_dict[i] = right_list.count(i)
    
    sum_duplicates = 0
    for l in left_list:
        if right_dict.get(l):
            sum_duplicates += l * right_dict[l]
    print(sum_duplicates)


puzzle_one()
puzzle_two()