h, m = map(int,input().split())
total = h*60 + m - 45
new_h = int(total/60)
new_m = total - new_h*60
if(new_m<0):
    new_total = 24*60 + new_m
    new_h = int(new_total/60)
    new_m = new_total - new_h*60
print(new_h,new_m)