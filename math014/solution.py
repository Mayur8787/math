def solution(p: int = None, q: int = None) :
    if not p and not q:
        return None
    elif not q:
        number = 2
        end = p
    else:
        number = p
        end = q
    
    ref = {}
    maxx = 0
    ans = None

    while number < end:
        score = 1
        copy = number
        while copy != 1:
            if copy in ref:
                score += ref[copy] - 1
                break
            if copy % 2 == 0:
                copy //= 2
                score += 1
            else:
                copy = (3*copy) + 1
                score += 1
        ref[number] = score
        if score > maxx:
            maxx = score
            ans = number
        number += 1
    
    return ans

