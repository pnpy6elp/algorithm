import sys
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())

from collections import deque
dist = [-1] * (f+1)
visited = [False] * (f+1)
if s==g:
    print(0)
    exit()
q = deque([s])
dist[s] = 0

def in_range(x):
    return x>=1 and x<=f
def can_go(x):
    return (in_range(x) and dist[x]==-1)
while q:
    x = q.popleft()
    
    for dx in [x+u, x-d]:
        if can_go(dx):
            dist[dx] = dist[x] + 1
            q.append(dx)
            if dx == g:
                print(dist[dx])
                exit()
if dist[g]==-1:
    print("use the stairs")