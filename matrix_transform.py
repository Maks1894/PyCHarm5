import sys
from reader import  CSVFileHandler, PickleFileHandler, TxtFileHandler, JSONFileHandler
if __name__ == "__main__":
    arguments = sys.argv[1:]
    print(arguments)
    input_file = arguments[0]
    output_file = arguments[1]
    transformations = arguments[2:]
    if input_file.endswith(".csv"):
        input_file_handler = CSVFileHandler(input_file, output_file, transformations)
    elif input_file.endswith(".pkl"):
        input_file_handler = PickleFileHandler(input_file, output_file, transformations)
    elif input_file.endswith(".txt"):
        input_file_handler = TxtFileHandler(input_file, output_file, transformations)
    elif input_file.endswith(".json"):
        input_file_handler = JSONFileHandler(input_file, output_file, transformations)

    if output_file.endswith(".csv"):
        output_file_handler = CSVFileHandler(input_file, output_file, transformations)
    elif output_file.endswith(".pkl"):
        output_file_handler = PickleFileHandler(input_file, output_file, transformations)
    elif output_file.endswith(".txt"):
        output_file_handler = TxtFileHandler(input_file, output_file, transformations)
    elif output_file.endswith(".json"):
        output_file_handler = JSONFileHandler(input_file, output_file, transformations)

    input_file_handler.read_file()
    input_file_handler.do_transformations()
    output_file_handler.data = input_file_handler.data
    output_file_handler.save_file()