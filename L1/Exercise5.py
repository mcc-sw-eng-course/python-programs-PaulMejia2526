def fibonacci(num, fibArr):

    if(num < 3):
        return fibArr[0:num]
    else:
        if len(fibArr) == num :
            return fibArr
        else:
            n = len(fibArr)
            fibArr.append(fibArr[n-1] + fibArr[n-2])
            fibonacci(num, fibArr)

    return fibArr

while True:
    fNumStr = input("How many Fibonnaci numbers to generate: ")
    try:
        fNum = int(fNumStr)
        fibArr = [0,1]
        print (fibonacci(fNum, fibArr))
    except:
        print("Invalid input. Input must be integer lower than 1000")