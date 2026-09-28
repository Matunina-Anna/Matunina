import math
x=3.76
dun=5*(x**5)+math.exp(-x)*math.cos(5*x)
num=3*(x**3)+(3**x)*math.sin(3*x)
y=dun/num
print(y)