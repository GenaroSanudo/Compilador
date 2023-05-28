
import pickle
from function_directory import Directory

class Memory:

    def __init__(self, int_size, float_size, string_size, dataF_size, t_int_size, t_float_size, t_bool_size, t_string_size, t_dataF_size) -> None:
        
        self.local_int = [None] * int_size
        self.local_float = [None] * float_size
        self.local_string = [None] * string_size
        self.local_dataF = [None] * dataF_size

        self.temp_int = [None] * t_int_size
        self.temp_float = [None] * t_float_size
        self.temp_bool = [None] * t_bool_size
        self.temp_string = [None] * t_string_size
        self.temp_dataF = [None] * t_dataF_size

    def setValue(self, type, value, dir):

        if (type == 1):
            self.local_int[dir] = value
        elif (type == 2):
            self.local_float[dir] = value
        elif (type == 4):
            self.local_string[dir] = value
        elif (type == 5):
            self.local_dataF[dir] = value

    def setTempValue(self, type, value, dir):

        if (type == 1):
            self.temp_int[dir] = value
        elif (type == 2):
            self.temp_float[dir] = value
        elif (type == 3):
            self.temp_bool[dir] = value
        elif (type == 4):
            self.temp_string[dir] = value
        elif (type == 5):
            self.temp_dataF[dir] = value

    def getValue(self, type, dir):

        if (type == 1):
            return  self.local_int[dir]
        elif (type == 2):
            return  self.local_float[dir]
        elif (type == 4):
            return  self.local_string[dir]
        elif (type == 5):
            return  self.local_dataF[dir]

    def getTempValue(self, type, dir):
        
        if (type == 1):
            return self.temp_int[dir]
        elif (type == 2):
            return self.temp_float[dir]
        elif (type == 3):
            return self.temp_bool[dir]
        elif (type == 4):
            return self.temp_string[dir]
        elif (type == 5):
            return self.temp_dataF[dir]

