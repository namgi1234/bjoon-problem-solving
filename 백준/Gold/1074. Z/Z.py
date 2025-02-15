n, r, c = map(int, input().split())

def func(n, r, c):
    if n == 0:
        return 0  # Base case (0,0)이면 0 리턴

    half = 2 ** (n - 1)  # 현재 정사각형의 절반 크기
    size = half * half  # 한 사분면의 총 개수

    if r < half and c < half:  # 0번 사분면 (좌상)
        return func(n - 1, r, c)
    elif r < half and c >= half:  # 1번 사분면 (우상)
        return size + func(n - 1, r, c - half)
    elif r >= half and c < half:  # 2번 사분면 (좌하)
        return 2 * size + func(n - 1, r - half, c)
    else:  # 3번 사분면 (우하)
        return 3 * size + func(n - 1, r - half, c - half)


print(func(n, r, c))



