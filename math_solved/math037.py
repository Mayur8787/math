def solution() :
    limit = 1000000
    counter = 11
    special = 0
    a = [True for i in range(limit)]
    number = 2

    while number * number <= limit:
        if a[number] :
            for i in range(number*number,limit,number) :
                a[i] = False
        number += 1
    
    a[1] = False
    for j in range(20,len(a)) :
        if counter == 0:
            break
        if a[j]:
            flag = True
            number = str(j)
            for i in range(1,len(number)) :    #removing from left side
                if not a[int(number[i:])] :
                    flag = False
                    break
            for i in range(len(number)-1,0,-1) :  #removing from right side
                if not flag:
                    break
                if not a[int(number[:i])] :
                    flag = False
                    break
            if flag:
                special += j
                counter -= 1
    print(special)
                


solution()


# Answer : 748317