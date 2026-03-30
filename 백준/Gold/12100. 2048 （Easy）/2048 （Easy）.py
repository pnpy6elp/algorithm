n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def move_board(current_board, dir):
    new_board = [[0] * n for _ in range(n)]
    
    if dir == 0: # 위로 밀기 (Up)
        for j in range(n):
            ptr = 0 # 블록이 놓일 자리 (맨 위부터 시작)
            for i in range(n):
                if current_board[i][j] != 0: # 빈칸이 아닌 블록을 발견하면
                    if new_board[ptr][j] == 0:
                        # 놓을 자리가 비어있으면 그냥 놓는다.
                        new_board[ptr][j] = current_board[i][j]
                    elif new_board[ptr][j] == current_board[i][j]:
                        # 놓을 자리에 있는 블록과 숫자가 같으면 2배로 합치고, 다음 자리로 넘어간다.
                        new_board[ptr][j] *= 2
                        ptr += 1
                    else:
                        # 숫자가 다르면, 바로 다음 자리에 블록을 놓는다.
                        ptr += 1
                        new_board[ptr][j] = current_board[i][j]
                        
    elif dir == 1: # 아래로 밀기 (Down)
        for j in range(n):
            ptr = n - 1 # 블록이 놓일 자리 (맨 아래부터 시작)
            for i in range(n - 1, -1, -1):
                if current_board[i][j] != 0:
                    if new_board[ptr][j] == 0:
                        new_board[ptr][j] = current_board[i][j]
                    elif new_board[ptr][j] == current_board[i][j]:
                        new_board[ptr][j] *= 2
                        ptr -= 1
                    else:
                        ptr -= 1
                        new_board[ptr][j] = current_board[i][j]
                        
    elif dir == 2: # 왼쪽으로 밀기 (Left)
        for i in range(n):
            ptr = 0 # 블록이 놓일 자리 (맨 왼쪽부터 시작)
            for j in range(n):
                if current_board[i][j] != 0:
                    if new_board[i][ptr] == 0:
                        new_board[i][ptr] = current_board[i][j]
                    elif new_board[i][ptr] == current_board[i][j]:
                        new_board[i][ptr] *= 2
                        ptr += 1
                    else:
                        ptr += 1
                        new_board[i][ptr] = current_board[i][j]
                        
    elif dir == 3: # 오른쪽으로 밀기 (Right)
        for i in range(n):
            ptr = n - 1 # 블록이 놓일 자리 (맨 오른쪽부터 시작)
            for j in range(n - 1, -1, -1):
                if current_board[i][j] != 0:
                    if new_board[i][ptr] == 0:
                        new_board[i][ptr] = current_board[i][j]
                    elif new_board[i][ptr] == current_board[i][j]:
                        new_board[i][ptr] *= 2
                        ptr -= 1
                    else:
                        ptr -= 1
                        new_board[i][ptr] = current_board[i][j]
                        
    return new_board

def dfs(depth, current_board):
    global ans
    
    # 5번 움직였으면 보드에서 가장 큰 값을 찾아서 정답 갱신 후 종료
    if depth == 5:
        for i in range(n):
            ans = max(ans, max(current_board[i]))
        return

    # 상(0), 하(1), 좌(2), 우(3) 4방향으로 다 밀어보기
    for i in range(4):
        next_board = move_board(current_board, i)
        dfs(depth + 1, next_board)

# 깊이 0, 초기 보드 상태로 탐색 시작
dfs(0, board)
print(ans)