answer = {}

for i in range(1,1001) :
    for a in range(1,1001):
        for b in range(a+1,1001) :
            c = i - a - b

            if a**2+b**2 == c**2 :
                if a > 0 and b > 0 and c > 0:
                    if not i in answer :
                        answer[i] = 1
                    answer[i] += 1
                    print(i)

print("answer:",max(answer,key=lambda a:answer[a]))


# Answer : 840