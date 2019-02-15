import unittest
import myPowerList


class TestmyPowerList(unittest.TestCase):

    def test_readFromTextFile(self):
        loadedUsers = myPowerList.myPowerList()
        filePath = "lista.txt"
        Lista = len(loadedUsers.readFromTextFile(filePath))
        self.assertEqual(Lista, 5)







if __name__ == '__main__':
    unittest.main()
