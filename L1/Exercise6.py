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
    try:
        userInput = input("Enter list to evaluate (separated by ',' ): ")
        listStr = userInput.split(",")
        listNumbers = list(map(int, listStr))
        fibArray =  fibArr = [0,1]
        fibArr = fibonacci(999, fibArr)
        i = 0
        validList = False;
        for item in listNumbers:
            if item == fibArr[i]:
                validList = True;
            else:
                validList = False
                break
            i = i+1
        print (validList)
    except:
        print("Invalid input. Input must be list of integer lower than 1000 elements")