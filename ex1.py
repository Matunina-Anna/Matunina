a=input()
def izo(s):
    for car in s:
        if s.count(car)>1:
            return False
    return True
print(izo(a))