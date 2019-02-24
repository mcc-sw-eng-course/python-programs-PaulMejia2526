import FileSortHandler
import CustomException

try:
    fileSortHandler = FileSortHandler.FileSortHandler()
    fileSortHandler.file_random_input_generator("my_numbers.txt", 50)                                                   #genera 50 numeros random en archivo my_numbers.txt
    fileSortHandler.set_input_data(file_path_name="my_numbers.txt")                                                     #lee archivo my_numbers.txt
    fileSortHandler.execute_merge_sort()                                                                                #ordena la lista de numeros creada en metodo set_input_data
    fileSortHandler.set_output_data(file_path_name="my_numbers_output.txt")                                             #escribe la lista ordenada en archivo "my_numbers_output.txt"

except (CustomException.InputFileNotFoundError, CustomException.FileInvalidInputError, CustomException.FileInvalidParameterError,
        CustomException.OutputFileCreationError, CustomException.NoOutputDataError, CustomException.NoInputDataError) as error:     #cacha excepciones generadas explicitamente en los metodos
    print ("The following error has been raised: ")
    print ("\t" + error.args[0])
except Exception as error:
    print("An unknown error has ocurred")                                                                               #cacha cualquier otra excepcion
    print ("\t" + error.args[0])
