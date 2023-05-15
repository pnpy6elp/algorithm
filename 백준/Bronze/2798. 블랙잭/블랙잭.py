import sys
N, M = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
cards.sort()
# M에 가까운 카드 3장의 합
answer = 0
for i in range(N):
    for j in range(i+1, N): 
        for k in range(j+1,N):
            tmp = cards[i] + cards[j] + cards[k]
            if(tmp>M):
                continue
            else:
                answer = max(answer, tmp)
print(answer)
                
            
        