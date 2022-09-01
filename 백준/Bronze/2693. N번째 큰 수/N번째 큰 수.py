import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):

    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    print(nums[2])
