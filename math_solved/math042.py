def checkTriangle(number: int) :
    """
    Helper Function to check if the given number is a triangle number or not
    """
    num = 1
    while num * (num+1) <= 2*number:
        if num*(num+1) == 2*number :
            return True
        num += 1
    return False


def solution():
    """
    Function to solve the problem
    """
    answer = 0

    with open('words.txt','r') as fp:
        for word in fp.read().split(',') :
            wordvalue = 0
            for letter in word.strip('"'):
                value = ord(letter) - 64
                wordvalue += value
            if checkTriangle(wordvalue) :
                answer += 1
    return answer



if __name__ == "__main__" :
    print(solution())

#Answer : 162
