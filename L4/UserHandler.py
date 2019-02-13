import User
import myPowerList
import json

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
            userJson = user.replace("\n","")
            userDict = json.loads(userJson)
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

