fib = [0,1]

index = 1

while len(str(fib[1])) < 1000:
    fib[0],fib[1] = fib[1],fib[0]+fib[1]
    index += 1
print(index)