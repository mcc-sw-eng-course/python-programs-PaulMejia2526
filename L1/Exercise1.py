
while True:
    numStr = input("Enter an integer number (Press X to exit): ")
    if numStr == "X":
        break
    try:
        num = int(numStr)
        mod = num % 2
        if num  % 2 == 0:
            print ('The number ' + numStr +' is even' )
        else:
            print ('The number '+ numStr +' is odd')

        if num % 4 == 0:
            print("Enter two numbers: ")
            numStr = input("Num: ")
            checkStr = input("Check: ")
            num = int(numStr)
            check = int(checkStr)
            if num % check == 0:
                print(checkStr + " divides evenly into " + numStr)
            else:
                print(checkStr + " NOT divides evenly into " + numStr)



    except:
        print('Invalid input ')

