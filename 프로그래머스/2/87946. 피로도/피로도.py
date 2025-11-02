def solution(k, dungeons):
    n = len(dungeons)
    used = [False] * n
    best = 0

    def dfs(curr_k, cleared):
        nonlocal best
        best = max(best, cleared)  # 현재까지 진행한 개수로 갱신
        for i in range(n):
            req, cost = dungeons[i]
            if not used[i] and curr_k >= req:
                used[i] = True
                dfs(curr_k - cost, cleared + 1)
                used[i] = False

    dfs(k, 0)
    return best
