n=int(input("n = "))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("sum:",tot)
