from collections import deque
import sys

read = sys.stdin.readline

n, m = map(int,read().split())

s = []
visited = [False]*(n+1)

def dfs(v):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
            s.append(i)
            dfs(i)
            s.pop()


dfs(1)

