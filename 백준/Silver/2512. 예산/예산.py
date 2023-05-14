N = int(input())
arr = list(map(int,input().split()))
arr.sort()
M = int(input())
lt, rt = 0 , arr[N-1]
while(lt<=rt):
    mid = (lt+rt)//2
    sum = 0
    for i in arr:
        sum += min(mid, i)
    if(sum>M):
        rt = mid - 1
    else:
        lt = mid + 1
print(rt)
        