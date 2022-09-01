import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    if a%b==0:
        return b
    return gcd(b, a%b)

def lcm(a, b):
    return a*b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))