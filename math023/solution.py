def solution(p=12, q=28123):
    def helper(number):
        total = 1
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                total += i
                if i != number // i:
                    total += number // i
        return total
    abundant = []
    for i in range(p, q + 1):
        if helper(i) > i:
            abundant.append(i)
    
    abundant_sum = [False] * (q + 1)
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            sum_abundant = abundant[i] + abundant[j]
            if sum_abundant <= q:
                abundant_sum[sum_abundant] = True
            else:
                break
    result = [i for i in range(1, q + 1) if not abundant_sum[i]]
    return sum(result)

solution()