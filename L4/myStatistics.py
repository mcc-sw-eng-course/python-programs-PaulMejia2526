import math


class myStatistics:

    def getVariance(self, list):
        sum = 0
        X = self.getMean(list)
        n = 0
        for ni in list:
            try:
                n = n + 1
                vi = (X - ni) * (X - ni)
                sum = sum + vi

            except:
                return

        result = sum / n
        return result

    def getStandarDeviation(self, list):
        sDev = 0
        try:
            variance = self.getVariance(list)

            sDev = math.sqrt(variance)
        except:
            return
        return sDev

    def getMean(self, list):
        sum = 0
        n = 0
        for ni in list:
            try:
                n = n + 1
                sum = sum + ni
            except:
                return
        result = sum / n
        return result

    def getMedian(self,list):
        list.sort()
        n = len(list)
        if n % 2 == 0 and n >= 2:
            i = int(n / 2)
            median = (list[i] + list[i - 1]) / 2
        elif n % 2 == 1 and n >= 2:
            median = list[int(n / 2)]
        elif n == 1:
            median = list[n-1]
        else:
            return
        return median

    def getNquartil(self, n, list):
        list.sort()

        l = len(list)
        odd = l % 2 == 1
        quartil = 0
        if n < 1 or n > 3:
            return
        else:
            qi = ((l + 1) * n) / 4
            if not qi.is_integer():
                i = int(qi) - 1
                d = qi - int(qi)
                qi = list[i] + d * (list[i+1] - list[i])

            else:
                qi = list[int(qi-1)]

        return qi

    def getNpercentil(self, n, list):
        list.sort()
        l = len(list)
        odd = l % 2 == 1
        quartil = 0
        if n < 1 or n > 99:
            return
        else:
            pi = ((l + 1) * n) / 100
            if not pi.is_integer():
                i = int(pi) - 1
                d = pi - int(pi)
                pi = list[i] + d * (list[i + 1] - list[i])

            else:
                pi = list[int(pi - 1)]


        return pi