import ply.yacc as yacc
from lexer import tokens
from cubo import semantic_cube, traduccion
import function_directory
from cuadruple import Cuadruple

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

temporal = 0

func_dir = function_directory.Directory()

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
    main : MAIN LPAR RPAR L_C_BRACKET body R_C_BRACKET SEMICOLON
    '''

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
    type = traduccion(current_type)
    var_list[var_id] = {'type' : type, 'dim' : 0, 'size': 0}

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
        operand_stack.append(p[-2])
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
        cuadruplos.append(Cuadruple(operator, left_operand, right_operand, left_operand))
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
    cuadruplos.append(Cuadruple('READ', None, None, var))

def p_write(p):
    '''
    write : WRITE LPAR write_2 write_3 RPAR SEMICOLON
    '''

def p_write_2(p):
    '''
    write_2 : exp
                | CTE_S
    '''

def p_write_3(p):
    '''
    write_3 : COMMA write_2 write_3 
                | empty
    '''

def p_if_1(p):
    '''
    if_1 : IF LPAR exp RPAR L_C_BRACKET estatuto if_2 R_C_BRACKET if_3 SEMICOLON
    '''

def p_if_2(p):
    '''
    if_2 : estatuto if_2 
            | empty
    '''

def p_if_3(p):
    '''
    if_3 : ELSE L_C_BRACKET estatuto if_2 R_C_BRACKET
    '''

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
    while_l : WHILE LPAR exp RPAR L_C_BRACKET estatuto while_l_2 R_C_BRACKET SEMICOLON
    '''

def p_while_l_2(p):
    '''
    while_l_2 : estatuto while_l_2
                    | empty
    '''

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
    operator_stack.append(70)

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
        if ((operator_stack[-1] == 15) or (operator_stack[-1] == 20)):
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
            global temporal

            cuadruplos.append(Cuadruple(operator, left_operand, right_operand, temporal))
            operand_stack.append(temporal)
            types_stack.append(result_type)
            temporal = temporal + 1


def p_add_operator_2(p):
    '''
    add_operator_2 : empty 
    '''
    global operator_stack
    global operand_stack
    global types_stack
    if (len(operator_stack) != 0) :
        if ((operator_stack[-1] == 5) or (operator_stack[-1] == 10)):
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
            global temporal

            cuadruplos.append(Cuadruple(operator, left_operand, right_operand, temporal))
            operand_stack.append(temporal)
            types_stack.append(result_type)
            temporal = temporal + 1

    
def p_add_operator_3(p):
    '''
    add_operator_3 : empty 
    '''
    global operator_stack
    global operand_stack
    global types_stack
    if (len(operator_stack) != 0) :
        if ((operator_stack[-1] == 25) or (operator_stack[-1] == 30) or (operator_stack[-1] == 35) or (operator_stack[-1] == 40) or
            (operator_stack[-1] == 45) or (operator_stack[-1] == 50)):
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
            global temporal

            cuadruplos.append(Cuadruple(operator, left_operand, right_operand, temporal))
            operand_stack.append(temporal)
            types_stack.append(result_type)
            temporal = temporal + 1

def p_add_operator_4(p):
    '''
    add_operator_4 : empty 
    '''
    global operator_stack
    global operand_stack
    global types_stack
    if (len(operator_stack) != 0) :
        if ((operator_stack[-1] == 60) or (operator_stack[-1] == 65)):
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
            global temporal

            cuadruplos.append(Cuadruple(operator, left_operand, right_operand, temporal))
            operand_stack.append(temporal)
            types_stack.append(result_type)
            temporal = temporal + 1

def p_add_constant_i(p):
    '''
    add_constant_i : empty
    '''
    global operand_stack
    global types_stack
    # Adds type and operand to the stack
    types_stack.append(1)
    operand_stack.append(p[-1])

def p_add_constant_f(p):
    '''
    add_constant_f : empty
    '''
    global operand_stack
    global types_stack
    # Adds type and operand to the stack
    types_stack.append(2)
    operand_stack.append(p[-1])
    
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
        for element in cuadruplos:
            element.print()
        print(operator_stack, operand_stack, types_stack)
        # print(global_vars)