"""
    All of the y-digits long numbers can be accepted as a
    multi-line string and then we can use replace() method and
    string slicing to store each number as a string in the list.

    Numbers can also be accepted one by one and stored into a string.

    Also We don't have to add all the least significant bits.
    We just have to take first x+1 most significant bits into
    consideration. That means for 10 digits we just have to add first
    11 digits from the numbers. We can also take first x bits but for
    safety we've taken x+1.
"""


def solution(numbers:str,n:int,y:int,x:int):
    numbers = numbers.replace("\n","")
    answer = ""
    carry = 0

    number_list = []

    for i in range(0,n*y,y):
        number_list.append(numbers[i:i+y])
    
    for digit in range(x+1,-1,-1):
        total = str(sum([int(i[digit]) for i in number_list]) + carry)
        if len(total) > 1:
            answer += total[-1]
            carry = int(total) // 10
        else:
            answer += total[-1]
            carry = 0
    answer = str(carry) + answer[::-1]
    return answer[:x]

print(solution)