t= int(input())
for i in range(t):
    k = int(input())
    cnt = 0
    while(k>0):
        if(k%2==1):
            print(cnt, end=" ")
        k = k // 2
        cnt += 1
