import sys
input = sys.stdin.readline

def bs(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid]==target:
            return True
        elif array[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return False


n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if bs(array, target, 0, n-1):
        print(1)
    else:
        print(0)