import unittest
import myStatistics
import coverage

class TestStatistics(unittest.TestCase):
    def test_getMean(self):
        myList = [10,4,5,6,7,45,35]
        handlerStatistics = myStatistics.myStatistics()
        result = handlerStatistics.getMean(myList)
        self.assertEqual(result, 16)

    def test_getMeanException(self):
        myList = ["10", 4, 5, 6, 7, 45, 35]
        handlerStatistics = myStatistics.myStatistics()
        self.assertRaises (Exception,  handlerStatistics.getMean(myList))

    def test_getStandarDeviation (self):
       myList = [10, 4, 5, 6, 7, 45, 35]
       handlerStatistics = myStatistics.myStatistics()
       result = handlerStatistics.getStandarDeviation(myList)
       self.assertEqual(result, 15.510365197874245)


if __name__ == '__main__':
    unittest.main()