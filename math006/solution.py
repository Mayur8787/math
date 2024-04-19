def solution(p,q) :
    square_of_sum = ((q//2)*((2*p)+(q-1)))**2
    sum_of_squares = ((q * (q + 1) * (2 * q + 1)) // 6) - ((p * (p + 1) * (2 * p + 1)) // 6) +1
    return square_of_sum - sum_of_squares

print(solution(1,100))