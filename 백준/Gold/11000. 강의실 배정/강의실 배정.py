import sys
import heapq
input = sys.stdin.readline
N = int(input().rstrip())
li = []
for i in range(N):
    s, t = map(int, input().split())
    li.append([s,t])
li.sort()
heap = []
cnt = 0
for s, e in li:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
print(len(heap))     