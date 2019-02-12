import random

def passwordGenerator(num):
    ranges = [[65,90],[97,121],{48,57},[33,47],[58,64]]
    pwdLength = num
    password = ""
    for i in range(pwdLength):
        randCharType = random.randint(0,4);
        rangeArr = list(ranges[randCharType])
        x = rangeArr[0]
        y = rangeArr[1]
        randCharValue = random.randint(x, y)
        password = password + chr(randCharValue)

    return password
while True:
    try:
        num = int(input("Enter Password length: "))
        print("Generated password : " + passwordGenerator(num))
    except:
        print ("Invalid input")
