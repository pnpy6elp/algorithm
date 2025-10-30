import sys
# 입력 속도 최적화
input = sys.stdin.readline
n = int(input().rstrip())

# n=0일 때를 먼저 처리
if n == 0:
    print(0)
    sys.exit()

# arr 배열을 1부터 n까지 사용 (arr[0] = 0)
arr = [0] + [int(input().rstrip()) for _ in range(n)]
dp = [0] * (n + 1)

# 1. n=1일 때
dp[1] = arr[1]
if n == 1:
    print(dp[1])
    sys.exit() # ❗️ n=1이면 여기서 종료!

# 2. n=2일 때
# 이 코드는 n >= 2일 때만 실행됨 (위에서 n=1이 걸러졌으므로)
dp[2] = arr[1] + arr[2] 
if n == 2:
    print(dp[2])
    sys.exit() # ❗️ n=2이면 여기서 종료!

# 3. n >= 3일 때만 일반 DP 루프 실행
# 이전 대화에서 확인했듯이, 계단 문제의 점화식이 불완전하므로 이 부분도 수정해야 합니다.
for i in range(3, n + 1):
    # 계단 오르기 문제의 정확한 점화식:
    dp[i] = arr[i] + max(
        dp[i - 2],              # Case 1: i-2에서 두 칸 점프
        dp[i - 3] + arr[i - 1]  # Case 2: i-3 -> i-1 -> i (i-2를 건너뜀)
    )

print(dp[n]) # dp[-1] 대신 dp[n]을 사용합니다.