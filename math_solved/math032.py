def is_pandigital(identity) :
    if len(identity) != 9 :
        return False
    
    if "0" in identity:
        return False

    for i in identity:
        if identity.count(i) != 1:
            return False
    return True


def isPandigitalProduct(number) :
    i = 1
    while i * i <= number:
        if number % i == 0 and is_pandigital(str(number)+str(i)+str(number//i)) :
            return True
        i += 1
    return False


answer = 0
for i in range(4396,7853) :
    if isPandigitalProduct(i):
        answer += i
print("Answer",answer)

# Answer : 45228