sum = 0


for i in range(1,1_000_001) :
    if str(i) == str(i)[::-1] and str(bin(i)[2:]) == str(bin(i)[2:])[::-1] :
        sum += i


print(sum)

# Answer : 872187