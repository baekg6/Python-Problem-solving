import sys
input = sys.stdin.readline

n, k = map(int, input().split())

divisors = []
for i in range(1, n+1):
    if n%i==0:
        divisors.append(i)


if k <= len(divisors):
    print(divisors[k-1])
else:
    print(0)    