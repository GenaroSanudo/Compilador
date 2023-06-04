# Clase cuadruplo

# Funcion que se utiliza para rellenar los cuadruplos de tipo GOTO o GOTOF
def fillCuad(end, cont, cuadruplos):
    cuadruplos[end].target = cont
    return cuadruplos

# Clase cuadruplo, toma 4 parametros para crear una estrutura asi: (operator, l_operand, r_operand, target)
# operador, loperand, roperand, target
class Cuadruplo:
    def __init__(self, operator, l_operand, r_operand, target) -> None:
        self.operator = operator
        self.l_operand = l_operand
        self.r_operand = r_operand
        self.target = target

    def print(self):
        print("Operator : ", self.operator)
        print("L_operand : ", self.l_operand)
        print("R_operand : ", self.r_operand)
        print("Result : ", self.target)
    