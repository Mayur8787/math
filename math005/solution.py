def solution(p,q):

    def lcm_helper(n1,n2) :
        def gcd(n1,n2):
            while n2 != 0:
                n1, n2 = n2, n1 % n2
            return n1
        return (n1*n2)// gcd(n1, n2)


    if q < p:
        p, q = q, p

    answer = p
    for i in range(p+1,q+1):
        answer = lcm_helper(answer,i)
    return answer

