h, w = map(int, input().split())

arr = []

for i in range(h):
    arr.append(list(input()))

half_area = 0
one_area = 0

for i in range(h):
    num_of_times_met = 0
    for j in range(w):
        if arr[i][j] == "/" or arr[i][j] == "\\":
            half_area += 0.5
            num_of_times_met += 1

        elif num_of_times_met % 2 == 1 :
            one_area += 1

print(one_area + int(half_area))
