from collections import deque
import sys
input = sys.stdin.readline

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    
    result.reverse()
    for i in result:
        print(i, end=' ')
    print()

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1);
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
    indegree[a]+=1

topology_sort()
