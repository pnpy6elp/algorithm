n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [0,1,0,-1], [1,0,-1,0]

visited = [[False]*m for _ in range(n)]
max_val = 0
def dfs(x, y, depth, total):
    global max_val
    
    if depth==4:
        max_val = max(max_val, total)
        return
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            # ㅜ모양
            if depth == 2:
                visited[nx][ny] = True
                dfs(x,y,depth+1,total+graph[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx,ny,depth+1,total+graph[nx][ny])
            visited[nx][ny]=False
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,1,graph[i][j])
        visited[i][j] = False
print(max_val)
        