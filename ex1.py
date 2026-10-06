namb=[]
n=int(input())
for i in range(n):
    namb.append(int(input()))
s=0
pr=None

for num in namb:
    if num!=0 and num>0:
        cur='pos'
    elif num<0:
        cur='neg' 
    else:
        continue
    if pr is not None and cur!=pr:
        s+=1
    pr=cur
print(s)
    