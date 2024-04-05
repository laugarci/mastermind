import random

def oneNumCorrect(num):
    digits = [int(d) for d in str(num)]

    firstDigit = digits[0];
    newNum = num;

    while True:
        newNum = random.randint(100, 999)
        newDigits = [int(d) for d in str(newNum)]
        if len(set(newDigits)) == 3:
            return (newNum)

def resultNum():
    while True:
        num = random.randint(100, 999)
        digits = [int(d) for d in str(num)]
        if len(set(digits)) == 3:
            return num;

def checkIncorrectNums(num):
    digits = [int(d) for d in str(num)]
    
    incorrectNum = num
    while any(str(digit) in str(incorrectNum) for digit in digits) or len(set(str(incorrectNum))) < 3:
        incorrectNum = random.randint(100, 999)
    return (incorrectNum)

num = resultNum();
noNum = checkIncorrectNums(num);
oneNum = oneNumCorrect(num);

print (num);
print (str(noNum) + " => todos los numeros son incorrectos")
print (str(oneNum) + " => un numero es correcto pero en el sitio incorrecto")
