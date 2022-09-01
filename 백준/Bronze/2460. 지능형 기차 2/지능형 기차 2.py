import sys
input = sys.stdin.readline

counts = []
for i in range(10):
    a, b = map(int, input().split())
    counts.append(b-a)

rider = 0 #탑승 인원
max_cnt = 0 #최대 인원
for cnt in counts:
    rider += cnt
    max_cnt = max(max_cnt, rider)
print(max_cnt)