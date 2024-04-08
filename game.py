import tkinter as tk
import random

def twoNumsCorrectWrongPlace(num):
    digits = [int(d) for d in str(num)]
    chose1 = digits[0]
    chose2 = digits[2]
    errnums = [n for n in range(10) if n not in digits]
    num1 = random.choice(errnums)

    newDigits = chose2, chose1, num1
    res = "".join(map(str, newDigits)).zfill(3)
    return res

def oneNumCorrectCorrectPlace(num):
    digits = [int(d) for d in str(num)]
    randomidx = random.randint(0, 2)
    chose = digits[randomidx]

    digits.pop(randomidx)
    errnums = [n for n in range(10) if n != chose and n not in digits]
    num1 = random.choice(errnums)
    errnums.remove(num1)
    num2 = random.choice(errnums)

    digits.remove(digits[0])
    digits.remove(digits[0])

    digits.insert(0, num1)
    digits.insert(1, num2)
    digits.insert(randomidx, chose)
    res = "".join(map(str, digits)).zfill(3)
    return res

def oneNumCorrectWrongPlace(num):
    digits = [int(d) for d in str(num)]
    randomidx = random.randint(0, 2)
    chose = digits[randomidx]

    digits.pop(randomidx)

    errnums = [n for n in range(10) if n != chose and n not in digits]
    num1 = random.choice(errnums)
    errnums.remove(num1)
    num2 = random.choice(errnums)

    digits.remove(digits[0])
    digits.remove(digits[0])

    digits.insert(0, num1)
    digits.insert(1, num2)

    newpos = 0 if randomidx == 2 else 2
    digits.insert(newpos, chose)
    res = "".join(map(str, digits)).zfill(3)
    return res

def resultNum():
    while True:
        num = random.randint(100, 999)
        digits = [int(d) for d in str(num)]
        if len(set(digits)) == 3:
            return num

def checkIncorrectNums(num):
    digits = [int(d) for d in str(num)]

    incorrectNum = num
    while any(str(digit) in str(incorrectNum) for digit in digits) or len(set(str(incorrectNum))) < 3:
        incorrectNum = random.randrange(100, 999)
    return incorrectNum
