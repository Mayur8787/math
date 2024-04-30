for i in range(2,20):
    dividend = 1
    rnd = 50
    answer = str(dividend // i) + "."
    dividend *= 10
    while rnd > 0 and dividend > 0 :
        answer += str(dividend // i)
        dividend = dividend % i * 10
        rnd -= 1
    print(i,answer)