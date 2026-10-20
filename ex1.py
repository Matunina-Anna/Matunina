lst=[10, 'hello', True, 20, 6.5]
to=0
count=0
for i in lst:
    if type(i) in (int, float):
        to+=i
        count+=1
    if count==0:
        count=1
res=to/count

print(res)