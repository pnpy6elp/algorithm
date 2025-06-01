import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort()  # 무게 오름차순
bags.sort()    # 용량 오름차순

result = 0
heap = []
j = 0

for c in bags:
    while j < N and jewels[j][0] <= c:
        # 힙은 최소 힙이므로 가치에 -를 붙여 최대 힙처럼 사용
        heapq.heappush(heap, -jewels[j][1])
        j += 1
    if heap:
        result += -heapq.heappop(heap)

print(result)
