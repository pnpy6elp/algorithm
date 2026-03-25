import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
dist = [-1] * 100001
def bfs(x, k):
    if x == k:
        print(0)
        return
    queue = deque()
    dist[x] = 0
    queue.append(x)
    while queue:
        x = queue.popleft()
        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx < 100001:
                if dist[nx] == -1:
                    dist[nx] = dist[x] + 1
                    queue.append(nx)
                    if nx == K:
                        print(dist[nx])
                        return
                
            
bfs(N, K)
    