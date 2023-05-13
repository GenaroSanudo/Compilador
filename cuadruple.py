# operador, loperand, roperand, target
class Cuadruple:
    def __init__(self, operator, l_operand, r_operand, target) -> None:
        self.operator = operator
        self.l_operand = l_operand
        self.r_operand = r_operand
        self.target = target

    def print(self):
        print("Operator : ", self.operator)
        print("L_operand : ", self.l_operand)
        print("R_operand : ", self.r_operand)
        print("Target : ", self.target)
    


cuadruples = Cuadruple(1,2,3,4)

