def Pyramids(number):
    return number * (number + 1) // 2

while True:
    number = int(input())
    
    if number == 0:
        break
        
    print(Pyramids(number=number))