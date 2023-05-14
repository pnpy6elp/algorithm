from collections import Counter
N = int(input())
arr = []
for i in range(N):
    arr.append(input())
arr.sort()
cnt = 0
tmp = ""
for i in range(len(arr)):
    count = Counter(arr[:i+1])
    a = count[arr[i]]
    if(a>cnt):
        cnt = a
        tmp = arr[i]
print(tmp)
    
    
