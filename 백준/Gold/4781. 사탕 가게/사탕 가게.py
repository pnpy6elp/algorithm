import sys
input=sys.stdin.readline

while True:

    N,M=map(float,input().split())
    if N==0 and M==0.00:
        break
    N=int(N)

    dp= [0]*( int(M*100+0.5)+1)
    L=[ [0,0] ]
    for i in range(N):
        a,b=map(float,input().split())
        L.append([int(a) , int(b*100+0.5)])

    for i in range(1,N+1):
        for j in range(1,int(M*100)+1):
            weight=L[i][1] ; value=L[i][0]
            if j>=weight:
                dp[j] = max(dp[j - weight] + value, dp[j - 1], dp[j])
                weight += L[i][1]; value += L[i][0]
            else:
                dp[j]=max(dp[j],dp[j-1])
    print(dp[-1])