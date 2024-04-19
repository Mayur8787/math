"""
        The program can generate primes till 5,761,455th index after that the system gets too much load.

"""


def solution(n) :
    a = [1 for i in range(100000000)]
    number = 2

    while number * number <= 100000000:
        if a[number] == 1 :
            for i in range(number*number,100000000,number) :
                a[i] = 0
        number += 1

    primes = None

    for j in range(2,len(a)) :
        if n == 0:
            return primes
        if a[j] == 1:
            primes = j
            n -= 1