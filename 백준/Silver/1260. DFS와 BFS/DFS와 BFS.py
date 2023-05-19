from collections import deque
import sys

read = sys.stdin.readline

n,m,v = map(int,read().split())
graph = [[False] * (n + 1) for _ in range(n + 1)] # index 1부터 시작하려고
for i in range(m):
    a, b = map(int, read().split())
    graph[a][b] = True
    graph[b][a] = True # 친구 네트워크 처럼 서로의 노드에서 True가 되도록
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)
def bfs(v):
    q = deque([v]) # root 노드부터 넣기
    visited1[v] = True # root 노드 방문함
    while q: # q가 빌 때까지 보는 거
        v = q.popleft()
        print(v, end=" ")
        for i in range(1,n+1):
            if not visited1[i] and graph[v][i]: # 방문 목록에 없고, 이웃일 경우
                q.append(i) # i 값 추가
                visited1[i] = True # 방문 표시

def dfs(v):
    visited2[v] = True # root 노드 방문함
    print(v, end=" ") # 방문한 정점 순서임...!
    for i in range(1,n+1):
        if not visited2[i] and graph[v][i]:
            dfs(i)
dfs(v)
print()
bfs(v)

                
                
                