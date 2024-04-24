def solution(number):
    if number == 0 :
        return 1
    return number*solution(number-1)