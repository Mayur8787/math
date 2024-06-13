ref = set()

def chainCalculator(number) :
    bag = []
    if number in ref :
        return 89
    while number != 89 :
        if number == 1:
            break
        bag.append(number)
        number = sum([int(i)**2 for i in str(number)])
    if number == 89 :
        ref.update(bag)
    return number



count = 0
for i in range(1,10_000_000) :
    if chainCalculator(i) == 89 :
        count += 1

print(count)

# Answer : 8581146