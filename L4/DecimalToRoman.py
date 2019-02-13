class DecimalToRoman:
    def addDigit(self, digit, t):
        result = ""
        for i in range(t):
            result = result + digit
        return result

    def addSubdigit(sef, subDigit, digit):
        result = subDigit + digit ;
        return result

    def decimalToRoman(self, number):
        result = ""
        while number > 0 and number < 3000:
            if number > 1000:
                nM = int(number/1000) #LISTO
                number = number % 1000
                result = result + self.addDigit("M",nM)
            elif number >= 500:
                if number < 900:
                    nD = int(number/500)#LISTO
                    result = result + self.addDigit("D", nD)
                    number = number % 500
                else:
                    result = result + self.addSubdigit("C","M") #LISTO
                    number = number % 100
            elif  number >= 100:
                if number < 400:
                    nD = int(number / 100) #LISTO
                    result = result + self.addDigit("C", nD)
                    number = number % 100
                else:
                    result = result + self.addSubdigit("C", "D") #LISTO
                    number = number % 100
            elif number >= 50:
                if number < 90:
                    nD = int(number / 50) #LISTO
                    result = result + self.addDigit("L", nD)
                    number = number % 50
                else:
                    result = result + self.addSubdigit("X", "C") #LISTO
                    number = number % 10
            elif number >= 10:
                if number < 40:
                    nD = int(number / 10)
                    result = result + self.addDigit("X", nD) #LISTO
                    number = number % 10
                else:
                    result = result + self.addSubdigit("X", "L")
                    number = number % 10  #LISTO
            elif number >= 5:
                if number < 9:
                    nD = int(number / 5)
                    result = result + self.addDigit("V", nD)#LISTO
                    number = number % 5
                else:
                    result = result + self.addSubdigit("I", "X")
                    number = 0 #LISTO
            elif number >= 1:
                if number < 4:
                    result = result + self.addDigit("I", number)#LISTO
                    number = 0
                else:
                    result = result + self.addSubdigit("I", "V")
                    number = 0  #LISTO

        return result

