n = int(input())
a_list = list(map(int, input().split()))
# +, -, *, // 
add, sub, mul, div = map(int, input().split())

# 최댓값, 최솟값 초기화
max_val = -1e10
min_val = 1e10

# idx: 현재 계산할 숫자의 인덱스, current_val: 지금까지 계산된 결괏값
def dfs(idx, current_val, add, sub, mul, div):
    global max_val, min_val
    
    # 1. 탈출 조건: 모든 숫자를 다 계산했다면 최댓값, 최솟값 갱신
    if idx == n:
        max_val = max(max_val, current_val)
        min_val = min(min_val, current_val)
        return
        
    # 2. 선택지 탐색: 남은 연산자가 있다면 하나씩 써보며 다음 숫자로
    if add > 0:
        dfs(idx + 1, current_val + a_list[idx], add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, current_val - a_list[idx], add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, current_val * a_list[idx], add, sub, mul - 1, div)
    if div > 0:
        # int(a / b) 를 쓰면 문제에서 요구하는 'C++14 기준 음수 나눗셈'과 완벽하게 똑같이 작동
        dfs(idx + 1, int(current_val / a_list[idx]), add, sub, mul, div - 1)

# 첫 번째 숫자(a_list[0])를 현재 값으로 넣고, 1번째 인덱스부터 탐색 시작!
dfs(1, a_list[0], add, sub, mul, div)

# int형으로 깔끔하게 출력
print(int(max_val))
print(int(min_val))