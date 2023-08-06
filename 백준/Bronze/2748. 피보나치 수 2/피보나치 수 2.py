n = int(input())

arr = []

def function(a):
    for i in range(a):
        if i == 0:
            arr.append(0)
        elif i <= 2:
            arr.append(1)
        else:
            num = arr[-1] + arr[-2]
            arr.append(num)
    
function(n+1)
print(arr[-1])