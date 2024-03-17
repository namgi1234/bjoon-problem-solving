n = int(input())

def function(a):
    arr = [0,1,1,1,2,2,3,4,5,7,9]
    if a <= 10 :
        print(arr[a])
    else :
        for i in range(a-10):
            num = arr[-1] + arr[-5]
            arr.append(num)
        print(arr[-1])

for i in range(n):
    a = int(input())
    function(a)