import sys
input = sys.stdin.readline
n, k = map(int, input().split())
subjects = [list(map(int,input().split())) for _ in range(n)]
subjects.sort(key=lambda x:(x[0],x[1]))
K = [[0]*(k+1) for _ in range(n+1)] # 배낭
for i in range(n+1): 
    for j in range(k+1): # 무게
        if i == 0 or j == 0:
            K[i][j] = 0
        elif subjects[i-1][0] <= j:
            K[i][j] = max(K[i-1][j], subjects[i-1][1] + K[i-1][j-subjects[i-1][0]])
        else:
            K[i][j] = K[i-1][j]
print(K[n][k])