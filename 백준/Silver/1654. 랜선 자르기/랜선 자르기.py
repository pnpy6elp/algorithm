K, N = map(int, input().split())
arr = []
for i in range(K):
    arr.append(int(input()))
arr.sort()
lt,rt = 1,max(arr)
while lt<=rt:
    mid = (lt+rt)//2
    lines = 0
    for i in arr:
        lines += i//mid
    if lines >= N:
        lt = mid + 1
    else:
        rt = mid - 1
print(rt)