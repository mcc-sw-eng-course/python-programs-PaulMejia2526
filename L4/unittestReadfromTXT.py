import unittest
import UserHandler


class TestloadUserRecord(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
