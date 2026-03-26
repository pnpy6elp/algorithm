n = int(input())
k = int(input())

from collections import deque

graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1 # 사과
    
l = int(input())
snake = []
dxs, dys = [0,1,0,-1], [1,0,-1,0]
for _ in range(l):
    x, c = input().split()
    snake.append((int(x), c))

# 시작점은 0,0
# 처음에는 y + 1 방향
q = deque([(1, 1)]) # 머리
graph[1][1] = 2 # 뱀의 몸통 -> 2

# for simulation
time = 0 # process
d = 0 # direction, 우측
turn_idx = 0
x, y = 1, 1 # current_points

while True:
    time += 1
    nx = x + dxs[d]
    ny = y + dys[d]
    
    if nx < 1 or nx > n or ny < 1 or ny > n or graph[nx][ny]==2:
        # 벽에 부딪 or 자기자신과 박치기
        print(time)
        break
    if graph[nx][ny] == 1:
        graph[nx][ny] = 2
        q.append((nx,ny))
    elif graph[nx][ny] == 0:
        tx, ty = q.popleft() # tail
        graph[tx][ty] = 0 # 꼬리자르기
        graph[nx][ny] = 2
        q.append((nx, ny))
        
    x, y = nx, ny
    
    if turn_idx < l and time == snake[turn_idx][0]:
        turn_dir = snake[turn_idx][1]
        if turn_dir == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4
        turn_idx += 1
        
