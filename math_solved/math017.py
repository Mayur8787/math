digits = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
tens = {1:'ten',2:'twenty',3:"thirty",4:"forty",5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
specials = {11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:"seventeen",18:'eighteen',19:'nineteen'}


def name_calculator(number) :
    digit = special = ten = hundred = None
    if number == 1000 :
        return {"digit":digit,"special":special,"ten":ten,"hundred":hundred,"thousand":1}
    while number > 0 :
        if number >= 100 :
            hundred = digits[number // 100]
            number %= 100
        if number >= 10 :
            if str(number)[-2] == "1" and str(number)[-1] != "0":
                special = specials[number]
                number %= number
            else:
                ten = tens[number // 10]
                number %= 10
        if number >= 1 :
            digit = digits[number]
            number //= 10
    return {"digit":digit,"special":special,"ten":ten,"hundred":hundred}

def solution(num) :
    struct = name_calculator(num)
    word = ""
    if struct.get('thousand') :
        return "onethousand"
    if struct['hundred'] :
        word += struct['hundred'] + 'hundred'
        if struct['digit'] or struct['special'] or struct['ten'] :
            word += 'and'
    if struct['special'] :
        word += struct['special']
    elif struct['ten'] :
        word += struct['ten']
    
    if struct['digit'] :
        word += struct['digit']
    
    return word

answer = 0
for i in range(1,1001) :
    answer += len(solution(i))

print(answer)

# Answer : 21124