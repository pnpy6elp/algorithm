from collections import deque

# 1. 입력 처리: 공백 없이 들어오는 문자열을 한 글자씩 쪼개서 정수로 변환 후 deque로 만듦
gears = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    num, dr = map(int, input().split())
    num -= 1  # 톱니바퀴 번호 1~4를 인덱스 0~3으로
    
    dirs = [0] * 4
    dirs[num] = dr
    
    # 톱니바퀴 기준 왼쪽
    for i in range(num, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            dirs[i-1] = -dirs[i] 
        else:
            break 
    # 톱니바퀴 기준 오른쪽      
    for i in range(num, 3):
        if gears[i][2] != gears[i+1][6]:
            dirs[i+1] = -dirs[i]
        else:
            break
            
    for i in range(4):
        if dirs[i] != 0:
            gears[i].rotate(dirs[i])

ans = 0
ans += 1 if gears[0][0] == 1 else 0
ans += 2 if gears[1][0] == 1 else 0
ans += 4 if gears[2][0] == 1 else 0
ans += 8 if gears[3][0] == 1 else 0

print(ans)