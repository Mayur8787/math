def solution(n) :
    max_factor = 2

    while max_factor * max_factor <= n :
        while n % max_factor == 0:
            n //= max_factor
        max_factor += 1
    
    if n > 1:
        return n
    return max_factor