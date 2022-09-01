import sys
input = sys.stdin.readline

#소수 판별
def prime_check(num):
    if num==1: return False
    for i in range(2, int(num**(0.5)+1)):
        if num%i==0:
            return False
    return True

#입력
m = int(input())
n = int(input())

nums = []
for i in range(m, n+1):
    if prime_check(i):
        nums.append(i)

#출력
if nums:
    print(sum(nums))
    print(nums[0])
else:
    print(-1)
