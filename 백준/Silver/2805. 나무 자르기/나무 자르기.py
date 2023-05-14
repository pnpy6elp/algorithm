# 4 7
# 20 15 10 17
K, M = map(int, input().split()) # M은 집에 가지고 가려고 하는 나무의 길이의 합
arr = list(map(int, input().split()))
lt, rt = 0, max(arr) # 최대는 가장 높은 나무의 높이
while lt <= rt:
    mid = (lt + rt) // 2 # H?
    cnt = 0
    for tree in arr:
        if(tree>=mid):
            cnt += (tree-mid)
    if M > cnt:
        rt = mid - 1
    elif M <= cnt:
        lt = mid + 1
print(rt)        
    