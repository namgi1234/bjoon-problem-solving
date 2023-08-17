score = []
ans = []
answer = 0

for _ in range(8):
    score.append(int(input()))

for i in range(5):
    answer += max(score)
    ans.append(score.index(max(score)) + 1)
    score[score.index(max(score))] = -1

ans.sort()
print(answer)
print(*ans)