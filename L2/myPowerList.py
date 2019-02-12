class myPowerList:

    def __init__(self):
        self.myList = list()

    def remove (self, n):
        if n >= 0 and n < len(self.myList):
            self.myList = self.myList[:n] + self.myList[n+1:]

    def add(self, item):
        self.myList.append(item)

    def sort(self):
        return

    def Lmerge(self, newList):
        self.myList = newList +  self.myList

    def Rmerge(self, newList):
        self.myList = self.myList + newList

    def saveToText(self, filePath):
        file = open(filePath, "w")
        for item in self.myList:
            file.write(str(item) + "\n")

    def readFromTextFile(self, filePath):
        file = open(filePath, "r") # read from file
        self.myList.clear() # limpiar la lista
        for line in file.readlines():
            self.myList.append(line) # cada linea del archivo se agrega como un nuevo elemento a la lista
        return self.myList

powerList = myPowerList()
results  = powerList.readFromTextFile("dummyLines.txt")
print ("Results from text file")
print (results)

