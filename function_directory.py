

# dic_func = funcion {params[], variables{}, typeOfR}
# variables = nombre, type, dim, size

class Directory:
    
    def __init__(self) -> 'None':
        self.func_directory = {
            'program' : {
                'params' : [],
                'vars' : {},
                'typeOfR' : 0
            }
        }

    def addFunction(self, name, type):
        if (self.func_directory.get(name) == None):
            self.func_directory[name] = {
                'typeOfR' : type,
                'vars' : {},
                'params' : []
            }
            print ("Added func: ", type, name)
        else:
            print("Function already exists")

    def addFunctionFull(self, name, type, par, variables ):
        if (self.func_directory.get(name) == None):
            self.func_directory[name] = {
                'params' : par,
                'vars' : variables,
                'typeOfR' : type
            }
        else:
            print("Function already exist")
    
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
        
    def getParameters(self, name):
        if (self.func_directory.get(name) != None):
            return self.func_directory[name].get('params')
            
            
    def print(self):
        print(self.func_directory)


# dir = Directory()

# # dir.addFunction('b', 1)

# dir.addFunctionFull('a', 1, [2,3,5], {'var' : 3, 'variable' : 2})

# dir.addVariables('a', {'var' : 1, 'variable' : 4})

# dir.print()
