
''' Below is the solution for Part A and Part B combined.
    The worst case time complexity is : O(n*m)
            Where n = Length of the list
                  m = Total Range from start to end  
'''






def sum_of_multiples(number_list=[], start=1, end=1000):
    if not number_list:
        return sum([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0])
    answer = 0
    for i in range(start,end+1):
        for j in number_list:
            if i % j == 0:
                answer += i
                break
    return answer