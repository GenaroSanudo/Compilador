import ply.yacc as yacc
from lexer import tokens
from cubo import semantic_cube, traduccion
import function_directory
from cuadruple import Cuadruple, fillCuad
import virtual_adresses as va

# Function directory
current_function = None
global_vars = {}
var_list = {}
last_id = None
current_type = None

# lista de cuadruplos
cuadruplos = []
# stack_operadores
operator_stack = []
# stack_tipos
types_stack = []
# stack_operandos
operand_stack = []
# stack_saltos
jump_stack = []

func_dir = function_directory.Directory()

# Direcciones virtuales
# global_int = 0
# global_float = 2000
# global_string = 4000

# global_temp_int = 6000
# global_temp_float = 8000
# global_temp_bool = 10000
# global_temp_string = 12000

# local_int = 14000
# local_float = 16000
# local_string = 18000

# local_temp_int = 20000
# local_temp_float = 22000
# local_temp_bool = 24000
# local_temp_string = 26000

# constant_int = 28000
# constant_float = 30000
# constant_string = 32000

constant_table = {}

def p_program(p):
    '''
    program : PROGRAM program_point ID COLON modules main
    '''

def p_program_point(p):
    '''
    program_point : empty
    '''
    global current_function
    current_function = p[-1]

def p_modules(p):
    '''
    modules : modules_2 modules_point modules_3
    '''

def p_modules_point(p):
    '''
    modules_point : empty
    '''
    global func_dir
    global var_list
    global current_function
    global global_vars

    func_dir.addVariables(current_function, var_list.copy())
    # func_dir.print()
    global_vars = var_list.copy()
    var_list.clear()
    

def p_modules_2(p):
    '''
    modules_2 : vars
                | empty
    '''

def p_modules_3(p):
    '''
    modules_3 : function
                    | empty
    '''

def p_main(p):
    '''
    main : MAIN main_point LPAR RPAR L_C_BRACKET body R_C_BRACKET SEMICOLON
    '''

def p_main_point(p):
    '''
    main_point : empty
    '''
    global current_function
    current_function = p[-1]
    func_dir.addFunction(p[-1], None)

def p_body(p):
    '''
    body : vars func_agrega_v estatuto body_2
    '''
    

def p_body_2(p):
    '''
    body_2 : estatuto body_2
                | empty
    '''

def p_tipo_simple(p):
    '''
    tipo_simple : INT 
                | FLOAT
                | CHAR
    '''
    global current_type
    current_type = p[1]

def p_tipo_comp(p):
    '''
    tipo_comp : DATAFRAME
    '''
    global current_type
    current_type = p[1]

def p_vars(p):
    '''
    vars : VAR vars_2 SEMICOLON vars_8
    '''
    

def p_vars_2(p):
    '''
    vars_2 : tipo_comp vars_3
                        | tipo_simple vars_4
    '''

def p_vars_3(p):
    '''
    vars_3 : ID vars_5
    '''
    var_id = p[1]
    global current_type
    global var_list
    global current_function

    type = traduccion(current_type)

    temp = va.getAddress(current_function, type)
    if (type == 5):
        print(current_function, type)

    var_list[var_id] = {'type' : type, 'dim' : 0, 'size': 0, 'virtual_dir' : temp}

def p_vars_4(p):
    '''
    vars_4 : vars_3 
                | ID vars_6
    '''

def p_vars_5(p):
    '''
    vars_5 : COMMA vars_3
            | empty
    '''

def p_vars_6(p):
    '''
    vars_6 : punto_id_especial L_S_BRACKET CTE_I R_S_BRACKET vars_7
                | empty
    '''
def p_punto_id_especial(p):
    '''
    punto_id_especial : empty
    '''
    global last_id
    last_id = p[-1]

def p_vars_7(p):
    '''
    vars_7 : L_S_BRACKET CTE_I R_S_BRACKET var_mat
                | var_array
    '''

