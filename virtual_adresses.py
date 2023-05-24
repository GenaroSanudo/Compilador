# Direcciones virtuales
global_int = 0
global_float = 2000
global_string = 4000
global_dataframe = 6000

global_temp_int = 10000
global_temp_float = 12000
global_temp_bool = 14000
global_temp_string = 16000
global_temp_dataframe = 18000

local_int = 30000
local_float = 32000
local_string = 34000
local_dataframe = 36000

local_temp_int = 40000
local_temp_float = 42000
local_temp_bool = 44000
local_temp_string = 46000
local_temp_dataframe = 48000

constant_int = 50000
constant_float = 52000
constant_bool = 54000
constant_string = 56000


def getAddress(current_function, type, size = 1):
    if (current_function == 'program'):
        if (type == 1):
            global global_int
            temp = global_int
            global_int = global_int + size
            return temp
        elif (type == 2):
            global global_float
            temp = global_float
            global_float = global_float + size
            return temp
        elif (type == 4):
            global global_string
            temp = global_string
            global_string = global_string + size
            return temp
        elif (type == 5):
            global global_dataframe
            temp = global_dataframe
            global_dataframe = global_dataframe + size
            return temp
    else:   
        if (type == 1):
            global local_int
            temp = local_int
            local_int = local_int + size
            return temp
        elif (type == 2):
            global local_float
            temp = local_float
            local_float = local_float + size
            return temp
        elif (type == 4):
            global local_string
            temp = local_string
            local_string = local_string + size
            return temp
        elif (type == 5):
            global local_dataframe
            temp = local_dataframe
            local_dataframe = local_dataframe + size
            return temp
        
def getTemporalAddress(current_function, type, size = 1):
    if (current_function == 'program'):
        if (type == 1):
            global global_temp_int
            temp = global_temp_int
            global_temp_int = global_temp_int + size
            return temp
        elif (type == 2):
            global global_temp_float
            temp = global_temp_float
            global_temp_float = global_temp_float + size
            return temp
        elif(type == 3):
            global global_temp_bool
            temp = global_temp_bool
            global_temp_bool = global_temp_bool + size
            return temp
        elif (type == 4):
            global global_temp_string
            temp = global_temp_string
            global_temp_string = global_temp_string + size
            return temp
        elif (type == 5):
            global global_temp_dataframe
            temp = global_temp_dataframe
            global_temp_dataframe = global_temp_dataframe + size
            return temp
    else:   
        if (type == 1):
            global local_temp_int
            temp = local_temp_int
            local_temp_int = local_temp_int + size
            return temp
        elif (type == 2):
            global local_temp_float
            temp = local_temp_float
            local_temp_float = local_temp_float + size
            return temp
        elif(type == 3):
            global local_temp_bool
            temp = local_temp_bool
            local_temp_bool = local_temp_bool + size
            return temp
        elif (type == 4):
            global local_temp_string
            temp = local_temp_string
            local_temp_string = local_temp_string + size
            return temp
        elif (type == 5):
            global local_temp_dataframe
            temp = local_temp_dataframe
            local_temp_dataframe = local_temp_dataframe + size
            return temp