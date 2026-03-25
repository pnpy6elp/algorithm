import sys
input = sys.stdin.readline
n = int(input().strip())
a, b = map(int,input().split())
m = int(input().strip())
# 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다
# 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
# a와 b 사이의 거리

from collections import deque
visited = [False] * (n+1)
INT_MAX = sys.maxsize
dist = [INT_MAX] * (n+1)
q = deque([a])
visited[a] = True
dist[a] = 0
while q:
    node = q.popleft()
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            q.append(i)
            dist[i] = dist[node] + 1
            
chon = dist[b]
if chon != INT_MAX:
    print(chon)
else:
    print(-1)
            