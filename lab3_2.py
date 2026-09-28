import math 
a=-0.3
b=0.7
step=0.05
n=int((b-a)/step)+1
print(f"{'x':>7}|{"y":>10}")
print("-"*20)
for i in range(n):
    x=a+i*step
chis=abs(math.sin(x)-math.cos(x))
zn=math.sin(x**2)**3+math.cos(x**3)**2


y=math.sqrt(chis/zn)
print(f'{x:7.2f}|{y:10.5f}')