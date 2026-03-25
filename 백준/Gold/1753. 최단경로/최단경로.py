import sys
input = sys.stdin.readline
# directed graph
v, e = map(int, input().split())
# adjacency list
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(e)]

# 여러 개의 간선이 존재할 수도 있다, 방향 그래프라?
graph = [[] for _ in range(v+1)]
for i in range(e):
    x, y, z = edges[i]
    graph[x].append((y,z))
pq = []
visited = [False] * (v+1)
INT_MAX = sys.maxsize
dist = [INT_MAX] * (v+1)
dist[k] = 0
import heapq
heapq.heappush(pq, (0, k)) # dist, idx

while pq:
    min_dist, min_index = heapq.heappop(pq)
    if min_dist != dist[min_index]:
        continue
    for target_index, target_dist in graph[min_index]:
        new_dist = dist[min_index] + target_dist
        if dist[target_index] > new_dist:
            dist[target_index] = new_dist
            heapq.heappush(pq, (new_dist, target_index))
for i in range(1, v+1):
    if dist[i] != INT_MAX:
        print(dist[i])
    else:
        print("INF")


