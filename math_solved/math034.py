def fact(number) :
    if number == 0:
        return 1
    return number*fact(number-1)

answer = 0


for i in range(10,10000000) :
    summ = 0

    for j in str(i) :
        summ += fact(int(j))
    
    if i == summ:
        answer += summ

print(answer)


# answer : 40730