def p_var_array(p):
    '''
    var_array : empty
    '''
    global var_list
    global last_id
    global current_type
    type = traduccion(current_type)
    var_list[last_id] = {'type' : type, 'dim' : 1, 'size': [p[-2]]}

def p_var_mat(p):
    '''
    var_mat : empty
    '''
    global var_list
    global last_id
    global current_type
    type = traduccion(current_type)
    var_list[last_id] = {'type' : type, 'dim' : 2, 'size': [p[-5],p[-2]]}
    

def p_vars_8(p):
    '''
    vars_8 : vars 
                | empty
    '''

def p_param(p):
    '''
    param : tipo_simple ID punto_param param_2
                | empty
    '''

def p_param_2(p):
    '''
    param_2 : COMMA param
                | empty
    '''

def p_punto_param(p):
    '''
    punto_param : empty
    '''
    global current_type
    type = traduccion(current_type)
    func_dir.addParameter(current_function, type)

def p_variable(p):
    '''
    variable : ID variable_2 variable_point
    '''

def p_variable_point(p):
    '''
    variable_point : empty
    '''
    global global_vars
    global current_function
    global func_dir
    global operand_stack
    global types_stack

    if (func_dir.checkVariable(current_function, p[-2])):
        type = func_dir.getType(current_function, p[-2])
        operand_stack.append(func_dir.func_directory[current_function]['vars'][p[-2]]['virtual_dir'])
        types_stack.append(type)
    elif(func_dir.checkVariable('program', p[-2])):
        type = func_dir.getType('program', p[-2])
        operand_stack.append(p[-2])
        types_stack.append(type)
    else:
        print("Esta variable no esta declarada")


def p_variable_2(p):
    '''
    variable_2 : L_S_BRACKET exp R_S_BRACKET variable_3 
                    | empty
    '''

def p_variable_3(p):
    '''
    variable_3 : L_S_BRACKET exp R_S_BRACKET
                    | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asigna
                | llamada
                | read
                | write
                | if_1
                | for_l
                | while_l
                | func_extra
    '''

def p_asigna(p):
    '''
    asigna : variable EQUAL add_operator exp asigna_point SEMICOLON
    '''

def p_asigna_point(p):
    '''
    asigna_point : empty
    '''
    global types_stack
    global operand_stack
    global operator_stack
    global cuadruplos

    right_operand = operand_stack.pop()
    right_type = types_stack.pop()

    left_operand = operand_stack.pop()
    left_type = types_stack.pop()

    operator = operator_stack.pop()

    try:
        result_type = semantic_cube[left_type][right_type][operator]
        cuadruplos.append(Cuadruple(operator, right_operand, None, left_operand))
        # Falta volver a agregar a stacks?
    except:
        print("Asignacion no compatible")



def p_llamada(p):
    '''
    llamada : ID LPAR exp llamada_2 RPAR SEMICOLON
    '''

def p_llamada_2(p):
    '''
    llamada_2 : COMMA exp llamada_2 
                | empty
    '''

def p_read(p):
    '''
    read : READ LPAR variable read_point RPAR SEMICOLON
    '''

def p_read_point(p):
    '''
    read_point : empty
    '''
    global operand_stack
    global types_stack
    global cuadruplos
    var = operand_stack.pop()
    types_stack.pop()
    cuadruplos.append(Cuadruple(100, None, None, var))

def p_write(p):
    '''
    write : WRITE LPAR write_2 write_3 RPAR SEMICOLON
    '''

def p_write_2(p):
    '''
    write_2 : exp write_point
                | CTE_S add_constant_s write_point
    '''

def p_write_3(p):
    '''
    write_3 : COMMA write_2 write_3 
                | empty
    '''

def p_write_point(p):
    '''
    write_point : empty
    '''
    global operand_stack
    global cuadruplos

    op = operand_stack.pop()
    types_stack.pop()
    cuadruplos.append(Cuadruple(105, None, None, op))

    

def p_if_1(p):
    '''
    if_1 : IF LPAR exp if_point RPAR L_C_BRACKET estatuto if_2 R_C_BRACKET if_3 SEMICOLON if_point_2
    '''

