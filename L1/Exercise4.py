import math
def getVariance(list):
    sum = 0
    X = getMean(list)
    n = 0
    for ni in list:
        try:
            n = n + 1
            vi = (X - ni) * (X - ni)
            sum = sum + vi
        except:
            return

    result = sum / n
    return result

def getStandarDeviation(list):
    sDev = 0
    try:
        variance = getVariance(list)
        sDev = math.sqrt(variance)
    except:
        return
    return sDev


def getMean(list):
    sum = 0
    n = 0
    for ni in list:
        try:
            n = n + 1
            sum = sum + ni
        except:
            return

    result = sum / n
    return result


userList  =input("Enter list of numbers (separated by ',')")
numbers = userList.split(",")
numberList = []
for number in numbers:
    try:
        ni = float(number)
        numberList.append(ni)
    except:
        print ("Invalid input")

sDev = getStandarDeviation(numberList)
mean = getMean(numberList)
print ("Mean : " + str(mean))
print("standar deviation: " + str(sDev))

