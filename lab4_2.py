import math
s=1.0
for n in range(1,11):
    num=n**2+math.sin(n*math.pi/2)
    den=n**2+n
    s*=num/den
print(s)