import sys
input = sys.stdin.readline

n, k = map(int, input().split())
from collections import deque

dist = [-1] * 100001
if n == k:
    print(0)
    exit()
    
q = deque([n])
dist[n] = 0
# n에서 k까지의 최단 시간
cnt = 0
while q:
    x = q.popleft()
    for nx in [x + 1, x - 1, x * 2]:
        if (nx >= 0 and nx < 100001) and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
            if nx == k:
                print(dist[nx])
                exit()
        