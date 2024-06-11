gap = 2
numbers = [1]
i = 1
while i < (1001*1001):
    iter = 4
    for j in range(0,4) :
        i += gap
        numbers.append(i)
    gap += 2

print(sum(numbers))

# Answer : 669171001