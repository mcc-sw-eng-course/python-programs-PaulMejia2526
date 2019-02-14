import unittest
import UserHandler
import coverage

class TestUserHandler(unittest.TestCase):

    def test_searchByUser_Loadedfromfile(self):
        userHandler = UserHandler.UserListHandler()
        userHandler.loadUserRecord("test_users.txt")
        userResults = userHandler.searchUserBy("Name","Irma Nataly Alonso de Leon")
        for user in userResults.myList:
            name = user.getUserRecord()["Name"]
            address = user.getUserRecord()["Address"]
            phone = user.getUserRecord()["Phone"]
            email = user.getUserRecord()["Email"]
            self.assertEqual(name, "Irma Nataly Alonso de Leon")
            self.assertEqual(address, "Av.Madeiras 197, Int.46")
            self.assertEqual(phone, "3318623976")
            self.assertEqual(email, "A00354773@itesm.mx")

    def test_searchByUser_AddedInList(self):
        userHandler = UserHandler.UserListHandler()
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
        userResults = userHandler.searchUserBy("Name", "Maria Gonzalez")
        for user in userResults.myList:
            name = user.getUserRecord()["Name"]
            address = user.getUserRecord()["Address"]
            phone = user.getUserRecord()["Phone"]
            email = user.getUserRecord()["Email"]
            self.assertEqual(name, "Maria Gonzalez")
            self.assertEqual(address, "Calle Jaque #210")
            self.assertEqual(phone, "4491123908")
            self.assertEqual(email, "diana.karen@gmail.com")

    def test_removeUser(self):
        userHandler = UserHandler.UserListHandler()
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


if __name__ == '__main__':
    unittest.main()