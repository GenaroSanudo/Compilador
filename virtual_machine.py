
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

    def setValue(self, type, value, dir, temp = False):

        if (temp):
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
        else:
            if (type == 1):
                self.local_int[dir] = value
            elif (type == 2):
                self.local_float[dir] = value
            elif (type == 4):
                self.local_string[dir] = value
            elif (type == 5):
                self.local_dataF[dir] = value

    def getValue(self, type, dir, temp):

        if (temp):
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
        else:
            if (type == 1):
                return  self.local_int[dir]
            elif (type == 2):
                return  self.local_float[dir]
            elif (type == 4):
                return  self.local_string[dir]
            elif (type == 5):
                return  self.local_dataF[dir]
        return None



class VirtualMachine:

    def __init__(self, func_dir, global_vars, constants, cuadruplos) -> None:
        
        self.global_vars = global_vars # CAMBIAR ESTO
        self.func_dir = func_dir
        self.cuadruplos = cuadruplos
        self.constants = constants
        self.execution_queue = []
        # self.execution_queue = [Memory()]

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

        # Change constant table
        self.changeConstantTalbe()


    def changeConstantTalbe(self):

        newTable = dict()

        for key, element in self.constants.items():
            type = element['type']

            if (type == 1):
                key = int(key)
            elif (type == 2):
                key = float(key)
            else:
                key = key
            
            newTable[element['virtual_dir']] = {'type' : type, 'value': key}

        self.constants = newTable

    def createFunction(self):
        pass

    def checkDir(self, dir):
        
        if ((dir >= 0) and (dir < 8000 )):
            temp = False
            local = False
            if (dir < 2000):
                type = 1
            elif (dir < 4000):
                type = 2
                dir = dir - 2000
            elif (dir < 6000):
                type = 4
                dir = dir - 4000
            elif (dir < 8000):
                type = 5
                dir = dir - 6000
            return temp, local, type, dir, False
        
        elif ((dir >= 10000) and (dir < 20000 )):
            temp = True
            local = False
            if (dir < 12000):
                type = 1
                dir = dir - 10000
            elif (dir < 14000):
                type = 2
                dir = dir - 12000
            elif (dir < 16000):
                type = 3
                dir = dir - 14000
            elif (dir < 18000):
                type = 4
                dir = dir - 16000
            elif (dir < 2000):
                type = 5
                dir = dir - 18000
            return temp, local, type, dir, False
        
        elif ((dir >= 30000) and (dir < 38000 )):
            temp = False
            local = True

            if (dir < 32000):
                type = 1
                dir = dir - 30000
            elif (dir < 34000):
                type = 2
                dir = dir - 32000
            elif (dir < 36000):
                type = 4
                dir = dir - 34000
            elif (dir < 38000):
                type = 5
                dir = dir -36000
            return temp, local, type, dir, False
        
        elif ((dir >= 40000) and (dir < 50000)):
            temp = True
            local = True

            if (dir < 42000):
                type = 1
                dir = dir - 40000
            elif (dir < 44000):
                type = 2
                dir = dir - 42000
            elif (dir < 46000):
                type = 3
                dir = dir - 44000
            elif (dir < 48000):
                type = 4
                dir = dir - 46000
            elif (dir < 50000):
                type = 5
                dir = dir - 48000

            return temp, local, type, dir, False
        
        elif ((dir >= 50000) and (dir < 56000)):
            
            return False, False, None, dir, True

    def suma(self, l_operand, r_operand, target):
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
        temp, local, type, dir, constant = self.checkDir(target)

        if (l_constant and r_constant):
            # ambas constantes
            l_value = self.constants[l_dir]['value']
            r_value = self.constants[r_dir]['value']
        
        elif (l_constant):

            l_value = self.constants[l_dir]['value']

            if (r_local):
                r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
            else:
                r_value = self.global_memory.getValue(r_type, r_dir, r_temp)
        
        elif (l_local):
            l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

            if (r_constant):
                r_value = self.constants[r_dir]['value']
            elif (r_local):
                r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
            else:
                r_value = self.global_memory.getValue(r_type, r_dir, r_temp)
        else:
            l_value = self.global_memory.getValue(l_type, l_dir, l_temp)
            if (r_constant):
                r_value = self.constants[r_dir]['value']
            elif (r_local):
                r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
            else:
                r_value = self.global_memory.getValue(r_type, r_dir, r_temp)

        result = l_value + r_value

        if (local):
            self.execution_queue[-1].setValue(type, result, dir, temp)
        else:
            self.global_memory.setValue(type, result, dir, temp)

    def resta(self, l_operand, r_operand, target):
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
        temp, local, type, dir, constant = self.checkDir(target)

        if (l_constant and r_constant):
            # ambas constantes
            l_value = self.constants[l_dir]['value']
            r_value = self.constants[r_dir]['value']
        
        elif (l_constant):

            l_value = self.constants[l_dir]['value']

            if (r_local):
                r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
            else:
                r_value = self.global_memory.getValue(r_type, r_dir, r_temp)
        
        elif (l_local):
            l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

            if (r_constant):
                r_value = self.constants[r_dir]['value']
            elif (r_local):
                r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
            else:
                r_value = self.global_memory.getValue(r_type, r_dir, r_temp)
        else:
            l_value = self.global_memory.getValue(l_type, l_dir, l_temp)
            if (r_constant):
                r_value = self.constants[r_dir]['value']
            elif (r_local):
                r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
            else:
                r_value = self.global_memory.getValue(r_type, r_dir, r_temp)

        result = l_value - r_value

        if (local):
            self.execution_queue[-1].setValue(type, result, dir, temp)
        else:
            self.global_memory.setValue(type, result, dir, temp)

    def mult(self, l_operand, r_operand, target):
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
        temp, local, type, dir, constant = self.checkDir(target)

        if (l_constant and r_constant):
            # ambas constantes
            l_value = self.constants[l_dir]['value']
            r_value = self.constants[r_dir]['value']
        
        elif (l_constant):

            l_value = self.constants[l_dir]['value']

            if (r_local):
                r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
            else:
                r_value = self.global_memory.getValue(r_type, r_dir, r_temp)
        
        elif (l_local):
            l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

            if (r_constant):
                r_value = self.constants[r_dir]['value']
            elif (r_local):
                r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
            else:
                r_value = self.global_memory.getValue(r_type, r_dir, r_temp)
        else:
            l_value = self.global_memory.getValue(l_type, l_dir, l_temp)
            if (r_constant):
                r_value = self.constants[r_dir]['value']
            elif (r_local):
                r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
            else:
                r_value = self.global_memory.getValue(r_type, r_dir, r_temp)

        result = l_value * r_value

        if (local):
            self.execution_queue[-1].setValue(type, result, dir, temp)
        else:
            self.global_memory.setValue(type, result, dir, temp)

    def divide(self, l_operand, r_operand, target):
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)

            if (l_constant and r_constant):
                # ambas constantes
                l_value = self.constants[l_dir]['value']
                r_value = self.constants[r_dir]['value']
            
            elif (l_constant):

                l_value = self.constants[l_dir]['value']

                if (r_local):
                    r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                else:
                    r_value = self.global_memory.getValue(r_type, r_dir, r_temp)
            
            elif (l_local):
                l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                else:
                    r_value = self.global_memory.getValue(r_type, r_dir, r_temp)
            else:
                l_value = self.global_memory.getValue(l_type, l_dir, l_temp)
                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    r_value = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                else:
                    r_value = self.global_memory.getValue(r_type, r_dir, r_temp)

            result = l_value / r_value

            if (type == 1):
                result = round(result)

            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)

    

    def asigna(self, l_operand, target):

        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        temp, local, type, dir, constant = self.checkDir(target)

        if (l_constant):
            # Aqui entra si son constantes
            result = self.constants[l_dir]['value']
            l_type = self.constants[l_dir]['type']
        else:
            if (l_local):
                result = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
            else:
                #AQUI SI ES GLOBAL
                result = self.global_memory.getValue(l_type, l_dir, l_temp)
                
        if (result == None):
            raise Exception ("Valor asignado no ha sido especificado")
                
        if (local):
            self.execution_queue[-1].setValue(type, result, dir, temp)
        else:
            self.global_memory.setValue(type, result, dir, temp)
                 

    def write(self, target):
        temp, local, type, dir, constant = self.checkDir(target)

        if (constant):
            value = self.constants[dir]['value']
        elif (local):
            value = self.execution_queue[-1].getValue(type, dir, temp)
        else:
            value = self.global_memory.getValue(type, dir, temp)
        
        print(value)


    def readQuad(self):
        ip = 0

        while (ip < len(self.cuadruplos)):
            op = self.cuadruplos[ip].operator
            l_operand = self.cuadruplos[ip].l_operand
            r_operand = self.cuadruplos[ip].r_operand
            target = self.cuadruplos[ip].target

            if (op == 10):
                self.suma(l_operand, r_operand, target)
            elif (op == 15):
                self.resta(l_operand, r_operand, target)
            elif (op == 20):
                self.mult(l_operand, r_operand, target)
            elif (op == 25):
                self.divide(l_operand, r_operand, target)
            elif (op == 30):
                pass
            elif (op == 35):
                pass
            elif (op == 40):
                pass
            elif (op == 45):
                pass
            elif (op == 50):
                pass
            elif (op == 55):
                pass
            elif (op == 60):
                self.asigna(l_operand, target)
            elif (op == 105):
                self.write(target) 
            ip += 1



with open("parser_1.py") as f:
    exec(f.read())

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
