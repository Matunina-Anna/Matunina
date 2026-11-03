def reverse_letter(st):
    l=''
    for i in st:
        if i.isalpha():
            l+=i
    rev=l[::-1]
    return rev
            
    pass