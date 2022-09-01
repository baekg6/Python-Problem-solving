from itertools import combinations
import sys
input = sys.stdin.readline

#입력
dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
dwarfs.sort()

#출력
combs = combinations(dwarfs, 7)
for comb in combs:
    if sum(comb)==100:
        result = list(comb)
        for dwarf in result:
            print(dwarf)
        break