import math

A = int(input())/100
B = int(input())/100

prime = [2, 3, 5, 7, 11, 13, 17]

a = b = 0

for i in prime:
    a += (math.factorial(18)//(math.factorial(i)*math.factorial(18-i))*(A**i)*((1-A)**(18-i))) 
    b += (math.factorial(18)//(math.factorial(i)*math.factorial(18-i))*(B**i)*((1-B)**(18-i)))

print(a + b - (a*b))