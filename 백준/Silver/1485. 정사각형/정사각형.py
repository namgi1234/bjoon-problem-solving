import sys
import math

x = [0] * 4
y = [0] * 4
s = [0] * 6

def main():
    tc = int(input())
    for _ in range(tc):
        k = 0
        for i in range(4):
            x[i], y[i] = map(int, input().split())
        
        for i in range(4):
            for j in range(i + 1, 4):
                s[k] = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
                k += 1
        s.sort()
        print(int(s[0] == s[1] and s[1] == s[2] and s[2] == s[3] and s[4] == s[5]))

if __name__ == "__main__":
    main()
