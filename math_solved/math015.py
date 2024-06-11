def fact(number):
    if number == 0:
        return 1
    return number*fact(number-1)


def solution(n) :
    return fact(2*n)//(fact(n)**2)


print(solution(20))


# Answer : 137846528820