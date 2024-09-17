n, p, q = map(int, input().split())
dict = {0: 1}

def solution(n):
    return dict[n] if n in dict else (dict.setdefault(n, solution(n//p) + solution(n//q)))

print(solution(n))