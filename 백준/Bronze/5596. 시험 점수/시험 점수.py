import sys
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
if sum(a)<sum(b):
    print(sum(b))
else:
    print(sum(a))