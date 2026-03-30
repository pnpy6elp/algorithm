n = int(input())
t = []
p = []
for _ in range(n):
    tt, pp = map(int, input().split())
    t.append(tt)
    p.append(pp)

def recursive(idx, current_profit):
    global max_p
    
    if current_profit > max_p:
        max_p = current_profit
        
    if idx >= n:
        return
        
    for next_idx in range(idx, n):
        if next_idx + t[next_idx] <= n:
            recursive(next_idx + t[next_idx], current_profit + p[next_idx])

res = []
for i in range(n):
    max_p = 0
    recursive(i, 0)
    res.append(max_p)

print(max(res))