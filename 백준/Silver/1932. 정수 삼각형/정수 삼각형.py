# 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
import sys
input = sys.stdin.readline

n = int(input().rstrip())
dp = []
for _ in range(n):
    dp.append(list(map(int, input().rstrip().split())))
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j] + dp[i][j], dp[i-1][j-1] + dp[i][j])

print(max(dp[n-1]))
        