def p_if_2(p):
    '''
    if_2 :  estatuto if_2 
            | empty
    '''

def p_if_3(p):
    '''
    if_3 : ELSE if_point_3 L_C_BRACKET estatuto if_2 R_C_BRACKET
            | empty
    '''

def p_if_point(p):
    '''
    if_point : empty
    '''
    global types_stack
    global operand_stack
    global jump_stack
    global cuadruplos
    
    type = types_stack.pop()

    if (type != 3):
        print ("TYPE MISMATCH")
    else:
        result = operand_stack.pop()
        cuadruplos.append(Cuadruple(135, result, None, None))
        jump_stack.append(len(cuadruplos)-1)
    
def p_if_point_2(p):
    '''
    if_point_2 : empty
    '''
    global jump_stack
    global cuadruplos
    
    end = jump_stack.pop()
    cuadruplos = fillCuad(end, len(cuadruplos) ,cuadruplos)

def p_if_point_3(p):
    '''
    if_point_3 : empty
    '''
    global jump_stack
    global cuadruplos

    cuadruplos.append(Cuadruple(130, None, None, None))
    false = jump_stack.pop()
    jump_stack.append(len(cuadruplos)-1)
    cuadruplos = fillCuad(false, len(cuadruplos), cuadruplos)

def p_for_l(p):
    '''
    for_l : FOR LPAR ID RPAR EQUAL exp TO exp RPAR L_C_BRACKET estatuto for_l_2 R_C_BRACKET SEMICOLON
    '''

def p_for_l_2(p):
    '''
    for_l_2 : estatuto for_l_2
                | empty
    '''

def p_while_l(p):
    '''
    while_l : WHILE while_point LPAR exp RPAR while_point_2 L_C_BRACKET estatuto while_l_2 R_C_BRACKET SEMICOLON while_point_3
    '''

def p_while_l_2(p):
    '''
    while_l_2 : estatuto while_l_2
                    | empty
    '''

def p_while_point(p):
    '''
    while_point : empty
    '''
    global jump_stack
    global cuadruplos
    jump_stack.append(len(cuadruplos))

def p_while_point_2(p):
    '''
    while_point_2 : empty
    '''
    global jump_stack
    global cuadruplos
    global types_stack
    global operand_stack

    type = types_stack.pop()

    if (type != 3):
        print("Type mismatch")
    else:
        result = operand_stack.pop()
        cuadruplos.append(Cuadruple(135, result, None, None))
        jump_stack.append(len(cuadruplos)-1)

    jump_stack.append(len(cuadruplos))

def p_while_point_3(p):
    '''
    while_point_3 : empty
    '''
    global jump_stack
    global cuadruplos
    end = jump_stack.pop()
    ret = jump_stack.pop()
    cuadruplos.append(Cuadruple(130,None, None, ret))
    cuadruplos = fillCuad(ret, len(cuadruplos), cuadruplos)

def p_func_extra(p):
    '''
    func_extra : empty
    '''

def p_exp(p):
    '''
    exp : t_exp add_operator_4 exp_2 
    '''

def p_exp_2(p):
    '''
    exp_2 : OR add_operator exp 
            | empty
    '''

def p_t_exp(p):
    '''
    t_exp : g_exp add_operator_4 t_exp_2 
    '''

def p_t_exp_2(p):
    '''
    t_exp_2 : AND add_operator t_exp 
                | empty
    '''

def p_g_exp(p):
    '''
    g_exp : m_exp g_exp_2 add_operator_3
    '''

def p_g_exp_2(p):
    '''
    g_exp_2 : LESS_EQUAL add_operator m_exp 
                | LESS add_operator m_exp 
                | GREATER_EQUAL add_operator m_exp 
                | GREATER add_operator m_exp 
                | COMPARE add_operator m_exp 
                | NOT_EQUAL add_operator m_exp 
                | empty
    '''

def p_m_exp(p):
    '''
    m_exp : t add_operator_2 m_exp_2
    '''

