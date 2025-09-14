import csv
import os
from abc import ABC, abstractmethod
import pickle
import json
class FileHandler(ABC):
    def __init__(self, input_file, output_file, transformations):
        self.input_file = os.path.join('danne', input_file)
        self.output_file = os.path.join('danne', output_file)
        self.transformations = transformations
        self.data = None

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_file(self):
        pass


    def do_transformations(self):
        for transformation in self.transformations:
            transformation_list = transformation.split(",")
            col = int(transformation_list[0])
            row = int (transformation_list[1])
            value = transformation_list[2]
            self.data[row][col] = value
        return self.data

class CSVFileHandler(FileHandler):
    def read_file(self):
        with open(self.input_file) as file:
            reader = csv.reader(file)
            matrix = []
            for row in reader:
                temp_row = []
                for item in row:
                    temp_row.append(item)
                matrix.append(temp_row)
        self.data = matrix


    def save_file(self):
        with open(self.output_file, mode="w", newline='') as file:
            writer = csv.writer(file)
            for row in self.data:
                writer.writerow(row)

class PickleFileHandler(FileHandler):
    def read_file(self):
        with open(self.input_file, mode="rb") as file:
            self.data = pickle.load(file)

    def save_file(self):
        with open(self.output_file, mode="wb") as file:
            file.write(pickle.dumps(self.data))
class TxtFileHandler(FileHandler):
    def read_file(self):
        with open(self.input_file) as file:
           read = file.readlines()
           matrix = []
           for line in read:
               row = line.strip().split(',')
               temp_row = []
               for item in row:
                    temp_row.append(item)
               matrix.append(temp_row)
        self.data = matrix

    def save_file(self):
        with open(self.output_file, 'w') as file:
            for row in self.data:
                string_row = [str(item) for item in row]
                file.write(','.join(string_row)+'\n')


class JSONFileHandler(FileHandler):
    def read_file(self):
        with open(self.input_file) as file:
            self.data = json.load(file)

    def save_file(self):
        with open(self.output_file, 'w') as file:
            json.dump(self.data, file,  indent=1)
