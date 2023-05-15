import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr1 = list(map(int,sys.stdin.readline().split()))
    arr.append(arr1)

answer = []
for k in arr:
    cnt = 1
    for j in arr:
        if(k[0]<j[0] and k[1]<j[1]):
            cnt += 1
    print(cnt,end=" ")
