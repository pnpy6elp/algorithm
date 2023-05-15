num = set(range(1,10001))
gen = set()
for i in num:
    for j in str(i):
        i += int(j)
    gen.add(i)
self_num = sorted(num - gen)
for i in self_num:
    print(i)
