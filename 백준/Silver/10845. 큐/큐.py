import sys
N = int(sys.stdin.readline())
queue = []
for i in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0]=="push":
        queue.insert(0, cmd[1]) # stack과 다름!! insert로 제일 앞에 넣어주기
    elif cmd[0]=="pop":
        if(len(queue)==0):
            print(-1)
        else:
            print(queue.pop())
    elif cmd[0]=="front":
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[-1])
    elif cmd[0]=="back":
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
    elif cmd[0]=="size":
        print(len(queue))
    elif cmd[0]=="empty":
        if(len(queue)==0):
            print(1)
        else:
            print(0)