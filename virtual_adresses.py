# Direcciones virtuales
global_int = 0
global_float = 2000
global_string = 4000

global_temp_int = 6000
global_temp_float = 8000
global_temp_bool = 10000
global_temp_string = 12000

local_int = 14000
local_float = 16000
local_string = 18000

local_temp_int = 20000
local_temp_float = 22000
local_temp_bool = 24000
local_temp_string = 26000

constant_int = 28000
constant_float = 30000
constant_string = 32000

def getAddress(current_function, type):
    if (current_function == 'program'):
        if (type == 1):
            global global_int
            temp = global_int
            global_int = global_int + 1
            return temp
        elif (type == 2):
            global global_float
            temp = global_float
            global_float = global_float + 1
            return temp
        elif (type == 4):
            global global_string
            temp = global_string
            global_string = global_string + 1
            return temp
    else:   
        if (type == 1):
            global local_int
            temp = local_int
            local_int = local_int + 1
            return temp
        elif (type == 2):
            global local_float
            temp = local_float
            local_float = local_float + 1
            return temp
        elif (type == 4):
            global local_string
            temp = local_string
            local_string = local_string + 1
            return temp
        
def getTemporalAddress(current_function, type):
    if (current_function == 'program'):
        if (type == 1):
            global global_temp_int
            temp = global_temp_int
            global_temp_int = global_temp_int + 1
            return temp
        elif (type == 2):
            global global_temp_float
            temp = global_temp_float
            global_temp_float = global_temp_float + 1
            return temp
        elif(type == 3):
            global global_temp_bool
            temp = global_temp_bool
            global_temp_bool = global_temp_bool + 1
            return temp
        elif (type == 4):
            global global_temp_string
            temp = global_temp_string
            global_temp_string = global_temp_string + 1
            return temp
    else:   
        if (type == 1):
            global local_temp_int
            temp = local_temp_int
            local_temp_int = local_temp_int + 1
            return temp
        elif (type == 2):
            global local_temp_float
            temp = local_temp_float
            local_temp_float = local_temp_float + 1
            return temp
        elif(type == 3):
            global local_temp_bool
            temp = local_temp_bool
            local_temp_bool = local_temp_bool + 1
            return temp
        elif (type == 4):
            global local_temp_string
            temp = local_temp_string
            local_temp_string = local_temp_string + 1
            return temp