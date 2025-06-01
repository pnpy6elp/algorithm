import sys
input = sys.stdin.readline
N = input().rstrip()
li = list(N)
li = list(map(int, N))
li.sort(reverse=True)

if sum(li) % 3 == 0 and li[-1]==0:
    result = ''.join(map(str, li))
    print(result)
else:
    print(-1)