
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



class VirtualMachine:

    def __init__(self, func_dir, global_vars, constants, cuadruplos) -> None:
        
        self.global_vars = global_vars # CAMBIAR ESTO
        self.func_dir = func_dir
        self.cuadruplos = cuadruplos
        self.constants = constants
        self.execution_queue = []

    def initialize_vm(self):

        # Adds global virtual memory
        g_memory = self.func_dir.func_directory['program']['num_vars']
        g_temp_memory = self.func_dir.func_directory['program']['num_temp_vars']
        self.global_memory = Memory(g_memory[0], g_memory[1], g_memory[2], g_memory[3], g_temp_memory[0], g_temp_memory[1], g_temp_memory[2], g_temp_memory[3], g_temp_memory[4])
        
        # Adds global variables
        # for var, element in self.global_vars.items():
        #     type = element['type']
        #     dir = element['virtual_dir']

        #     print(type, dir)

        #     if (type == 1):
        #         self.global_memory.setValue(type, )

        # Adds memory for main and appends to execution queue
        main_memory = self.func_dir.func_directory['main']['num_vars']
        main_temp_memory = self.func_dir.func_directory['main']['num_temp_vars']
        self.execution_queue.append(Memory(main_memory[0], main_memory[1], main_memory[2], main_memory[3], main_temp_memory[0], main_temp_memory[1], main_temp_memory[2], main_temp_memory[3], main_temp_memory[4]))


    def createFunction(self):
        pass

    def checkDir(self, dir):
        pass

    
    def readQuad(self):
        pass




with open('func_dir.pickle', 'rb') as handle:
    func_dir = pickle.load(handle)

with open('constants.pickle', 'rb') as handle:
    constant_table = pickle.load(handle)

with open('global_vars.pickle', 'rb') as handle:
    global_vars = pickle.load(handle)

with open('cuadruplos.pickle', 'rb') as handle:
    cuad = pickle.load(handle)


vm = VirtualMachine(func_dir, global_vars, constant_table, cuad)

vm.initialize_vm()

vm.readQuad()