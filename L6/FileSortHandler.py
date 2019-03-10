import CustomException
import os
import random
import time

class FileSortHandler:

    MERGE_SORT = "merge_sort"
    QUICK_SORT = "quick_sort"
    HEAP_SORT = "heap_sort"

    def __init__(self):
        self.file = None                                                                                                #se inicializa la variable file y lista como vacias cuando se crea el objeto
        self.numbersList = list()
        self.performance_data = {"number_of_records" : 0,
                                 "time_consumed" : 0,
                                 "start_time" : 0,
                                 "end_time" : 0}
    def set_input_data(self, file_path_name):                                                                           #el metodo set_input_data(file_path_name): recibe un parametro tipo string donde se especifica la ruta del archivo a leer
                                                                                                                        #si no ocurre ningun error, devuelve una lista de numeros que sera la que se va a utilizar al momento de ordenar
        if (type(file_path_name) == str):

            self.file = FileSortHandler.load_file(file_path_name)                                                       #abrir el archivo usando FileSortHandler.load_file,
            if self.file != None:                                                                                       #CustomException.InputFileNotFoundError, si no, sigue con el proceso,
                numberList = list()                                                                                     #creamos numberList que es una lista temporal
                fileLines = self.file.readlines()
                self.file.close()
                #leer las lineas del archivo
                if(len(fileLines) > 0):
                    for line in fileLines:                                                                              #recorrer las lineas del archivo
                        if(len(line) > 0):
                            values  = line.split(",")                                                                   #por cada linea separar con "," para seguir con el formato csv y guardar en lista values
                            for value in values:
                                if (value != ""):
                                    numeric_value = FileSortHandler.convert_float(value)                                #revisar que value no sea vacio y tratar de convertir a numero
                                    if (numeric_value != None):
                                        numberList.append(numeric_value)                                                #si es diferente de None significa que no hubo errores mientras se convertia a numero, lo agregamos a la lista temporal
                                    else:
                                        raise CustomException.FileInvalidInputError
                                else:
                                    raise CustomException.FileInvalidInputError                                         #si hubo error mientras se convertia, lanzamos excepcion  CustomException.FileInvalidInputError

                    self.numbersList = numberList                                                                       #si no ocurrio ningun error pasamos lista temporal numberList, a la lista de la clase self.numbersList
                else:
                    raise CustomException.NoInputDataError                                                              #si no hay lineas en el archivo, lanzamos excepcion  CustomException.NoInputDataError

            else:
                raise CustomException.InputFileNotFoundError
        else:
            raise CustomException.FileInvalidParameterError("set_input_data")                                           #si el typo de parametro no es del tipo esperado, entonces lanza excepcion CustomException.FileInvalidParameterError
        return self.numbersList

    def set_output_data(self,file_path_name):                                                                           #metodo que escribe un archivo con la lista de numbers ordenados en formato csv separado por ",", recibe como parametro
        if (type(file_path_name) == str):                                                                               #file_path_name que es el nombre del archivo donde se va a escribir la lista
            if len(self.numbersList) > 0:
                created_file = FileSortHandler.create_file(file_path_name)
                if created_file != None:
                    joinner = ","
                    numbers = joinner.join(map(str,self.numbersList))                                                   #une la lista de numeros y las escribe en el archivo especificado
                    created_file.write(numbers)
                    created_file.close()
                else:
                    raise CustomException.OutputFileCreationError                                                       #si un error ocurre durante la creacion del archivo, lanza excepcion OutputFileCreationError
            else:
                raise CustomException.NoOutputDataError                                                                 #si la lista esta vacia lanza excepcion CustomException.NoOutputDataError

        else:
            raise CustomException.FileInvalidParameterError("set_output_data")                                          #si el parametro no es tipo str lanza excepcion CustomException.FileInvalidParameterError

    def execute_merge_sort(alist):                                                                                               #funcion que recibe una lista e implementa un algoritmo de ordenamiento merge sort (obtenido de internet)

        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            FileSortHandler.execute_merge_sort(lefthalf)
            FileSortHandler.execute_merge_sort(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i + 1
                else:
                    alist[k] = righthalf[j]
                    j = j + 1
                k = k + 1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i = i + 1
                k = k + 1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j = j + 1
                k = k + 1


    def partition(arr,low,high):
        i = ( low-1 )
        pivot = arr[high]
        for j in range(low , high):
            if arr[j] <= pivot:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return ( i+1 )

    def execute_quick_sort(arr, low, high):
        if low < high:
            pi = FileSortHandler.partition(arr, low, high)
            FileSortHandler.execute_quick_sort(arr, low, pi - 1)
            FileSortHandler.execute_quick_sort(arr, pi + 1, high)

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap
            FileSortHandler.heapify(arr, n, largest)

    def execute_quick_sort(arr, low, high):
        if low < high:
            pi = FileSortHandler.partition(arr, low, high)
            FileSortHandler.execute_quick_sort(arr, low, pi - 1)
            FileSortHandler.execute_quick_sort(arr, pi + 1, high)

    def execute_heap_sort(arr):
        n = len(arr)
        for i in range(n, -1, -1):
            FileSortHandler.heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            FileSortHandler.heapify(arr, i, 0)

    def execute_sort (self, algorithm):
        #funcion que llama al algortimo de ordenamiento y envia como parametro la lista de la clase  self.numbersList
        if(len(self.numbersList) > 0):
            start_time = time.perf_counter()
            if algorithm == FileSortHandler.MERGE_SORT:
                FileSortHandler.execute_merge_sort(self.numbersList)
            elif algorithm == FileSortHandler.QUICK_SORT:
                FileSortHandler.execute_quick_sort(self.numbersList, 0, len(self.numbersList) - 1)
            elif algorithm == FileSortHandler.HEAP_SORT:
                FileSortHandler.execute_heap_sort(self.numbersList)
            end_time = time.perf_counter()
            self.performance_data["start_time"] = start_time
            self.performance_data["end_time"] = end_time
            self.performance_data["time_consumed"] =  end_time  -  start_time
            self.performance_data["number_of_records"] = len(self.numbersList)

        else:
            raise CustomException.NoInputDataError

    def get_performance_data(self):
        return self.performance_data

    def file_random_input_generator(self, file_path_name, nSize):                                                       #funcion que genera un archivo con numeros random, recibe como parametros la ruta del archivo y el numero de numeros a generar
        myFile = FileSortHandler.create_file(file_path_name)
        if type(file_path_name) == str and type(nSize) == int:
            if myFile != None:

                randomNumbersList = list()
                joinner = ","

                for n in range(nSize):
                    randNum = random.randint(0, 100) + 1
                    randomNumbersList.append(randNum)

                randonNumbers = joinner.join(map(str,randomNumbersList))
                myFile.write(randonNumbers)
                myFile.close()
            else:
                raise CustomException.OutputFileCreationError
        else:
            raise CustomException.FileInvalidParameterError("file_random_input_generator")


    #   These methods can be used for general purposes --- START :
    def convert_float( input):
        try:
            num = float(input)                                                                                          # Trata de convertir el parametro de entrada a variable tipo float
        except ValueError:
            return None                                                                                                 # si ocurre una excepcion durante la conversion devuelve None(valor nulo)
        return num                                                                                                      # si no, devuelve el numero en tipo float

    def create_file(file_path_name):
        try:
            myCreatedFile = open(file_path_name,"w")
            return myCreatedFile
        except Exception:
            return None

    def load_file(file_path_name):
        try:
            exists = os.path.exists(file_path_name)
            if exists:
                myFile = open(file_path_name, 'r')
                return myFile
            else:
                return None
        except Exception:
            return None
                                                                                                                        #En general, dentro de estos metodos, si ocurre una excepcion mientras se ejecuta algun metodo de
                                                                                                                        #python, devuelven None, si no devuelven la variable resultante de la conversion del metodo
    #   These methods can be used for general purposes --- END :