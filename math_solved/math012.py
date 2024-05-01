from math import ceil , floor

def factors(number):
  factors = 0
  for i in range(1,int(number**(1/2))+1) :
    if number%i == 0:
      factors += 1
      if ceil(number/i) == floor(number/i) :
        factors += 1
  return factors

def triangleNumber(limit):
  number = 0
  index = 1
  fct = 0
  while fct < limit:
    number += index
    index += 1
    fct = factors(number)
  return number

print(triangleNumber(500)) #76576500