def p_m_exp_2(p):
    '''
    m_exp_2 : PLUS add_operator m_exp 
                | MINUS add_operator m_exp
                | empty
    '''

def p_t(p):
    '''
    t : f add_operator_1 t_2
    '''

def p_t_2(p):
    '''
    t_2 : TIMES add_operator t 
            | DIVIDE add_operator t
            | empty
    '''

def p_f(p):
    '''
    f : LPAR add_floor exp RPAR remove_floor
            | variable
            | llamada
            | f_2
    '''

def p_f_2(p):
    '''
    f_2 : CTE_I add_constant_i
            | CTE_F add_constant_f
    '''

def p_add_floor(p):
    '''
    add_floor : empty
    '''
    global operator_stack
    operator_stack.append(75)

def p_remove_floor(p):
    '''
    remove_floor : empty
    '''
    global operator_stack
    operator_stack.pop()

def p_add_operator(p):
    '''
    add_operator : empty 
    '''
    # print('add_operator')
    global operator_stack
    op = traduccion(p[-1])
    operator_stack.append(op)
    
def p_add_operator_1(p):
    '''
    add_operator_1 : empty 
    '''
    global operator_stack
    global operand_stack
    global types_stack
    if (len(operator_stack) != 0) :
        if ((operator_stack[-1] == 20) or (operator_stack[-1] == 25)):
            right_operand = operand_stack.pop()
            right_type = types_stack.pop()

            left_operand = operand_stack.pop()
            left_type = types_stack.pop()

            operator = operator_stack.pop()
            
            try: 
                result_type = semantic_cube[left_type][right_type][operator]
            except:
                print("Type mismatch")
                return
            global current_function
            temp = va.getTemporalAddress(current_function, result_type)

            cuadruplos.append(Cuadruple(operator, left_operand, right_operand, temp))
            operand_stack.append(temp)
            types_stack.append(result_type)


def p_add_operator_2(p):
    '''
    add_operator_2 : empty 
    '''
    global operator_stack
    global operand_stack
    global types_stack
    if (len(operator_stack) != 0) :
        if ((operator_stack[-1] == 10) or (operator_stack[-1] == 15)):
            right_operand = operand_stack.pop()
            right_type = types_stack.pop()

            left_operand = operand_stack.pop()
            left_type = types_stack.pop()

            operator = operator_stack.pop()
            
            try: 
                result_type = semantic_cube[left_type][right_type][operator]
            except:
                print("Type mismatch")
                return
            global current_function
            temp = va.getTemporalAddress(current_function, result_type)

            cuadruplos.append(Cuadruple(operator, left_operand, right_operand, temp))
            operand_stack.append(temp)
            types_stack.append(result_type)

    
def p_add_operator_3(p):
    '''
    add_operator_3 : empty 
    '''
    global operator_stack
    global operand_stack
    global types_stack
    if (len(operator_stack) != 0) :
        if ((operator_stack[-1] == 30) or (operator_stack[-1] == 35) or (operator_stack[-1] == 40) or (operator_stack[-1] == 45) or
            (operator_stack[-1] == 50) or (operator_stack[-1] == 55)):
            right_operand = operand_stack.pop()
            right_type = types_stack.pop()

            left_operand = operand_stack.pop()
            left_type = types_stack.pop()

            operator = operator_stack.pop()
            
            try: 
                result_type = semantic_cube[left_type][right_type][operator]
            except:
                print("Type mismatch", left_operand, left_type, right_operand, right_type, operator)
                return
            global current_function
            temp = va.getTemporalAddress(current_function, result_type)

            cuadruplos.append(Cuadruple(operator, left_operand, right_operand, temp))
            operand_stack.append(temp)
            types_stack.append(result_type)

