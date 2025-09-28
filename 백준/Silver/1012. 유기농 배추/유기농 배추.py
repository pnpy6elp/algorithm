import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())


def dfs(graph,x, y, M, N):
    if x <= -1 or y <= -1 or x >= M or y >= N:
        return False 
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph,x-1,y, M, N)
        dfs(graph,x,y-1, M, N)
        dfs(graph,x+1,y, M, N)
        dfs(graph,x,y+1, M, N)
        return True
    return False

for t in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    result = 0
    graph = [[0] * N for _ in range(M)]
    for k in range(K):
        x, y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1
    for i in range(M):
        for j in range(N):
            if dfs(graph,i, j,M, N) == True:
                result += 1
    print(result)