t = int(input())
for i in range(t):
    n = int(input())
    arr1 = set(map(int,input().split()))
    m = int(input())
    arr2 = list(map(int,input().split()))
    for k in arr2:
        if(k in arr1):
            print(1)
        else:
            print(0)