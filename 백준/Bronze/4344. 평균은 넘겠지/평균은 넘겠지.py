N = int(input())

for _ in range(N):
    arr = list(map(int, input().split()))
    av = sum(arr[1:]) / arr[0]
    ans = 0
    for i in arr[1:]:
        if i > av:
            ans += 1
    av_per = ans/arr[0] *100
    print(f'{av_per:.3f}%')