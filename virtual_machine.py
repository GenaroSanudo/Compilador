
# Se importan las librerias necesarias
import pickle
from Components.function_directory import Directory
import parser_1 as parser

# Estadistica
from sklearn.linear_model import LinearRegression

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Se crea el objeto de tipo memoria
class Memory:

    def __init__(self, int_size, float_size, string_size, dataF_size, t_int_size, t_float_size, t_bool_size, t_string_size, t_dataF_size, t_pointer_size, params = None) -> None:
        
        # Se generan listas para cada tipo de variable utilizada en compilacion

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

        self.temp_pointer = [None] * t_pointer_size
    # Funcion setValue recibe la direccion y tipo de variable y se encarga de poner el valor en el espacio indicado de la lista indicada
    def setValue(self, type, value, dir, temp = False):

        if (type == 6):
            self.temp_pointer[dir] = value

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
    # Esta funcion recibe el tipo y la direccion y regresa el valor que se encuentra en esa casilla de la lista
    def getValue(self, type, dir, temp):

        if (type == 6):
            return self.temp_pointer[dir]

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
    # Agrega un parametro a la lista de variables correspondiente
    def addParam(self, k, value):

        type = self.params[k]

        if (type == 1):
            self.setValue(1, value, self.param_int)
            self.param_int += 1
        elif(type == 2):
            self.setValue(2, value, self.param_float)
            self.param_float += 1

# Se genera la clase de tipo VirtualMachine
class VirtualMachine:
    # Se inicializa la clase con los valores que se cargaron a traves de pickle
    def __init__(self, func_dir, global_vars, constants, cuadruplos) -> None:
        
        self.global_vars = global_vars 
        self.func_dir = func_dir
        self.cuadruplos = cuadruplos
        self.constants = constants
        self.execution_queue = []
    # Funcion para inicializar la maquina virtual
    def initialize_vm(self):

        # Se agrega la global virtual memory
        g_memory = self.func_dir.func_directory['program']['num_vars']
        g_temp_memory = self.func_dir.func_directory['program']['num_temp_vars']
        self.global_memory = Memory(g_memory[0], g_memory[1], g_memory[2], g_memory[3], g_temp_memory[0], g_temp_memory[1], g_temp_memory[2], g_temp_memory[3], g_temp_memory[4], g_temp_memory[5])

        # Se agrega la mememoria de main al execution queue
        main_memory = self.func_dir.func_directory['main']['num_vars']
        main_temp_memory = self.func_dir.func_directory['main']['num_temp_vars']
        self.execution_queue.append(Memory(main_memory[0], main_memory[1], main_memory[2], main_memory[3], main_temp_memory[0], main_temp_memory[1], main_temp_memory[2], main_temp_memory[3], main_temp_memory[4], main_temp_memory[5]))

        # Se cambia la tabla de constantes
        self.changeConstantTalbe()

    # Funcion para cmabiar la llave de la tabla de constantes
    def changeConstantTalbe(self):

        newTable = dict()
        # Se genera una nueva table donde la llave es la direccion virtual y el valor se cambia a un elemento del diccionario
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
    # Se crea y regresa un nuevo objeto de tipo Memory para una funcion
    def createFunction(self, target):
        func_memory = self.func_dir.func_directory[target]['num_vars']
        func_temp_memory = self.func_dir.func_directory[target]['num_temp_vars']
        params = self.func_dir.func_directory[target]['params']
        return(Memory(func_memory[0], func_memory[1], func_memory[2], func_memory[3], func_temp_memory[0], func_temp_memory[1], func_temp_memory[2], func_temp_memory[3], func_temp_memory[4], func_temp_memory[5], params))

    # Esta funcion recibe una direccion y a traves de los estatuos if calcula el equivalente de esa direccion de compilacion en ejecucion y regresa el nuevo valor junto al tipo, si es logal, si es temporal o si es constante
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
            dir = dir - 56000
            return False, True, 6, dir, False
        
