import unittest
import FileSortHandler
import CustomException
import time

class TestSortHandler(unittest.TestCase):

    def test_set_input_data(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        listaNumbers = fileSortHandler.set_input_data("my_numbers.txt")
        listaEsperada = (56, 3, 80, 65, 62, 49, 15, 78, 16, 59, 12,14,6,7,93,5,3,6565,32)
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

    def test_set_output_data(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        listaNumbers = fileSortHandler.set_input_data("my_numbers.txt")
        fileSortHandler.set_output_data("my_numbers_output.txt")
        fileSortHandler2 = FileSortHandler.FileSortHandler()
        listaNumbers2 = fileSortHandler.set_input_data("my_numbers_output.txt")
        assertResult = True
        for i in range(len(listaNumbers)):
            if listaNumbers2[i] != listaNumbers[i]:
                assertResult = False
        self.assertTrue(assertResult)

    def test_set_output_data_invalid_parameter(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        with self.assertRaises(CustomException.FileInvalidParameterError) as context:
            fileSortHandler.set_output_data(3)
        self.assertEqual(context.exception.args[0], "Invalid type of function parameter: set_output_data")



    def test_merge_sort(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        listaNumbers = fileSortHandler.set_input_data("my_numbers.txt")
        fileSortHandler.execute_sort("merge_sort")
        listaOrdenada = fileSortHandler.numbersList
        assertResult = True
        for i in range(len(listaOrdenada) - 1):
            if listaOrdenada[i + 1] >= listaOrdenada[i]:
                continue
            else:
                assertResult = False
                break
        self.assertTrue(assertResult)


    def test_quick_sort(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        listaNumbers = fileSortHandler.set_input_data("my_numbers.txt")
        fileSortHandler.execute_sort("quick_sort")
        listaOrdenada = fileSortHandler.numbersList
        assertResult = True
        i = 0
        for i in range(len(listaOrdenada) - 1):
            if listaOrdenada[i + 1] >= listaOrdenada[i]:
                continue
            else:
                assertResult = False
                break

        self.assertTrue(assertResult)

    def test_heap_sort(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        fileSortHandler.set_input_data("my_numbers.txt")
        fileSortHandler.execute_sort("heap_sort")
        listaOrdenada = fileSortHandler.numbersList
        assertResult = True
        for i in range(len(listaOrdenada)-1):
            if listaOrdenada[i+1] >= listaOrdenada[i]:
                continue
            else:
                assertResult = False
                break

        self.assertTrue(assertResult)

    def test_get_performance_date(self):
        fileSortHandler = FileSortHandler.FileSortHandler()
        fileSortHandler.set_input_data("my_numbers.txt")
        start_time = time.perf_counter()
        fileSortHandler.execute_sort("heap_sort")
        end_time = time.perf_counter()
        performanceData = fileSortHandler.get_performance_data()
        sort_start_time = performanceData["start_time"]
        sort_end_time = performanceData["end_time"]
        sort_number_of_records = performanceData["number_of_records"]
        self.assertAlmostEqual(sort_start_time, start_time, 4)
        self.assertAlmostEqual(sort_end_time, end_time, 4)
        self.assertEqual(len(fileSortHandler.numbersList), sort_number_of_records)



if __name__ == '__main__':
    unittest.main()