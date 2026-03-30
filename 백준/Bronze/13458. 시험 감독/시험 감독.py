n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
import math
ans = 0
for i in a:
    if b >= i:
        ans += 1
    else:
        x = math.ceil((i-b)/c)
        ans += (1+x)
print(ans)