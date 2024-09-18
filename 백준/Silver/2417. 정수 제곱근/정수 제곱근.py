n = int(input())
q = int(n**0.5)

if q * q < n:q += 1

print(q)