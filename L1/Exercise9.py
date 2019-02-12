def addDigit(digit, t):
    result = ""
    for i in range(t):
        result = result + digit
    return result

def addSubdigit(subDigit, digit):
    result = subDigit + digit ;
    return result

def decimalToRoman(number):
    result = ""
    while number > 0 and number < 3000:
        if number > 1000:
            nM = int(number/1000)
            number = number % 1000
            result = result + addDigit("M",nM)
        elif number >= 500:
            if number < 900:
                nD = int(number/500)
                result = result + addDigit("D", nD)
                number = number % 500
            else:
                result = result + addSubdigit("C","M")
                number = number % 100
        elif  number >= 100:
            if number < 400:
                nD = int(number / 100)
                result = result + addDigit("C", nD)
                number = number % 100
            else:
                result = result + addSubdigit("C", "D")
                number = number % 100
        elif number >= 50:
            if number < 90:
                nD = int(number / 50)
                result = result + addDigit("L", nD)
                number = number % 50
            else:
                result = result + addSubdigit("X", "C")
                number = number % 10
        elif number >= 10:
            if number < 40:
                nD = int(number / 10)
                result = result + addDigit("X", nD)
                number = number % 10
            else:
                result = result + addSubdigit("X", "L")
                number = number % 10
        elif number >= 5:
            if number < 9:
                nD = int(number / 5)
                result = result + addDigit("V", nD)
                number = number % 5
            else:
                result = result + addSubdigit("I", "X")
                number = 0
        elif number >= 1:
            if number < 4:
                result = result + addDigit("I", number)
                number = 0
            else:
                result = result + addSubdigit("I", "V")
                number = 0

    return result

userInput = ""
userInput = input("Enter decimal number [1-3000]: ")
while not userInput == "X":
    try:
        number = int(userInput)
        romanFormat = decimalToRoman(number)
        if romanFormat != "":
            print ("Roman format: " + romanFormat)
        else:
            print ("Invalid number.")
    except:
        print("Invalid number.")
    userInput = input("Enter decimal number [1-3000] or press 'X' to exit: ")
