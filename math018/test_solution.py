class Listnode:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

def nodeComparison(head1,head2):
    sum1 = 0
    curr = head1
    while curr:
        sum1 += curr.value
        curr = curr.next
    sum2 = 0
    curr = head2
    while curr:
        sum2 += curr.value
        curr = curr.next
    if sum1 >= sum2 :
        return head1
    return head2


def nodeSummer(head):
    curr = head
    summ = 0

    while curr :
        summ += curr.value
        curr = curr.next
    return summ
    


def solution(numbers):
    for i in range(len(numbers[-1])):
        numbers[-1][i] = Listnode(numbers[-1][i])

    for i in range(len(numbers)-2,-1,-1):
        for j in range(len(numbers[i])):
            numbers[i][j] = Listnode(numbers[i][j],nodeComparison(numbers[i+1][j],numbers[i+1][j+1]))
    return nodeSummer(numbers[0][0])


with open('new.txt','r') as file:
    data = file.read().strip().split('\n')
    pyramid = []
    for i in data:
        pyramid.append(list(map(int,i.strip().split())))
    print(solution(pyramid))