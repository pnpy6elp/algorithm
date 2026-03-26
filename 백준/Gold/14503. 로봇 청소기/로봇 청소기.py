import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split()) # (r,c), direction
graph = [list(map(int, input().split())) for _ in range(n)]

# 북(0), 동(1), 남(2), 서(3) 순서에 맞춘 이동 변화량 (move 함수를 대체)
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]

# 청소기 시작 위치 방문(청소) 처리
visited[r][c] = 1
ans = 1

while True:
    is_cleaned_around = False  # 주변 4칸 중 청소할 곳이 있는지 체크하는 깃발
    
    # 반시계 방향으로 최대 4번 회전하며 확인
    for _ in range(4):
        # 1. 반시계 방향으로 90도 회전
        d = (d + 3) % 4  # 작성하셨던 rot_dc = [3,0,1,2] 와 완벽히 동일한 수식입니다!
        
        nx = r + dxs[d]
        ny = c + dys[d]
        
        # 2. 바라보는 방향의 앞쪽 칸이 청소되지 않은 빈 칸인지 확인
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                # 청소하고 한 칸 전진
                visited[nx][ny] = 1
                ans += 1
                r, c = nx, ny
                is_cleaned_around = True
                break # 전진했으니 회전 멈추고 처음(1번) 규칙으로 돌아감
                
    # 3. 4방향 모두 청소할 곳이 없었던 경우
    if not is_cleaned_around:
        # 후진할 방향 (현재 방향의 반대)
        back_d = (d + 2) % 4 # 작성하셨던 back = [2,3,0,1] 과 동일합니다!
        nx = r + dxs[back_d]
        ny = c + dys[back_d]
        
        # 후진할 수 있으면 후진 (방향 d는 유지됨에 주의!)
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            r, c = nx, ny
        else:
            # 뒤가 벽(1)이라 후진할 수 없으면 작동 멈춤
            break

print(ans)

