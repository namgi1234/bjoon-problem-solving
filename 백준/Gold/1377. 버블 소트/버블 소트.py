import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append((num, i))

arr.sort()

max_move = 0
for sorted_index, (value, original_index) in enumerate(arr):
    move = original_index - sorted_index
    if move > max_move:
        max_move = move

print(max_move + 1)