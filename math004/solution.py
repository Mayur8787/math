def answer():
    n1, n2 = 999, 999
    ans = -1

    for i in range(n1,99,-1) :
        for j in range(n2,99,-1) :
            product = str(i * j)
            if product == product[::-1] :
                ans = max(ans,int(product))
    return ans


def solver(n, p=None, q=None) :
    if not p and not q:
        p = int("9"*(n-1))
        q = int("9"*n)
    elif not q:
        q = p
        p = int("9"*(n-1))
    print(p,q)
    ans = -1

    for i in range(q,p,-1):
        for j in range(q,p,-1):
            product = str(i * j)
            if product == product[::-1] :
                ans = max(ans,int(product))
    return ans

