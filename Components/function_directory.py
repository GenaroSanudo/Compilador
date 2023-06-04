

# Clase directorio de funciones
# Este objeto se utiliza para tener un registro de todas las funciones y sus variables, parametros al igual que el numero de cuadruplo donde comienzan
class Directory:
    # Al inicializar se agrega la "funcion" de tipo programa.
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

    # Funcion para agregar una funcion, se utilizan valores placeholder para la mayoria de los estatutos
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
            # print ("Added func: ", type, name)
        else:
            raise Exception("Function " + str(name) + " already exists")

    # Funcion para agregar variables a una funcion, "name", que ya se declaro
    def addVariables(self, name, variables):
        if (self.func_directory.get(name) != None):
            self.func_directory[name]['vars'] = variables
        else:
            print("Function does not exist")

    # Funcion para agregar parametros a una funcion, "name", que ya se declaro
    def addParameter(self, name, parameter):
        if (self.func_directory.get(name) != None):
            self.func_directory[name]['params'].append(parameter)
        else:
            print("Function does not exist")

    # Funcion que regresa las variables de una funcion "name"
    def getVariables(self, name):
        if (self.func_directory.get(name) != None):
            return self.func_directory[name].get('vars')
    
    # Funcion para revisar si una variable se declaro para una funcion "func"
    def checkVariable(self, func, var):
        if (self.func_directory[func]['vars'].get(var) != None):
            return True
        else:
            return False
    
    # Funcion que revisa si ya se declaro una funcion de nombre "func" dentro del directorio de funciones
    def checkFunction(self, func):
        if (self.func_directory.get(func) != None):
            return True
        else:
            return False
    
    # Funcion que regresa el tipo de una funcion "func"
    def getType(self, func, var):
        return self.func_directory[func]['vars'][var]['type']
    
    # Funcion que regresa los parametros de una funcion con nombre "name"
    def getParameters(self, name):
        if (self.func_directory.get(name) != None):
            return self.func_directory[name].get('params')

    # Funcnion para conseguir la direccionn virtual de una variable "var" dentro de una funcion "current_function"
    def getAddress(self, current_function, var):
        dir = self.func_directory[current_function]['vars'][var]['virtual_dir']
        return dir

    # Funcion para agregar el numero de variables temporales a una funcion 
    def setTempVars(self, function, vars):
        try:
            self.func_directory[function]['num_temp_vars'] = vars
        except:
            raise Exception("Error setting temp variables")
    
    # Funcion para imprimir el objeto func_directory
    def print(self):
        print(self.func_directory)
