import User
import myPowerList
class UserListHandler:
    def __init__(self):
        self.usersList = myPowerList.myPowerList()

    def createNewUserRecord(self, userDict): # hay que probar
        user = User.User() #crear objeto tipo User con variables vacias
        user.setUserRecord(userDict) #pasar diccionario con datos de el usuario para settear variables
        self.usersList.add(user)  #agregar objeto user a la lista userLists

    def saveAllRecords(self, filePath): # hay que probar #recibe el archivo de destino
        self.usersList.saveToText(filePath)

    def loadUserRecord(self, filePath):

        loadedUsers = myPowerList.myPowerList()
        loadedUsers.readFromTextFile(filePath)
        for user in loadedUsers.myList:
            userArr = user.split(",")
            userDict = {}
            for elem in userArr:
                elem = elem.replace('"', '')
                elemArr = elem.split(":")
                if len(elemArr) > 1:
                    key = elemArr[0].strip()
                    value = elemArr[1].strip()
                userDict[key] = value
            user = User.User()
            user.setUserRecord(userDict)
            self.usersList.add(user)
        return self.usersList

    def searchUserBy(self, field, criteria):
        result = myPowerList.myPowerList()
        for user in self.usersList.myList:
            userDict = user.getUserRecord()
            if str(userDict[field]).find(criteria) >= 0:
                result.add(user)
        return result


userHandler = UserListHandler()
userData = {
    "Name": "Ana Lopez",
    "Address": "Av.Madeiras 197, Int.86",
    "Phone": "3352525343",
    "Email": "1234321@itesm.mx"
}
user2Data = {
    "Name": "Maria Gonzalez",
    "Address": "Calle Jaque #210",
    "Phone": "4491123908",
    "Email": "diana.karen@gmail.com"
}

userHandler.createNewUserRecord(userData)
userHandler.createNewUserRecord(user2Data)
userHandler.saveAllRecords("userRecords_write.txt") #crea archivo con los usuarios que hay en userHandler.usersList

loadedResults = userHandler.loadUserRecord("userRecords.txt") #metodo para probar #3
print ("Loaded record from file : ")
for user in loadedResults.myList:
    print (user.getUserRecord())

criteria = input ("Search user by : Name ")
results = userHandler.searchUserBy("Name",criteria)
print("Search results --> ")
for user in results.myList:
    print (user.getUserRecord())