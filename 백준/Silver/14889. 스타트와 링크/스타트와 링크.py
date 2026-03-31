n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
def comb(arr, n):
    res = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        for C in comb(arr[i+1:],n-1):
            res.append([elem]+C)
    return res
li = [i for i in range(n)]
li_com = comb(li, n//2)

min_val = 1e9
for team in li_com:
    other = [i for i in li if i not in team]
    
    team_stat = 0
    other_stat = 0
    
    for i in team:
        for j in team:
            team_stat += graph[i][j]
            
    for i in other:
        for j in other:
            other_stat += graph[i][j]
            
    min_val = min(min_val, abs(team_stat - other_stat))

print(min_val)
    