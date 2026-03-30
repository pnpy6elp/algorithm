n,m, x,y,K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
k_li = list(map(int, input().split()))

dirs = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]
dice = [0,0,0,0,0,0]
def roll(dice, dr):
    dice_copy = [d for d in dice]
    if dr ==1:
        # 오른쪽으로 굴리기
        dice_copy[0] = dice[3]
        dice_copy[2] = dice[0]
        dice_copy[3] = dice[5]
        dice_copy[5] = dice[2]
    elif dr == 2:
        dice_copy[0] = dice[2]
        dice_copy[2] = dice[5]
        dice_copy[3] = dice[0]
        dice_copy[5] = dice[3]
    elif dr == 3:
        dice_copy[0] = dice[4]
        dice_copy[1] = dice[0]
        dice_copy[4] = dice[5]
        dice_copy[5] = dice[1]
    elif dr == 4:
        dice_copy[0] = dice[1]
        dice_copy[1] = dice[5]
        dice_copy[4] = dice[0]
        dice_copy[5] = dice[4]
    return dice_copy

for k in k_li:
    dx, dy = dirs[k]
    if 0<=(x+dx)<n and 0<=(y+dy)<m:
        x += dx
        y += dy
        dice = roll(dice,k)
        print(dice[0])
        if maps[x][y] == 0:
            # 주사위 바닥면 -> 칸
            maps[x][y] = dice[5]
        else:
            dice[5] = maps[x][y]
            maps[x][y] = 0
    