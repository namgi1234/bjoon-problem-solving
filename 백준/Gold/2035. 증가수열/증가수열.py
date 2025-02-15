def sex_hagosipda(s):
    def backtrack(index, prev, memo):
        if index == len(s):
            return prev
        if (index, prev) in memo:
            return memo[(index, prev)]
        
        min_last, num = float('inf'), 0
        for i in range(index, len(s)):
            num = num * 10 + int(s[i])
            if num > prev:
                result = backtrack(i + 1, num, memo)
                min_last = min(min_last, result)
                if num > min_last:
                    break
        
        memo[(index, prev)] = min_last
        return min_last
    
    return backtrack(0, -1, {})

print(sex_hagosipda(input().strip()))