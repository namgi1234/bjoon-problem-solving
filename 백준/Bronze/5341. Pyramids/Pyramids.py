while True:
    number = int(input())
    
    if number == 0:
        break
        
    print(number * (number + 1) // 2)