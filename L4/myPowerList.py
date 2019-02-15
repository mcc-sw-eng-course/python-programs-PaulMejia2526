class myPowerList:

    def __init__(self):
        self.myList = list()


    def readFromTextFile(self, filePath):
        file = open(filePath, "r") # read from file
        self.myList.clear() # limpiar la lista
        for line in file.readlines():
            self.myList.append(line) # cada linea del archivo se agrega como un nuevo elemento a la lista
        file.close()
        return self.myList


