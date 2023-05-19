import sys
input = sys.stdin.readline

t = int(input().rstrip())
for i in range(t):
    n = int(input().rstrip()) # 지원자 수
    l = []
    for j in range(n):
        score = list(map(int, input().split()))
        l.append(score)
    l.sort(key=lambda x:(x[0],x[1]))
    top = 0
    result = 1 # 1등인 사람은 무조건 붙으니까
    for i in range(1, len(l)):
        if l[i][1] < l[top][1]:
            top = i
            result += 1
    print(result)









