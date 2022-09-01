import sys
input = sys.stdin.readline

def prime_check(num):
    if num==1: return False
    for i in range(2, int(num**(0.5)+1)):
        if num%i==0:
            return False
    return True


n = int(input())
nums = list(map(int, input().split()))

result = 0
for num in nums:
    if prime_check(num):
        result +=1

print(result)