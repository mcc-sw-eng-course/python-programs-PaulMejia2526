#modulo que define todas las class para las Excepciones que se pueden generar en los metodos

class FileSortError(Exception):
    """Base error for Input file"""
    pass

class InputFileNotFoundError(FileSortError):
    """Error raised when input file not exist"""
    def __init__(self):
        Exception.__init__(self, "File was not found in the system")

    pass

class FileInvalidInputError(FileSortError):
    """Error raised when input is not a valid number"""
    def __init__(self):
        Exception.__init__(self, "Some Value in the input is not a valid number")

    pass

class FileInvalidParameterError(FileSortError):
    """Error raised when input is not a valid number"""
    def __init__(self, method):
        Exception.__init__(self, "Invalid type of function parameter: " + method)

    pass

class OutputFileCreationError(FileSortError):
    def __init__(self):
        Exception.__init__(self, "Output file could not be created")

    pass

class NoOutputDataError(FileSortError):
    def __init__(self):
        Exception.__init__(self, "There is no output data.")

    pass
class NoInputDataError(FileSortError):
    def __init__(self):
        Exception.__init__(self, "There is no input data.")

    pass
