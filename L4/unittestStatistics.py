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

    def test_getMedian_even(self):
        myList = [ 4, 5, 6, 7,10, 45]
        handlerStatistics = myStatistics.myStatistics()
        result = handlerStatistics.getMedian(myList)
        self.assertEqual(result, 6.5)

    def test_getMedian_odd(self):
        myList = [ 4, 35, 5, 6, 7,10, 45]
        handlerStatistics = myStatistics.myStatistics()
        result = handlerStatistics.getMedian(myList)
        self.assertEqual(result, 7)

    def test_getMedian_one(self):
        myList = [4]
        handlerStatistics = myStatistics.myStatistics()
        result = handlerStatistics.getMedian(myList)
        self.assertEqual(result, 4)

    def test_getMedian_empty(self):
        myList = []
        handlerStatistics = myStatistics.myStatistics()
        result = handlerStatistics.getMedian(myList)
        self.assertIsNone(result)

    def test_getNQuartil_noQ(self):
        myList = [ 4, 35, 5, 6, 7,10, 45, 34,32, 79, 4, 35, 5, 6, 7,10, 45, 34,60, 79, 4, 35, 5, 56, 7,40, 65, 43,32, 79]
        handlerStatistics = myStatistics.myStatistics()
        n = 1
        result = handlerStatistics.getNquartil(n, myList)
        self.assertEquals(result,6)

    def test_getNQuartil_Qint(self):
        myList = [56, 7,40, 65, 43,32, 79]
        handlerStatistics = myStatistics.myStatistics()
        n = 3
        result = handlerStatistics.getNquartil(n, myList)
        self.assertEquals(result,65)

    def test_getNPercentil_PNoInt(self):
        myList = [4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 37, 120, 245, 34, 32, 79, 4, 35, 5, 643, 7, 10, 45,
                  34, 32, 79, 4, 35, 5, 6, 7, 10, 45, 34, 32, 749, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7,
                  10, 45, 10, 45, 34, 32, 79,
                  35, 678, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 7, 10,
                  45, 34, 32, 79, 47, 10, 45, 34, 32, 79, 4, 35, 5, 790, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35,
                  5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79]
        handlerStatistics = myStatistics.myStatistics()
        n = 150
        result = handlerStatistics.getNpercentil(n, myList)
        self.assertIsNone(result)

    def test_getNPercentil_PInt(self):
        myList = [4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 37, 120, 245, 34, 32, 79,4, 35, 5, 643, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7, 10, 45, 34, 32, 749, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79,
                 35, 678, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79,4, 35, 5, 6, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 7, 10, 45, 34, 32, 79,4, 35, 5, 6, 7, 10, 45, 34, 32, 79,4, 35, 5, 6, 7, 10, 45, 34, 32, 79,4, 35, 5, 6, 7, 10, 45, 34, 32, 79,5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 27, 150, 455, 34, 32, 79, 4, 35, 5, 6, 75, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7, 45, 34, 32, 790, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79]
        handlerStatistics = myStatistics.myStatistics()
        n = 75
        result = handlerStatistics.getNpercentil(n, myList)
        self.assertEquals(result, 35)

    def test_getNPercentil_PNoInt(self):
        myList = [4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 37, 120, 245, 34, 32, 79, 4, 35, 5, 643, 7, 10, 45,
                  34, 32, 79, 4, 35, 5, 6, 7, 10, 45, 34, 32, 749, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7,
                  10, 45, 10, 45, 34, 32, 79,
                  35, 678, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 7, 10,
                  45, 34, 32, 79, 47, 10, 45, 34, 32, 79, 4, 35, 5, 790, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79, 4, 35,
                  5, 6, 7, 10, 45, 34, 32, 79, 4, 35, 5, 6, 7, 10, 45, 34, 32, 79]
        handlerStatistics = myStatistics.myStatistics()
        n = 50
        result = handlerStatistics.getNpercentil(n, myList)
        self.assertEquals(result, 32)

if __name__ == '__main__':
    unittest.main()