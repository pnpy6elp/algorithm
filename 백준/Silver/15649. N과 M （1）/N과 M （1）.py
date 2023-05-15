import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘리는 용도 -> 런타임 에러 방지
n, m = map(int, sys.stdin.readline().split())
result = []
visited = [False] * (n+1) # index를 1부터 사용하려고. visited는 방문한 node
# backtracking
def backtrack(num): # num is the depth of graph
    if(num==m):
        print(' '.join(map(str, result))) #리스트에 있는 애들 출력
    for i in range(1,n+1):
        # 숫자 노드들 탐색 중
        if not visited[i]:
            visited[i]=True
            result.append(i)
            backtrack(num+1) # depth 1씩 추가
            visited[i]=False
            result.pop() # 상위 노드로 돌아감
backtrack(0)
            

        