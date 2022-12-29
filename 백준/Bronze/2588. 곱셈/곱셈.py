data = [int(input()) for i in range(2)]
data[1] = str(data[1])
result=[]
zero = 0
for i in list(data[1][-1::-1]):
    result.append(data[0]*int(i+"0"*zero))
    print(data[0]*int(i))
    zero += 1
print(sum(result))