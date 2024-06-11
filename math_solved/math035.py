answer = 0

limit = 1_000_000
number_array = [True for i in range(limit)]

number = 2

while number*number <= limit :
    if number_array[number]:
        for i in range(number*number,limit,number):
            number_array[i] = False
    number += 1

for i in range(2,limit):
    flag = True
    if number_array[i] :
        number = [int(k) for k in str(i)]
        for j in range(len(str(i))) :
            last = number.pop(0)
            number.append(last)

            if not number_array[int("".join(str(i) for i in number))] :
                flag = False
                break
        
        if flag :
            answer += 1

print("answer",answer)


# answer : 55