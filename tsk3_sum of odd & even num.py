X = int(input(" A= "))
Y = int(input(" B= "))
even = 0
odd = 0
for number in range(X,Y + 1):
    if(number % 2 == 0):
        even = even + number
    else:
        odd = odd + number
 
print("The Sum of Even Numbers " ,even)
print("The Sum of Odd Numbers ",odd)
 
