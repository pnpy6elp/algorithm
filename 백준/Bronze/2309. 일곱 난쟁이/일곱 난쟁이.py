arr = []
for i in range(9):
    arr.append(int(input()))
total = sum(arr)
fake = sum(arr) - 100 # 가짜 난쟁이의 합의 조합
arr.sort()
lt, rt = 0, 8
answer = [arr[lt],arr[rt]]
while(lt<=rt):
    tmp = arr[lt] + arr[rt]
    if(tmp>fake):
        rt -= 1
    elif(tmp<fake):
        lt += 1
    else:
        answer = [arr[lt],arr[rt]]
        break
arr.remove(answer[0])
arr.remove(answer[1])
for k in arr:
    print(k)
        
    
