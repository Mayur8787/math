constant = ""


for i in range(1_000_001) :
    constant += str(i)

answer = 1

number = 1

for i in range(6) :
    answer *= int(constant[number])
    number = int(str(number)+"0")

print(answer)

# Answer : 210