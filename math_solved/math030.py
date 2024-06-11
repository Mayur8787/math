answer = 0

for i in range(1000,10000000) :
    summ = 0

    for j in str(i) :
        summ += int(j)**5
    
    if i == summ:
        answer += summ

print(answer)


# answer : 443839