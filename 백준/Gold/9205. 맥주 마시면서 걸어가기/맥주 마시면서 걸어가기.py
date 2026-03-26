import sys
from collections import deque
input = sys.stdin.readline
t = int(input().strip())

def cal_dist(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

for _ in range(t):
    n = int(input().strip())
    home = tuple(map(int, input().split()))
    conv_loc = [tuple(map(int, input().split())) for i in range(n)]
    fest = tuple(map(int, input().split()))
    
    q = deque([home])
    visited_conv = [False] * n
    is_happy = False
    
    while q:
        x, y = q.popleft()
        if cal_dist((x,y),fest)<=1000:
            print("happy")
            is_happy = True
            break
        
        for i in range(n):
            if not visited_conv[i] and cal_dist((x,y), conv_loc[i]) <= 1000:
                visited_conv[i] = True
                q.append(conv_loc[i])
                
    if not is_happy:
        print("sad")
            
        
    
    