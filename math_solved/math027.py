def isPrime(number) :
    if number <= 1:
        return False
    for i in range(2,int(number**(1/2))+1) :
        if number % i == 0:
            return False
    return True

numberOfPrimes = 0
max_A = 0
max_B = 0

for a in range(-1000,1000) :
    for b in range(-1000,1001) :

        n = 0
        primes = 0
        while isPrime(n**2+(a*n)+b) :
            primes += 1
            n += 1
        
        if primes > numberOfPrimes :
            numberOfPrimes = primes
            max_A = a
            max_B = b


print(max_A*max_B)

# Answer : -59231