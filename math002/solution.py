"""

    Below is the solution for Part A of the problem.

"""


def answer():
    number1 = 1
    number2 = 2
    answer = 0

    while number1 <= 4_000_000:
        if number1 % 2 == 0:
            answer += number1

        number1, number2 = number2, number1 + number2
    return answer


"""

    Below is the solution for Part B of the problem.

"""


def solver(start, end, even=False, odd=False):
    if start > end:
        return None
    e_sum = 0 if even else None
    o_sum = 0 if odd else None
    flag = False
    n1 = 1
    n2 = 2

    while n1 <= end:
        if n1 >= start:
            flag = True
        if flag and even and n1 % 2 == 0:
            e_sum += n1
        elif flag and odd:
            o_sum += n1

        n1, n2 = n2, n1 + n2

    return {"Even_Sum": e_sum, "Odd_sum": o_sum}


"""

Below is the Universal Solution for both the problems.


"""


def solution(start=1, end=4_000_000, even=False, odd=False):
    if start > end:
        return None

    number1 = 1
    number2 = 2

    answer = 0
    e_sum = 0 if even else None
    o_sum = 0 if odd else None

    flag = False

    while number1 <= end:
        if number1 >= start:
            flag = True
        if flag:
            if number1 % 2 == 0:
                if even:
                    e_sum += number1
                answer += number1
            else:
                if odd:
                    o_sum += number1
        number1, number2 = number2, number1 + number2

    if start == 1 and end == 4_000_000 and not even and not odd:
        return answer
    if even and odd:
        return e_sum + o_sum
    elif even and not odd:
        return e_sum
    elif odd and not even:
        return o_sum
    return None
