def solution(number):
    def factHelper(number):
        if number == 0 :
            return 1
        return number*solution(number-1)
    return sum([int(i) for i in str(factHelper(number))])
