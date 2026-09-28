import math
to=0
for n in range(1,51):
    num=math.tan(2*n+(math.pi/2))
    den=math.factorial(n+1)
    to+=num/den
print(to)