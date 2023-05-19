import sys

input = sys.stdin.readline
k,n = map(int, input().split()) # 한도, 인덱스 개수
subjects = [list(map(int, input().split())) for _ in range(n)] # 중요도, 시간 순
subjects.sort(key=lambda x:(x[1],x[0])) # 시간순으로 정렬
K = [[0]*(k+1) for _ in range(n+1)] # 배낭
for i in range(n+1):
    for j in range(k+1):
        if(i==0 or j==0):
            K[i][j] = 0
        elif(subjects[i-1][1]<=j):
            K[i][j] = max(K[i-1][j], subjects[i-1][0] + K[i-1][j-subjects[i-1][1]])
        else:
            K[i][j] = K[i-1][j]

print(K[n][k])