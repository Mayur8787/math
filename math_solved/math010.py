def primeSum(limit) :
  ref = [True for i in range(limit)]

  number = 2
  while number*number < limit:
    for i in range(number*number,limit,number):
      if ref[i]:
        ref[i] = False
    number += 1
  
  primes = 0
  for i in range(2,limit):
    if ref[i]:
      primes += i
  return primes


print(primeSum(2_000_000)) #output : 142913828922