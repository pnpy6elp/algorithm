import sys
input = sys.stdin.readline

n = int(input().rstrip()) # the num of cities (여기에 주유소가 있음)
roads = list(map(int, input().split())) # 필요한 리터
cities = list(map(int, input().split())) # 각 도시에서의 리터 당 가격
# 비용은 도시에서 기름 충전할 때만 발생
result = cities[0] * roads[0] # 무조건 첫번째 도로를 지나갈 만큼은 충전해야함
m = cities[0] # 현재 도시의 가격
dist = 0
for i in range(1,n-1):
    if cities[i] < m: # 다음 정류장이 현재보다 더 가격이 낮음
        result += m*dist
        dist = roads[i]
        m = cities[i]
    else:
        dist += roads[i] # 아니면 그 다음 정류장까지 가는 것까지 충전해야함
    if i == n-2: # 마지막 도로 직전
        result += m*dist
print(result)
        
    