def p_add_operator_4(p):
    '''
    add_operator_4 : empty 
    '''
    global operator_stack
    global operand_stack
    global types_stack
    if (len(operator_stack) != 0) :
        if ((operator_stack[-1] == 65) or (operator_stack[-1] == 70)):
            right_operand = operand_stack.pop()
            right_type = types_stack.pop()

            left_operand = operand_stack.pop()
            left_type = types_stack.pop()

            operator = operator_stack.pop()
            
            try: 
                result_type = semantic_cube[left_type][right_type][operator]
            except:
                print("Type mismatch")
                return
            global current_function
            temp = va.getTemporalAddress(current_function, result_type)

            cuadruplos.append(Cuadruple(operator, left_operand, right_operand, temp))
            operand_stack.append(temp)
            types_stack.append(result_type)

def p_add_constant_i(p):
    '''
    add_constant_i : empty
    '''
    global operand_stack
    global types_stack
    global constant_table

    # Adds type and operand to the stack
    if (constant_table.get(str(p[-1])) != None):
        types_stack.append(constant_table[str(p[-1])]['type'])
        operand_stack.append(constant_table[str(p[-1])]['virtual_dir'])
    else:
        constant_table[str(p[-1])] = {'type' : 1, 'virtual_dir' : va.constant_int}
        types_stack.append(1)
        operand_stack.append(va.constant_int)
        va.constant_int = va.constant_int + 1

def p_add_constant_s(p):
    '''
    add_constant_s : empty
    '''
    global operand_stack
    global types_stack
    global constant_table
    # Adds type and operand to the stack
    if (constant_table.get(str(p[-1])) != None):
        types_stack.append(constant_table[str(p[-1])]['type'])
        operand_stack.append(constant_table[str(p[-1])]['virtual_dir'])
    else:
        constant_table[str(p[-1])] = {'type' : 4, 'virtual_dir' : va.constant_string}
        types_stack.append(4)
        operand_stack.append(va.constant_string)
        va.constant_string = va.constant_string + 1

def p_add_constant_f(p):
    '''
    add_constant_f : empty
    '''
    global operand_stack
    global types_stack
    global constant_table  
    # Adds type and operand to the stack
    if (constant_table.get(str(p[-1])) != None):
        types_stack.append(constant_table[str(p[-1])]['type'])
        operand_stack.append(constant_table[str(p[-1])]['virtual_dir'])
    else:
        constant_table[str(p[-1])] = {'type' : 2, 'virtual_dir' : va.constant_float}
        types_stack.append(1)
        operand_stack.append(va.constant_float)
        va.constant_float = va.constant_float + 1
    
def p_function(p):
    '''
    function : FUNC function_2 SEMICOLON function_3
    '''

def p_function_2(p):
    '''
    function_2 : tipo_simple ID function_punto1 LPAR param RPAR L_C_BRACKET body RETURN LPAR exp RPAR SEMICOLON R_C_BRACKET 
                    | VOID ID function_punto2 LPAR param RPAR L_C_BRACKET body R_C_BRACKET
    '''

def p_function_3(p):
    '''
    function_3 : function
                    | empty
    '''

def p_function_punto1(p):
    '''
    function_punto1 : empty
    '''
    global current_type
    type = traduccion(current_type)
    func_dir.addFunction(p[-1], type)
    global current_function
    current_function = p[-1]

def p_function_punto2(p):
    '''
    function_punto2 : empty
    '''
    func_dir.addFunction(p[-1], 0)
    global current_function
    current_function = p[-1]

def p_func_agrega_v(p):
    '''
    func_agrega_v : empty
    '''
    global current_function
    func_dir.addVariables(current_function, var_list.copy())
    # func_dir.print()
    var_list.clear()



def p_empty(p):
    '''
    empty : 
    '''

parser = yacc.yacc()

def test_Parser():
  try:
      test_file = open("./test.txt", "r")
      test = test_file.read()
      test_file.close()
      print ("Test parser")
      parser.parse(test)
      
  except EOFError:
      print('s')

if __name__ == '__main__':
        test_Parser()
        cont = 0
        for element in cuadruplos:
            print (cont)
            cont = cont +1 
            element.print()
        print(operator_stack, operand_stack, types_stack)
        # func_dir.print()
        # print(va.constant_float)
        # print(constant_table)