# Funcion para el cuadruplo de suma
    def suma(self, l_operand, r_operand, target):
        # Se consigue la direccion para los componentes del cuadruplo
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
        temp, local, type, dir, constant = self.checkDir(target)

        # Se revisa si son de tipo pointer y de sera asi se vuelve a generar la operacion de direccion
        if(l_type == 6):
                temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
        
        if(r_type == 6):
                temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)
        
        # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde este

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
            if(l_type == 6):
                temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
            else:
                l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
            if (r_constant):
                r_value = self.constants[r_dir]['value']
            elif (r_local):
                if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
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
        # Se calcula el resultado
        result = l_value + r_value
        
        # Se guarda el resultado en el target
        if (local):
            self.execution_queue[-1].setValue(type, result, dir, temp)
        else:
            self.global_memory.setValue(type, result, dir, temp)
    # Funcion para el cuadruplo de resta
    def resta(self, l_operand, r_operand, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
        temp, local, type, dir, constant = self.checkDir(target)

        # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
        if(l_type == 6):
                temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
        
        if(r_type == 6):
                temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)

        # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores

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
            if(l_type == 6):
                temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
            else:
                l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
            if (r_constant):
                r_value = self.constants[r_dir]['value']
            elif (r_local):
                if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
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
        # Se calcula el resultado de la resta
        result = l_value - r_value

        # Se guarda el resultado en el target
        if (local):
            self.execution_queue[-1].setValue(type, result, dir, temp)
        else:
            self.global_memory.setValue(type, result, dir, temp)
    
    # Funcion para el cuadruplo de multiplicacion
    def mult(self, l_operand, r_operand, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
        temp, local, type, dir, constant = self.checkDir(target)

         # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
        if(l_type == 6):
                temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
        
        if(r_type == 6):
                temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)

        # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores
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
            if(l_type == 6):
                temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
            else:
                l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

            if (r_constant):
                r_value = self.constants[r_dir]['value']
            elif (r_local):
                if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
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
        # Se calcula el resultado de la multiplicacion
        result = l_value * r_value
        
        # Se guarda el resultado en el target
        if (local):
            self.execution_queue[-1].setValue(type, result, dir, temp)
        else:
            self.global_memory.setValue(type, result, dir, temp)

    # Funcion para el cuadruplo de division
    def divide(self, l_operand, r_operand, target):
            # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)
            
             # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
            if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
            
            if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)

            # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores
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
                if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
                    l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    if(r_type == 6):
                        temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                        t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                        r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                    else:
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
            # Se calcula el resultado de la division
            result = l_value / r_value

            # Si el resultado es de tipo int se redondea
            if (type == 1):
                result = round(result)

            # Se guarda el resultado en el target
            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)

    # Funcion para el cuadruplo de less_than
    def less_than(self, l_operand, r_operand, target):
            # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)

             # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
            if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
            
            if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)

            # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores   
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
                if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
                    l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    if(r_type == 6):
                        temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                        t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                        r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                    else:
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
            # Se calcula el resultado de la comparacion
            result = l_value < r_value
            # Se guarda el resultado en el target
            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)
    # Funcion para el cuadruplo less_equals
    def less_equal(self, l_operand, r_operand, target):
            # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)

             # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
            if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
            
            if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)
            # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores
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
                if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
                    l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    if(r_type == 6):
                        temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                        t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                        r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                    else:
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
            # Se calcula el resultado de la comparacion
            result = l_value <= r_value
            # Se guarda el resultado en el target
            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)
    # Funcion para el cuadruplo is_equal
    def is_equal(self, l_operand, r_operand, target):
            # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)

             # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
            if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
            
            if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)
            # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores
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
                if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
                    l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    if(r_type == 6):
                        temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                        t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                        r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                    else:
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
            # Se calcula al resultado de la comparacion
            result = l_value == r_value
            # Se guarda el resultado en el target
            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)
    # Funcion para el cuadruplo greater_than
    def greater_than(self, l_operand, r_operand, target):
            # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)

             # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
            if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
            
            if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)
            # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores
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
                if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
                    l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    if(r_type == 6):
                        temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                        t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                        r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                    else:
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
            # Se calcula el resultado de la comparacion
            result = l_value > r_value
            # Se guarda el resultado en el target
            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)
    # Funcion para el cuadruplo greater_equal
    def greater_equal(self, l_operand, r_operand, target):
            # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)

             # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
            if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
            
            if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)
            # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores
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
                if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
                    l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    if(r_type == 6):
                        temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                        t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                        r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                    else:
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
            # Se calucla el resultado de la comparacion
            result = l_value >= r_value
            # Se guarda el resultado en el target
            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)
    # Funcion para el cuadruplo not_equal
    def not_equal(self, l_operand, r_operand, target):
            # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)

             # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
            if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
            
            if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)
            # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores
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
                if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
                    l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    if(r_type == 6):
                        temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                        t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                        r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                    else:
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
            # Se calcula el resultado de la comparacion
            result = l_value != r_value
            # Se guarda el resultado en el target
            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)
    # Funcion para el cuadruplo and
    def and_func(self, l_operand, r_operand, target):
            # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)

             # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
            if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
            
            if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)
            # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores
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
                if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
                    l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    if(r_type == 6):
                        temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                        t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                        r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                    else:
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
            # Se calcula el resultado de la comparacion
            result = l_value and r_value
            # Se guarda el resultado en el target
            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)
    # Funcion para el cuadruplo or
    def or_func(self, l_operand, r_operand, target):
            # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
            r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(r_operand)
            temp, local, type, dir, constant = self.checkDir(target)

            # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
            if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
            
            if(r_type == 6):
                    temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                    r_temp, r_local, r_type, r_dir, r_constant = self.checkDir(temp_val)
            # Se hacen las diferentes validaciones para conseguir el valor dependiendo de la tabla donde esten lo valores
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
                if(l_type == 6):
                    temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
                    t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                    l_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                else:
                    l_value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)

                if (r_constant):
                    r_value = self.constants[r_dir]['value']
                elif (r_local):
                    if(r_type == 6):
                        temp_val = self.execution_queue[-1].getValue(r_type, r_dir, r_temp)
                        t_temp, t_local, t_type, t_dir, t_constant = self.checkDir(temp_val)
                        r_value = self.execution_queue[-1].getValue(t_type, t_dir, t_temp)
                    else:
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
            # Se calcula el resultado de la comparacion
            result = l_value or r_value
            # Se guarda el resultado en el target
            if (local):
                self.execution_queue[-1].setValue(type, result, dir, temp)
            else:
                self.global_memory.setValue(type, result, dir, temp)
    # Funcion para el cuadruplo asigna
    def asigna(self, l_operand, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        temp, local, type, dir, constant = self.checkDir(target)
         # Se revisa si alguna variable es de tipo pointer, de ser asi se vuelve a buscar la direccion
        if (type == 6):
            temp_val = self.execution_queue[-1].getValue(type, dir, temp)
            temp, local, type, dir, constant = self.checkDir(temp_val)

        if (l_type == 6):
            temp_val = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
            l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(temp_val)
        # Se hacen las diferentes validaciones para conseguir el valor del resultado dependiendo de la tabla donde esten lo valores
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
        # Si el resultado todavia no se especifica se manda el error   
        if (result == None):
            raise Exception ("Assigned value not specified")
        # Se guarda el resultado en el target
        if (local):
            self.execution_queue[-1].setValue(type, result, dir, temp)
        else:
            self.global_memory.setValue(type, result, dir, temp)
                 
    # Funcion para el cuadruplo write
    def write(self, target):
        # se consigue la direccion del target
        temp, local, type, dir, constant = self.checkDir(target)
        # Si es de tipo pointer se repite el proceso
        if(type == 6):
            temp_val = self.execution_queue[-1].getValue(type, dir, temp)
            temp, local, type, dir, constant = self.checkDir(temp_val)
        # Se hacen validaciones sobre el tipo de la variable
        if (constant):
            value = self.constants[dir]['value']
        elif (local):
            value = self.execution_queue[-1].getValue(type, dir, temp)
        else:
            value = self.global_memory.getValue(type, dir, temp)
        # Se imprime el valor
        print(value)
    # Funcion para el cuadruplo read
    def read(self, target):
        # Se consigue el valor del target
        temp, local, type, dir, constant = self.checkDir(target)
        # Si es de tipo pointer se repite el proceso
        if(type == 6):
            temp_val = self.execution_queue[-1].getValue(type, dir, temp)
            temp, local, type, dir, constant = self.checkDir(temp_val)
        if (type == 1):
            try:
                # Si la variable es de tipo int se intenta hacer un cast a int del input
                value = int(input("Enter an integer: "))
            except:
                raise Exception("Value entered is not integer")
        elif (type == 2):
            try:
                # Si la variable es de tipo float se intenta hacer un cast a float del input
                value = float(input("Enter a float: "))
            except:
                raise Exception("Value entered is not valid")
        else:
            raise Exception ("Invalid type variable in read statement")
        # Se guarda el resultado en la variable
        if (local):
            self.execution_queue[-1].setValue(type, value, dir, temp)
        else:
            self.global_memory.setValue(type, value, dir, temp)
    # Funcion para el cuadruplo read_csv
    def read_csv(self, l_operand, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        temp, local, type, dir, constant = self.checkDir(target)
        # se consigue el valor del path del csv
        file_path = self.constants[l_dir]['value']

        try:
            # Se intena leer el csv utilizando la libreria de pandas
            df = pd.read_csv(file_path)
        except:
            raise Exception("No file was found in that path")
        # se guarda el datafraame en el target address
        if (local):
            self.execution_queue[-1].setValue(type, df, dir, temp)
        else:
            self.global_memory.setValue(type, df, dir, temp)
    # Funcion para el cuadruplo mean
    def mean(self, l_operand, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        temp, local, type, dir, constant = self.checkDir(target)
        
        # Se consigue el dataframe
        try:
            if (local):
                value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
            else:
                value = self.global_memory.getValue(l_type, l_dir, l_temp)
        except:
            raise Exception ("Error in mean function")
        # Se aplica la funcion de mean en el df
        df = value.mean()
        # Se guarda la variable en el target
        if (l_local):
            self.execution_queue[-1].setValue(type, df, dir, temp)
        else:
            self.global_memory.getValue(type, df, dir, temp)
    # FUncion para el cuadruplo mode
    def mode(self, l_operand, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        temp, local, type, dir, constant = self.checkDir(target)
        # Se consigue el dataframe
        try:
            if (local):
                value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
            else:
                value = self.global_memory.getValue(l_type, l_dir, l_temp)
        except:
            raise Exception ("Error in mode function")
        # Se aplica la funcion de moda en el df
        df = value.mode()
        # se guarda el dataframe en el target address
        if (l_local):
            self.execution_queue[-1].setValue(type, df, dir, temp)
        else:
            self.global_memory.getValue(type, df, dir, temp)
    # Funcion para el cuadruplo median
    def median(self, l_operand, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        l_temp, l_local, l_type, l_dir, l_constant = self.checkDir(l_operand)
        temp, local, type, dir, constant = self.checkDir(target)
        
        try:
            if (local):
                value = self.execution_queue[-1].getValue(l_type, l_dir, l_temp)
            else:
                value = self.global_memory.getValue(l_type, l_dir, l_temp)
        except:
            raise Exception ("Error in median function")
        # Se aplica la funcion de median en el df
        df = value.median()
        # Se guarda el df
        if (l_local):
            self.execution_queue[-1].setValue(type, df, dir, temp)
        else:
            self.global_memory.getValue(type, df, dir, temp)
    # Funcion para cuaduplo linearR
    def linearR(self, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        temp, local, type, dir, constant = self.checkDir(target)
        # se consigue el df
        try:
            if (local):
                df = self.execution_queue[-1].getValue(type, dir, temp)
            else:
                df = self.global_memory.getValue(type, dir, temp)
        except:
            raise Exception ("Error in linear regression ")
        
        # Se separa la ultima columna del df para hacer el entrenamiento

        x = df.iloc[:, 0].values.reshape(-1, 1)
        y = df.iloc[:, 1].values.reshape(-1, 1)

        # se crea la regresion lineal
        linear_regressor = LinearRegression()
        # Se entrena el modelo con x y y
        linear_regressor.fit(x, y)
        # se hacen las predicciones del modelo para x
        predictions = linear_regressor.predict(x) 
        # Se hace el scatter plot de x y y
        plt.scatter(x, y)
        # Se genera la linea de las predicciones del modelo
        plt.plot(x, predictions, color='purple')
        # se muestra la grafica
        plt.show() 
        
    # Funcion para el cuadruplo de boxplot
    def boxplot(self, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        temp, local, type, dir, constant = self.checkDir(target)
        # Se consigue el df
        try:
            if (local):
                df = self.execution_queue[-1].getValue(type, dir, temp)
            else:
                df = self.global_memory.getValue(type, dir, temp)
        except:
            raise Exception ("Error in boxplot")
        # Se generan las graficas para cada una de las columans numericas del df
        try:      
            for column in df:
                df.boxplot([column])   
                plt.show()   
        except:
            raise Exception("Error in boxplot")
        
    # FUncion para el cuadruplo histogram
    def histogram(self, target):
        # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
        temp, local, type, dir, constant = self.checkDir(target)
        # Se consigue el df
        try:
            if (local):
                df = self.execution_queue[-1].getValue(type, dir, temp)
            else:
                df = self.global_memory.getValue(type, dir, temp)
        except:
            raise Exception ("Error in histogram ")

        # Se genera el histograma para cada una de las columnas numericas del df
        try:    
            for column in df:
                df.hist([column])   
                plt.show()   
        except:
            raise Exception("Error in histogram")

    # Funcion que se encarga de leer los cuadruplos que se generaron en el parser
    def readQuad(self):
        # Inicializa el ip en 0
        ip = 0
        # Crea una lista de ips
        ip_list = []

        # Comienza a leer los cuadruplos en un ciclo while
        while (ip < len(self.cuadruplos)):
            # Asigna los valores de los cuadruplos
            op = self.cuadruplos[ip].operator
            l_operand = self.cuadruplos[ip].l_operand
            r_operand = self.cuadruplos[ip].r_operand
            target = self.cuadruplos[ip].target

            # Comienza en un "switch case" donde revisa la operacion del cuadruplo y manda llamar a la funcion correspondiente

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
            elif (op == 65):
                self.and_func(l_operand, r_operand, target)
            elif (op == 70):
                self.or_func(l_operand, r_operand, target)
            elif (op == 100):
                self.read(target)
            elif (op == 105):
                self.write(target)
            elif (op == 110):
                # Cuadruplo return
                # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
                temp, local, type, dir, constant = self.checkDir(target)
                if (constant):
                    value = self.constants[dir]['value']
                elif(local):
                    value = self.execution_queue[-1].getValue(type, dir, temp)
                else:
                    value = self.global_memory.getValue(type,dir,temp)
                # Se guarda el valor
                temp, local, type, dir, constant = self.checkDir(l_operand)
                self.global_memory.setValue(type, value, dir, temp)
                # Se elimina la funcion actual del execution queue
                self.execution_queue.pop()
                # Se consigue el ultimo valor del ip
                ip = ip_list.pop()
                continue
            elif (op == 115):
                # VER
                # Se verifica que el valor indexado este dentro de los limites

                temp, local, type, dir, constant = self.checkDir(l_operand)
                if (type == 6):
                    temp_val = self.execution_queue[-1].getValue(type, dir, temp)
                    temp, local, type, dir, constant = self.checkDir(temp_val)

                if (constant):
                    value = self.constants[dir]['value']
                elif (local):
                    value = self.execution_queue[-1].getValue(type, dir, temp)
                else:
                    value = self.global_memory.getValue(type, dir, temp)

                if ((value < r_operand) or (value >= target) or (type != 1 and constant == False)):
                    raise Exception ("Out of bounds")
                    
            elif (op == 130):
                #GOTO
                ip = target
                continue
            elif (op == 135):
                #GOTOF
                # Se consiguen las direcciones en ejecucion de los componentes del cuadruplo
                temp, local, type, dir, constant = self.checkDir(l_operand)
                # Se consigue el valor del resultado
                if (local):
                    value = self.execution_queue[-1].getValue(type, dir, temp)
                else:
                    value = self.global_memory.getValue(type, dir, temp)
                # Si el resultado es falso se cambia el ip
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
                # Endfunc
                # Se saca el ultimo valor del execution queue
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
                # Se agregan los parametros a la memoria de ejecucion
                temp, local, type, dir, constant = self.checkDir(l_operand)
                if (constant):
                    value = self.constants[dir]['value']
                elif (local):
                    value = self.execution_queue[-1].getValue(type, dir, temp)
                else:
                    value = self.global_memory.getValue(type, dir, temp)
                
                nextFunctionMem.addParam(r_operand, value)
            elif (op == 160):
                # GOSUB
                # Se mueve el ip al quad donde comienza la funcion
                self.execution_queue.append(nextFunctionMem)
                quad = self.func_dir.func_directory[l_operand]['quad_counter']
                # Se agrega el ip actual  + 1 a la lista de ips
                ip_list.append(ip + 1)
                ip = quad
                continue
            elif (op == 200):
                self.read_csv(l_operand, target)
            elif(op == 205):
                self.mean(l_operand, target)
            elif (op == 210):
                self.mode(l_operand, target)
            elif(op == 215):
                self.median(l_operand, target)
            elif(op == 220):
                self.linearR(target)
            elif(op == 225):
                self.boxplot(target)
            elif(op == 230):
                self.histogram(target)
            # Se le suma 1 al ip
            ip += 1


FILE_NAME = "./tests/pruebaEstadistica.txt"

# Se corre la funcion test_parser con el nombre de archivo que se quiere
parser.test_Parser(FILE_NAME)
# Se abren los diferentes archivos pickle y se guardan el contenido

with open('./Pickle/func_dir.pickle', 'rb') as handle:
    func_dir = pickle.load(handle)

with open('./Pickle/constants.pickle', 'rb') as handle:
    constant_table = pickle.load(handle)

with open('./Pickle/global_vars.pickle', 'rb') as handle:
    global_vars = pickle.load(handle)

with open('./Pickle/cuadruplos.pickle', 'rb') as handle:
    cuad = pickle.load(handle)

# Se genera la maquina virtual con los documento scargador por pickle
vm = VirtualMachine(func_dir, global_vars, constant_table, cuad)
# Se inicializa la maquina virtual
vm.initialize_vm()
# Se comienzan a leer los cuadruplos
vm.readQuad()