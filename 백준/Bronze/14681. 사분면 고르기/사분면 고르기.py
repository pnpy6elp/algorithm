data = [int(input()) for i in range(2)]
result = 0 
if(data[0]>0 and data[1]>0):
    result = 1
elif(data[0]<0 and data[1]>0):
    result = 2
elif(data[0]<0 and data[1]<0):
    result = 3
elif(data[0]>0 and data[1]<0):
    result = 4
print(result)