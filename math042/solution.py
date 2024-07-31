from math import ceil, floor
"""
Solution of Euler problem number 42
"""
def checkTriangle(number):
    """
    Helper Function to check if the given number is Triangle or not
    """
    roots = (((1+(8*number))**(1/2)) - 1) / 2
    if floor(roots) == ceil(roots) :
        return True
    else:
        return False


def solution(input_file):
    """
    Solution function
    """
    answer = 0
    fp = open(input_file,'r')
    words = [i.strip('"') for i in fp.read().strip().split(',')]
    fp.close()

    for word in words:
        total = sum([ord(letter)-64 for letter in word])
        if checkTriangle(total) :
            answer += 1
    return answer




if __name__ == "__main__":
    file = 'words.txt'
    print(solution(file))