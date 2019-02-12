import statistics

userInput = input("Enter list to evaluate (separated by ',' ): ")
listStr = userInput.split(",")
listNumbers = list(map(int, listStr))

nQuartil = statistics.getNquartil(3,listNumbers)
nPercent = statistics.getNpercentil(75, listNumbers)
mean = statistics.getMean(listNumbers)
sD = statistics.getStandarDeviation(listNumbers)
med = statistics.getMedian(listNumbers)
print ("Sample mean : " + str(mean))
print ("Sample standard deviation : " + str(sD))
print ("Sample median : " + str(med))
print ("3 quartil : " + str(nQuartil))
print ("75 percentil : " + str(nPercent))
