s=[1,1,1,2,2,3]
k=int(input())
par=[]
for i in set(s):
    count=s.count(i)
    par.append([count, i])

par.sort(reverse=True)
res=[]
for i in range(k):
    res.append(par[i][1])
print(res)
