import sys
input = sys.stdin.readline

a, b = map(int, input().split())

nums = []
i=1
while len(nums)<b:
    for _ in range(i):
        nums.append(i)
    i+=1

print(sum(nums[a-1:b]))