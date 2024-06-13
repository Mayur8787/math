primes = []

def checker(n) :
    if n in primes:
        return True
    
    for i in range(2,int(n**(1/2))+1) :
        if n % i == 0 :
            return False
    primes.append(n)
    return True



gap = 2
numbers = []
i = 1
size = 3
total_primes = 3
count = 0
while total_primes/(size+(size-1)) > 0.10 :
    for j in range(0,4) :
        i += gap
        if checker(i) :
            numbers.append(i)
    total_primes = len(numbers)
    gap += 2
    size += 2
print("answer",size)


# Answer : 26241