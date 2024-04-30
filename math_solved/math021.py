from math import ceil , floor

def divisors(number):
    divisor = []
    for i in range(1,int(number**(1/2))+1):
        if number%i == 0:
            divisor.append(i)
            if ceil(number%i) == floor(number%i) and number//i not in divisor:
                divisor.append(number//i)
    divisor.remove(number)
    return sum(divisor)

summ = 0

for i in range(6,10000) :
    if divisors(divisors(i)) == i and divisors(i) != i :
        summ += i

print(summ)