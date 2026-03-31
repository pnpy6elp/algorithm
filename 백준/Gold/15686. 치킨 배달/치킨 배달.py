n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
# 0 빈칸, 1 집, 2 치킨집
visited = [[False]*n for _ in range(n)]

from collections import deque
house = deque([])
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))
def comb(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for C in comb(arr[i+1:],n-1):
            res += [[elem]+C]
    return res

combs = comb(chicken, m)
min_city_dist = float('inf')  # 도시의 치킨 거리 최솟값을 저장할 변수
for c in combs:
    city_dist = 0
    for hx, hy in house:
        min_house_dist = float('inf')
        for cx, cy in c:
            dist = abs(hx - cx) + abs(hy - cy)
            if dist < min_house_dist:
                min_house_dist = dist
        city_dist += min_house_dist
    if city_dist < min_city_dist:
        min_city_dist = city_dist

print(min_city_dist)