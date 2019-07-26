st = input('Enter String:')
ps = " "
for i in st:
    if i.isupper():
        p=i.lower()
    elif i.islower():
        p=i.upper()
    else:
        p = i
    ps +=p
print(ps)
