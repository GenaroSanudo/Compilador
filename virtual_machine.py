
import pickle
from function_directory import Directory

class Memory:

    def __init__(self, int_size, float_size, string_size, dataF_size, t_int_size, t_float_size, t_bool_size, t_string_size, t_dataF_size, params = None) -> None:
        
        self.local_int = [None] * int_size
        self.local_float = [None] * float_size
        self.local_string = [None] * string_size
        self.local_dataF = [None] * dataF_size

        self.temp_int = [None] * t_int_size
        self.temp_float = [None] * t_float_size
        self.temp_bool = [None] * t_bool_size
        self.temp_string = [None] * t_string_size
        self.temp_dataF = [None] * t_dataF_size

        self.params = params
        self.param_int = 0
        self.param_float = 0

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

    def addParam(self, k, value):

        type = self.params[k]

        if (type == 1):
            self.setValue(1, value, self.param_int)
            self.param_int += 1
        elif(type == 2):
            self.setValue(2, value, self.param_float)
            self.param_float += 1


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

    def createFunction(self, target):
        func_memory = self.func_dir.func_directory[target]['num_vars']
        func_temp_memory = self.func_dir.func_directory[target]['num_temp_vars']
        params = self.func_dir.func_directory[target]['params']
        return(Memory(func_memory[0], func_memory[1], func_memory[2], func_memory[3], func_temp_memory[0], func_temp_memory[1], func_temp_memory[2], func_temp_memory[3], func_temp_memory[4], params))

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
        elif ((dir >= 56000) and (dir < 58000)):
            pass

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

    def less_than(self, l_operand, r_operand, target):
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

            result = l_value < r_value

            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)

    def less_equal(self, l_operand, r_operand, target):
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

            result = l_value <= r_value

            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)

    def is_equal(self, l_operand, r_operand, target):
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

            result = l_value == r_value

            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)

    def greater_than(self, l_operand, r_operand, target):
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

            result = l_value > r_value

            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)
    
    def greater_equal(self, l_operand, r_operand, target):
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

            result = l_value >= r_value

            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)

    def not_equal(self, l_operand, r_operand, target):
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

            result = l_value != r_value

            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)

    def and_func(self, l_operand, r_operand, target):
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

            result = l_value and r_value

            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)

    def or_func(self, l_operand, r_operand, target):
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

            result = l_value or r_value

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
    
    def read(self, target):
        temp, local, type, dir, constant = self.checkDir(target)

        if (type == 1):
            try:
                value = int(input("Enter an integer: "))
            except:
                raise Exception("Value entered is not integer")
        elif (type == 2):
            try:
                value = float(input("Enter an float: "))
            except:
                raise Exception("Value entered is not valid")
        else:
            raise Exception ("Invalid type variable in read statement")
        
        if (local):
            self.execution_queue[-1].setValue(type, value, dir, temp)
        else:
            self.global_memory.setValue(type, value, dir, temp)



    def readQuad(self):
        ip = 0
        ip_list = []


        while (ip < len(self.cuadruplos)):
            op = self.cuadruplos[ip].operator
            l_operand = self.cuadruplos[ip].l_operand
            r_operand = self.cuadruplos[ip].r_operand
            target = self.cuadruplos[ip].target

            # print(ip)

            if (op == 10):
                self.suma(l_operand, r_operand, target)
            elif (op == 15):
                self.resta(l_operand, r_operand, target)
            elif (op == 20):
                self.mult(l_operand, r_operand, target)
            elif (op == 25):
                self.divide(l_operand, r_operand, target)
            elif (op == 30):
                self.less_than(l_operand, r_operand, target)
            elif (op == 35):
                self.less_equal(l_operand, r_operand, target)
            elif (op == 40):
                self.is_equal(l_operand, r_operand, target)
            elif (op == 45):
                self.greater_than(l_operand, r_operand, target)
            elif (op == 50):
                self.greater_equal(l_operand, r_operand, target)
            elif (op == 55):
                self.not_equal(l_operand, r_operand, target)
            elif (op == 60):
                self.asigna(l_operand, target)
                print("Valor", self.execution_queue[-1].getValue(1, 0, True))
            elif (op == 65):
                self.and_func(l_operand, r_operand, target)
            elif (op == 70):
                self.or_func(l_operand, r_operand, target)
            elif (op == 100):
                self.read(target)
            elif (op == 105):
                self.write(target) 
            elif (op == 110):
                temp, local, type, dir, constant = self.checkDir(target)
                value = self.execution_queue[-1].getValue(type, dir, temp)

                temp, local, type, dir, constant = self.checkDir(l_operand)
                self.global_memory.setValue(type, value, dir, temp)

                self.execution_queue.pop()
                ip = ip_list.pop()
                continue
            elif (op == 115):
                temp, local, type, dir, constant = self.checkDir(l_operand)
                if (constant):
                    value = self.constants[dir]['value']
                elif (local):
                    value = self.execution_queue[-1].getValue(type, dir, temp)
                else:
                    value = self.global_memory.getValue(type, dir, temp)
                if ((value < r_operand) and (value >= target)):
                    raise Exception ("Out of bounds")
                    

            elif (op == 130):
                #GOTO
                ip = target
                continue
            elif (op == 135):
                temp, local, type, dir, constant = self.checkDir(l_operand)

                if (local):
                    value = self.execution_queue[-1].getValue(type, dir, temp)
                else:
                    value = self.global_memory.getValue(type, dir, temp)
                
                if (value == False):
                    ip = target
                    continue
            elif (op == 140):
                temp, local, type, dir, constant = self.checkDir(l_operand)

                if (local):
                    value = self.execution_queue[-1].getValue(type, dir, temp)
                else:
                    value = self.global_memory.getValue(type, dir, temp)
                
                if (value):
                    ip = target
                    continue
            elif (op == 145):
                if (len(self.execution_queue) > 1):
                    ip = ip_list.pop()
                elif(len(self.execution_queue) == 0):
                    ip += 1
                    break
                self.execution_queue.pop()
                continue
            elif (op == 150):
                nextFunctionMem = self.createFunction(target)
            elif (op == 155):
                temp, local, type, dir, constant = self.checkDir(l_operand)
                if (constant):
                    value = self.constants[dir]['value']
                elif (local):
                    value = self.execution_queue[-1].getValue(type, dir, temp)
                else:
                    value = self.global_memory.getValue(type, dir, temp)
                
                nextFunctionMem.addParam(r_operand, value)
            elif (op == 160):
                self.execution_queue.append(nextFunctionMem)
                quad = self.func_dir.func_directory[l_operand]['quad_counter']
                ip_list.append(ip + 1)
                ip = quad
                continue
                
            print(ip)
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
