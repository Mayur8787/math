weights = {'\"':0}

start = 1
for i in range(65,65+26):
    weights[chr(i)] = start
    start += 1

ans = 0

with open('names.txt','r') as file:
    data = sorted(file.read().split(","),key=lambda n: n[1:-1])
    for i in range(len(data)) :
        summ = 0
        for j in data[i]:
            summ += weights[j]
        ans += (summ*(i+1))

print(ans)