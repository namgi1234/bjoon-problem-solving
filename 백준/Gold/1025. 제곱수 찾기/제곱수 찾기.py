import math

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())

answer = -1

def sqr(S):
    S = int(S)
    return int(math.sqrt(S)) * int(math.sqrt(S)) == S

for i in range(N):
    for j in range(M):
        for row_d in range(-N, N):
            for col_d in range(-M, M):
                S = ""
                x = i
                y = j
                if row_d == 0 and col_d == 0:
                    continue
                while 0 <= x < N and 0 <= y < M:
                    temp = board[x][y]
                    S += temp
                    if sqr(int(S)):
                        answer = max(answer, int(S))
                    x += row_d
                    y += col_d

print(answer)