import unittest
import DecimalToRoman
import coverage

class TestRomanNumbers(unittest.TestCase):

    def test_getMore1000(self):
        number = 1250
        romanNumbersConvert = DecimalToRoman.DecimalToRoman()
        result = romanNumbersConvert.decimalToRoman(number)
        self.assertEqual(result, "MCCL")

    def test_1000_900(self):
        number = 989
        romanNumbersConvert = DecimalToRoman.DecimalToRoman()
        result = romanNumbersConvert.decimalToRoman(number)
        self.assertEqual(result, "CMLXXXIX")

    def test_500_900(self):
        number = 736
        romanNumbersConvert = DecimalToRoman.DecimalToRoman()
        result = romanNumbersConvert.decimalToRoman(number)
        self.assertEqual(result, "DCCXXXVI")

    def test_500_400(self):
        number = 499
        romanNumbersConvert = DecimalToRoman.DecimalToRoman()
        result = romanNumbersConvert.decimalToRoman(number)
        self.assertEqual(result, "CDXCIX")

    def test_10_40(self):
        number = 43
        romanNumbersConvert = DecimalToRoman.DecimalToRoman()
        result = romanNumbersConvert.decimalToRoman(number)
        self.assertEqual(result, "XLIII")

    def test_0_10(self):
        number = 4
        romanNumbersConvert = DecimalToRoman.DecimalToRoman()
        result = romanNumbersConvert.decimalToRoman(number)
        self.assertEqual(result, "IV")

    def test_out_of_range(self):
        romanNumbersConvert = DecimalToRoman.DecimalToRoman()
        number = -1
        result = romanNumbersConvert.decimalToRoman(number)
        self.assertEqual(result, "")
        number = 4500
        result = romanNumbersConvert.decimalToRoman(number)
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main()