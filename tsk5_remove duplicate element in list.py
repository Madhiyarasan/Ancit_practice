li=[1,2,3,4,2,1,2,1,5]
x=[]
for i in li:
    if i not in x:
        x.append(i)
        x.sort()
print(x)
