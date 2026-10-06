n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))
count=0
for i in range(1,len(num)-1):
    pr=abs(num[i-1])
    cur=abs(num[i])
    next_m=abs(num[i+1])
    if cur>pr and cur<next_m:
        count+=1
print(count)