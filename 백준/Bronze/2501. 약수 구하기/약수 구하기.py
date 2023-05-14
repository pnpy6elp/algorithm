num, k = map(int, input().split())
arr = []
for i in range(1,num+1):
    res = num % i
    if(res == 0):
        arr.append(i)
if(len(arr)<k):
    print(0)
else:
    print(arr[k-1])