# 1253

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split(' ')))
data.sort()

result = 0
for i in range(n):
    target = data[i]
    s = 0
    e = n-1
    while s < e:
        if data[s]+data[e] == target:
            if s != i and e != i:
                result += 1
                break
            elif s == i:
                s += 1
            elif e == i:
                e -= 1
        elif data[s]+data[e] < target:
            s += 1
        else:
            e -= 1

print(result)
