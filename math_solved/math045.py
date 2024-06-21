"""
Solution of euler Problem no 45
"""

def triangle_generator(n: int):
    """
    Helper function to generate nth triangle number
    """
    return (n*(n+1))//2


def check_pentagonal(number: int) :
    """
    Helper Function to check if number is penatgonal or not
    """
    num = 1
    while num*(3*num - 1) <= 2*number:
        if num*(3*num-1) == 2*number:
            return True
        num += 1
    return False

def check_hexagonal(number: int) :
    """
    Helper Function to check if number is hexagonal or not
    """
    num = 1
    while num*(2*num-1) <= number :
        if num*(2*num-1) == number :
            return True
        num += 1
    return False


def solution():
    """
    Main Function
    """
    index = 286

    while True:
        triangle_number = triangle_generator(index)
        if check_hexagonal(triangle_number) and check_pentagonal(triangle_number) :
            return triangle_number
        index += 1
        print(index)



if __name__ == "__main__" :
    print("Answer",solution())