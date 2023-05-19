import sys
input = sys.stdin.readline

n = int(input().rstrip())
l = []
for _ in range(n):
    start, end = map(int, input().split())
    l.append([start,end])
l.sort(key=lambda x:(x[1],x[0])) # 회의 끝나는 시간으로 먼저 정렬 !!!! 그다음 회의시작시간
# 최대한 회의를 많이 해야함
cnt = 1
end_time = l[0][1]
for i in range(1,n):
    if l[i][0] >= end_time:
        cnt += 1
        end_time = l[i][1]
print(cnt)



