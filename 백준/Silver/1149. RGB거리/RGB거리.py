import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = [[0,0,0]]
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))
    
dp = [[0] * 3 for _ in range(N+1)] # 색깔 인덱스, 비용?
dp[1] = arr[1]

for i in range(2, N+1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0] # 삘간색 0
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1] # 초록색 1
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2] # 파란색 2
print(min(dp[N]))
