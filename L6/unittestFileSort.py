import unittest
import FileSortHandler
import CustomException


class TestSortHandler(unittest.TestCase):

    def test_set_input_data(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        listaNumbers = fileSortHandler.set_input_data("my_numbers.txt")
        listaEsperada = (56, 3, 80, 65, 62, 49, 15, 78, 16, 59)
        assertResult = True
        i = 0
        for n in listaEsperada:
            if n != listaNumbers[i]:
                assertResult = False
            i = i + 1
        self.assertTrue(assertResult)

    def test_set_input_data_failed_FileInvalidInputError(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        with self.assertRaises(CustomException.FileInvalidInputError) as context:
            fileSortHandler.set_input_data("my_numbers_fail.txt")
        self.assertEqual(context.exception.args[0], "Some Value in the input is not a valid number")

    def test_set_input_data_failed_NoInputDataError(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        with self.assertRaises(CustomException.NoInputDataError) as context:
            fileSortHandler.set_input_data("my_numbers_fail_2.txt")
        self.assertEqual(context.exception.args[0], "There is no input data.")

    def test_set_input_data_failed_InputFileNotFoundError(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        with self.assertRaises(CustomException.InputFileNotFoundError) as context:
            fileSortHandler.set_input_data("my_numbers_fail_3.txt")
        self.assertEqual(context.exception.args[0], "File was not found in the system")

    def test_set_input_data_failed_FileInvalidParameterError(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        with self.assertRaises(CustomException.FileInvalidParameterError) as context:
            fileSortHandler.set_input_data(3)
        self.assertEqual(context.exception.args[0], "Invalid type of function parameter: set_input_data")

    def test_set_input_data_failed_FileInvalidParameterError(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        with self.assertRaises(CustomException.FileInvalidParameterError) as context:
            fileSortHandler.set_input_data(3)
        self.assertEqual(context.exception.args[0], "Invalid type of function parameter: set_input_data")

    def test_set_input_data_failed_FileInvalidInputError_2(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        with self.assertRaises(CustomException.FileInvalidInputError) as context:
            fileSortHandler.set_input_data("my_numbers_fail_4.txt")
        self.assertEqual(context.exception.args[0], "Some Value in the input is not a valid number")

    def test_mergeSort(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        listaNumbers = fileSortHandler.set_input_data("my_numbers.txt")
        fileSortHandler.execute_merge_sort()
        listaOrdenada = fileSortHandler.numbersList
        listaEsperada = (3, 15, 16, 49, 56, 59, 62, 65, 78, 80)
        assertResult = True
        i = 0
        for n in listaEsperada:
            if n != listaOrdenada[i]:
                assertResult = False
            i = i + 1
        self.assertTrue(assertResult)





if __name__ == '__main__':
    unittest.main()