class User:

    def __init__(self):
        self.Name = ""
        self.Address = ""
        self.Phone = ""
        self.Email = ""


    def getUserRecord(self):
        userDict = {
            "Name" : self.Name,
            "Address" : self.Address,
            "Phone" : self.Phone,
            "Email" : self.Email
        }
        return  userDict

    def setUserRecord(self, userDict):
        self.Name = userDict["Name"]
        self.Address = userDict["Address"]
        self.Phone = userDict["Phone"]
        self.Email = userDict["Email"]

    def __str__(self):
        userDict = {
            "Name": self.Name,
            "Address": self.Address,
            "Phone": self.Phone,
            "Email": self.Email
        }
        return str(userDict)
