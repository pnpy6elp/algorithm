import sys
from collections import deque
read = sys.stdin.readline
n = int(read()) # 총 컴퓨터의 수 (노드)
m = int(read()) # 간선의 수
# root는 1부터
mat = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    a, b = map(int,read().split())
    mat[a].append(b)
    mat[b].append(a)
q = deque([1])
visited[1] = 1
while q:
    v = q.popleft()
    #print(v)
    for i in range(len(mat[v])):
        if visited[mat[v][i]] == 0:
            q.append(mat[v][i])
            visited[mat[v][i]] = 1
print(sum(visited) - 1)
