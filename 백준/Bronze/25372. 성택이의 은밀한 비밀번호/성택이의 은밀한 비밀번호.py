N = int(input())
for _ in range(N):
    string = input()
    if len(string) <= 9 and len(string)>=6:
        print('yes')
    else:
        print('no')