import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    result = list(bin(n)[2:])
    result.reverse()

    for i in range(len(result)):
        if result[i]=='1':
            print(i, end=' ')
    print()