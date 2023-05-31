

# dic_func = funcion {params[], variables{}, typeOfR}
# variables = nombre, type, dim, size

class Directory:
    
    def __init__(self) -> 'None':
        self.func_directory = {
            'program' : {
                'params' : [],
                'vars' : {},
                'typeOfR' : None,
                'num_params' : 0,
                'quad_counter' : 0,
                'num_vars' : [0, 0, 0, 0, 0],
                'num_temp_vars' : [0, 0, 0, 0, 0]
            }
        }

    def addFunction(self, name, type):
        if (self.func_directory.get(name) == None):
            self.func_directory[name] = {
                'typeOfR' : type,
                'vars' : {},
                'params' : [],
                'num_params' : 0,
                'quad_counter' : 0,
                'num_vars' : [0, 0, 0 , 0, 0],
                'num_temp_vars' : [0, 0, 0, 0, 0]
            }
            print ("Added func: ", type, name)
        else:
            raise Exception("Function " + str(name) + " already exists")

    
    def addVariables(self, name, variables):
        if (self.func_directory.get(name) != None):
            self.func_directory[name]['vars'] = variables
        else:
            print("Function does not exist")


    def addParameter(self, name, parameter):
        if (self.func_directory.get(name) != None):
            self.func_directory[name]['params'].append(parameter)
        else:
            print("Function does not exist")

    def getVariables(self, name):
        if (self.func_directory.get(name) != None):
            return self.func_directory[name].get('vars')
    
    def checkVariable(self, func, var):
        if (self.func_directory[func]['vars'].get(var) != None):
            return True
        else:
            return False
    
    def checkFunction(self, func):
        if (self.func_directory.get(func) != None):
            return True
        else:
            return False
    
    def getType(self, func, var):
        return self.func_directory[func]['vars'][var]['type']
        
    def getParameters(self, name):
        if (self.func_directory.get(name) != None):
            return self.func_directory[name].get('params')

    def getAddress(self, current_function, var):
        dir = self.func_directory[current_function]['vars'][var]['virtual_dir']
        return dir
                
    def setTempVars(self, function, vars):
        try:
            self.func_directory[function]['num_temp_vars'] = vars
        except:
            raise Exception("Error setting temp variables")
             
    def print(self):
        print(self.func_directory)


# dir = Directory()

# # dir.addFunction('b', 1)

# dir.addFunctionFull('a', 1, [2,3,5], {'var' : 3, 'variable' : 2})

# dir.addVariables('a', {'var' : 1, 'variable' : 4})

# dir.print()
