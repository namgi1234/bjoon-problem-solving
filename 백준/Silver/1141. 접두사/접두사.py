n = int(input())

arr = []

for i in range(n):
    arr.append(input())

arr = list(set(arr))

string = sorted(arr, key=len)

ans_arr = []

for i in range(len(string)):
    can_add = True
    for j in range(len(string)):
        if string[j] != string[i]:
            if string[j].startswith(string[i]):
                can_add = False
                break

    if can_add :
        ans_arr.append(string[i])

print(len(ans_arr))