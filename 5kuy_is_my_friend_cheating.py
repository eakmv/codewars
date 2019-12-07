def removNb(n):
    sum_n = sum(range(0, n + 1))
    result = []
    for i in range(1, n + 1):
        temp = (sum_n - i) / (i + 1)
        if temp % 1 == 0 and temp <= n:
            result.append((i, int(temp)))

    return sorted(result, key=lambda a: result[:][0])