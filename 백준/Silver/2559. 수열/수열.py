n, k = map(int, input().split())

temperture = list(map(int,input().split()))

log = []

log.append(sum(temperture[:k]))

for i in range(n-k):
    log.append(log[i]+temperture[k+i]-temperture[i])

print(max(log))