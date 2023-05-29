import ply.yacc as yacc
from lexer import tokens
from cubo import semantic_cube, traduccion
import function_directory
from cuadruplo import Cuadruplo, fillCuad
import virtual_adresses as va
import pickle

# Function directory
current_function = None
called_function = None
global_vars = {}
var_list = {}
last_id = None
current_type = None
return_flag = 0
k = None

# For loop
v_control = None

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

dim_stack = []

func_dir = function_directory.Directory()

# Counters para las direcciones temporales utilizadas
temp_int_cont = 40000
temp_float_cont = 42000
temp_bool_cont = 44000
temp_string_cont = 46000
temp_dataf_cont = 48000

local_int_cont = 30000
local_float_cont = 32000
local_string_cont = 34000
local_dataframe_cont = 36000

global_int_cont = 0
global_float_cont = 2000
global_string_cont = 4000
global_dataframe_cont = 6000

temp_pointer_cont = 56000


constant_table = {}

def p_program(p):
    '''
    program : PROGRAM program_point ID COLON modules main
    '''

def p_program_point(p):
    '''
    program_point : empty
    '''
    global current_function, cuadruplos, jump_stack
    cuadruplos.append(Cuadruplo(130, None, None, None))
    jump_stack.append(len(cuadruplos)-1)
    current_function = p[-1]

def p_modules(p):
    '''
    modules : modules_2 modules_point modules_3 count_global_vars
    '''

def p_modules_point(p):
    '''
    modules_point : empty
    '''
    global func_dir, var_list, current_function, global_vars
    
    func_dir.addVariables(current_function, var_list.copy())
    # func_dir.print()
    func_dir.func_directory[current_function]['quad_counter'] = len(cuadruplos)

    global_vars = var_list.copy()
    var_list.clear()

def p_count_global_vars(p):
    '''
    count_global_vars : empty
    '''
    global func_dir, var_list, current_function, global_vars
    global global_int_cont, global_float_cont, global_string_cont, global_dataframe_cont

    int_cont = va.global_int - global_int_cont 
    float_cont = va.global_float - global_float_cont
    string_cont = va.global_string - global_string_cont
    dataframe_cont =  va.global_dataframe - global_dataframe_cont

    global_int_cont = va.global_int
    global_float_cont = va.global_float
    global_string_cont = va.global_string
    global_dataframe_cont = va.global_dataframe

    func_dir.func_directory['program']['num_vars'] = [int_cont, float_cont, string_cont, dataframe_cont]
    func_dir.func_directory['program']['vars'].clear()
    

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
    main : MAIN main_point LPAR RPAR L_C_BRACKET body R_C_BRACKET SEMICOLON main_final
    '''

def p_main_point(p):
    '''
    main_point : empty
    '''
    global current_function, cuadruplos, jump_stack

    goto = jump_stack.pop()
    cuadruplos = fillCuad(goto, len(cuadruplos), cuadruplos)

    current_function = p[-1]
    func_dir.addFunction(p[-1], None)

def p_main_final(p):
    '''
    main_final : empty
    '''
    global current_function, func_dir, cuadruplos
    global temp_int_cont, temp_float_cont, temp_dataf_cont, temp_bool_cont, temp_string_cont

    temp_addresses = [va.local_temp_int - temp_int_cont, va.local_temp_float-temp_float_cont, va.local_temp_bool - temp_bool_cont, va.local_temp_string - temp_string_cont, va.local_temp_dataframe - temp_dataf_cont]
    func_dir.setTempVars(current_function, temp_addresses)

    va.local_temp_int = temp_int_cont
    va.local_temp_float = temp_float_cont
    va.local_temp_bool = temp_bool_cont
    va.local_temp_dataframe = temp_dataf_cont

    func_dir.func_directory[current_function]['vars'].clear()

    cuadruplos.append(Cuadruplo(145, None, None, None))

def p_body(p):
    '''
    body : body_2 func_agrega_v estatuto body_3
    '''

def p_body_2(p):
    '''
    body_2 : vars
                | empty
    '''  
    
def p_body_3(p):
    '''
    body_3 : estatuto body_3
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

    var_list[var_id] = {'type' : type, 'dim' : 0, 'size': 1, 'virtual_dir' : temp}

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
    global var_list, last_id, current_type, current_function
    type = traduccion(current_type)
    var_list[last_id] = {'type' : type, 'dim' : 1, 'size': [p[-2]], 'virtual_dir' : va.getAddress(current_function, type, p[-2])}

def p_var_mat(p):
    '''
    var_mat : empty
    '''
    global var_list
    global last_id
    global current_type
    type = traduccion(current_type)
    var_list[last_id] = {'type' : type, 'dim' : 2, 'size': [p[-5],p[-2]], 'virtual_dir' : va.getAddress(current_function, type, p[-2] * p[-5])}
    

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
    global var_list
    type = traduccion(current_type)
    func_dir.addParameter(current_function, type)
    virtual_dir = va.getAddress(current_function, type)
    var_list[p[-1]] = {'type' : type, 'dim' : 0, 'size': 1, 'virtual_dir' : virtual_dir}


def p_punto_param_2(p):
    '''
    punto_param_2 : empty
    '''
    global current_function
    global func_dir
    func_dir.func_directory[current_function]['num_params'] = len(func_dir.func_directory[current_function]['params'])
    

def p_variable(p):
    '''
    variable : ID variable_2 variable_point
    '''

def p_variable_point(p):
    '''
    variable_point : empty
    '''
    global global_vars, current_function, func_dir, operand_stack, types_stack, cuadruplos

    

    if (func_dir.checkVariable(current_function, p[-2])):
        dim = func_dir.func_directory[current_function]['vars'][p[-2]]['dim']
        if (dim > 0):
            size = func_dir.func_directory[current_function]['vars'][p[-2]]['size']
            dir = func_dir.func_directory[current_function]['vars'][p[-2]]['virtual_dir']

            if (constant_table.get(str(dir)) != None):
                constant_dir = constant_table[str(dir)]['virtual_dir']
            else:
                constant_table[str(dir)] = {'type' : 1, 'virtual_dir' : va.constant_int}
                constant_dir = va.constant_int
                va.constant_int = va.constant_int + 1
            
            if (dim == 1):
                value = operand_stack.pop()

                cuadruplos.append(Cuadruplo(115, value, 0, size[0]))
                tp = va.getTemporalAddress(current_function, 1)
                cuadruplos.append(Cuadruplo(10, value, constant_dir, tp))
                operand_stack.append(tp)
                types_stack.append(1)
            elif (dim == 2):
                value2 = operand_stack.pop()
                value = operand_stack.pop()
                cuadruplos.append(Cuadruplo(115, value, 0, size[0]))
                tp = va.getTemporalAddress(current_function, 1)
                cuadruplos.append(Cuadruplo(20, value, size[0], tp))
                cuadruplos.append(Cuadruplo(115, value2, 0, size[1]))
                tp2 = va.getTemporalAddress(current_function, 1)
                cuadruplos.append(Cuadruplo(10, tp, value2, tp2))
                tp3 = va.getTemporalAddress(current_function, 1)
                cuadruplos.append(Cuadruplo(10, tp2, constant_dir, tp3))
                operand_stack.append(tp3)
                types_stack.append(1)
        else:
            type = func_dir.getType(current_function, p[-2])
            operand_stack.append(func_dir.getAddress(current_function, p[-2]))
            types_stack.append(type)
        
    elif(global_vars.get(p[-2], False)):
        dim = global_vars[p[-2]]['dim']
        
        if (dim == 1):
            #AQUI VAN ARREGLOS
            print(operand_stack.pop())
        elif (dim == 2):
            #AQUI VAN MATRICES
            print(operand_stack.pop(), operand_stack.pop())
        type = global_vars[p[-2]]['type']
        operand_stack.append(global_vars[p[-2]]['virtual_dir'])
        types_stack.append(type)
    else:
        raise Exception("Esta variable no esta declarada", p[-2])
    


def p_variable_2(p):
    '''
    variable_2 : L_S_BRACKET add_floor exp R_S_BRACKET remove_floor variable_3 
                    | empty
    '''

def p_variable_3(p):
    '''
    variable_3 : L_S_BRACKET add_floor exp R_S_BRACKET remove_floor
                    | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asigna
                | llamada
                | llamada_void
                | read
                | write
                | if_1
                | for_l
                | while_l
                | return
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

    print("ellow", right_operand, left_operand)

    try:
        result_type = semantic_cube[left_type][right_type][operator]
        cuadruplos.append(Cuadruplo(operator, right_operand, None, left_operand))
        # Falta volver a agregar a stacks?
    except:
        raise Exception ("Asignación no compatible")



def p_llamada(p):
    '''
    llamada : ID verify_func not_void LPAR add_floor llamada_2 llamada_3 RPAR remove_floor SEMICOLON gosub add_temp
    '''

def p_llamada_2(p):
    '''
    llamada_2 : exp verify_parameter
                | empty
    '''

def p_llamada_3(p):
    '''
    llamada_3 : COMMA exp verify_parameter llamada_3
                | empty
    '''

def p_llamada_void(p):
    '''
    llamada_void : ID verify_func LPAR add_floor llamada_void_2 llamada_void_3 RPAR remove_floor SEMICOLON gosub 
    '''

def p_llamada_void_2(p):
    '''
    llamada_void_2 : exp verify_parameter
                | empty
    '''

def p_llamada_void_3(p):
    '''
    llamada_void_3 : COMMA exp verify_parameter llamada_void_3
                | empty
    '''

def p_not_void(p):
    '''
    not_void : empty
    '''
    global func_dir

    if (func_dir.func_directory[p[-2]]['typeOfR'] == 0):
        raise Exception (" Void functions cannot be called in return statement")
    


def p_verify_func(p):
    '''
    verify_func : empty
    '''
    global func_dir, called_function

    called_function = p[-1]

    if (func_dir.checkFunction(called_function) != True):
        raise Exception ("Called function does not exist")
    
    global cuadruplos, k

    cuadruplos.append(Cuadruplo(150, None, None, called_function))

    k = 1
    

def p_verify_parameter(p):
    '''
    verify_parameter : empty
    '''
    global func_dir, operand_stack, types_stack, called_function, k, cuadruplos

    argument = operand_stack.pop()
    argument_type = types_stack.pop()

    arg_types = func_dir.func_directory[called_function]['params']
    
    try:
        arg_type = arg_types[k-1]
    except:
        raise Exception ("Invalid number of parameters")
    
    if (arg_type != argument_type):
        raise Exception ("Parameter type does not match the specified")
    

    cuadruplos.append(Cuadruplo(155, argument, k-1, "param" + str(k)))

    
    k = k + 1

def p_gosub(p):
    '''
    gosub : empty
    '''
    global called_function, cuadruplos, func_dir, k

    if (k-1 != len(func_dir.getParameters(called_function))):
        raise Exception("Number of parameters do not match with function declaration")

    cuadruplos.append(Cuadruplo(160, called_function, None, None))

def p_add_temp(p):
    '''
    add_temp : empty
    '''
    global called_function, func_dir, cuadruplos, global_vars, types_stack, operand_stack

    typeOfR = func_dir.func_directory[called_function]['typeOfR']
    global_address = global_vars[called_function]['virtual_dir']

    temp_dir = va.getTemporalAddress(called_function, typeOfR)
    
    cuadruplos.append(Cuadruplo(60, global_address, None, temp_dir))

    operand_stack.append(temp_dir)
    types_stack.append(typeOfR)

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
    cuadruplos.append(Cuadruplo(100, None, None, var))

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
    cuadruplos.append(Cuadruplo(105, None, None, op))

    

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
        raise Exception ("Type mismatch in if")
    else:
        result = operand_stack.pop()
        cuadruplos.append(Cuadruplo(135, result, None, None))
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

    cuadruplos.append(Cuadruplo(130, None, None, None))
    false = jump_stack.pop()
    jump_stack.append(len(cuadruplos)-1)
    cuadruplos = fillCuad(false, len(cuadruplos), cuadruplos)

def p_for_l(p):
    '''
    for_l : FOR LPAR ID for_point_1 EQUAL exp for_point_2 TO exp for_point_3 RPAR L_C_BRACKET estatuto for_l_2 R_C_BRACKET SEMICOLON for_point_4
    '''


def p_for_l_2(p):
    '''
    for_l_2 : estatuto for_l_2
                | empty
    '''

def p_for_point_1(p):
    '''
    for_point_1 : empty
    '''
    global operand_stack
    global types_stack
    global func_dir
    global current_function
    
    type = func_dir.getType(current_function, p[-1])
    if ((type != 1)):
        raise Exception ("Type mismatch in for loop, variable must be an integer")
    else:
        operand_stack.append(func_dir.getAddress(current_function, p[-1]))
        types_stack.append(type)

def p_for_point_2(p):
    '''
    for_point_2 : empty
    '''
    global operand_stack
    global types_stack
    global func_dir
    global current_function
    global cuadruplos
    global v_control

    exp_type = types_stack.pop()

    if (exp_type != 1):
        raise Exception ("Type mismatch in for loop, number must be an integer")
    else:
        exp = operand_stack.pop()
        v_control = operand_stack[-1]
        control_type = types_stack[-1]
        try:
            tipo_res = semantic_cube[exp_type][control_type][60]
            cuadruplos.append(Cuadruplo(60, exp, None, v_control))
        except:
            raise Exception ("Type mismatch in for loop")

def p_for_point_3(p):
    '''
    for_point_3 : empty
    '''
    global operand_stack, types_stack, jump_stack, func_dir, current_function, v_control, temp_int_cont

    
    exp_type = types_stack.pop()

    if ((exp_type != 1)):
        raise Exception ("Type mismatch in for loop")
    else:
        exp = operand_stack.pop()
        v_final = va.getTemporalAddress(current_function, 1)
        # temp_int_cont += 1
        cuadruplos.append(Cuadruplo(60, exp, None, v_final))
        
        Tx = va.local_temp_bool
        va.local_temp_bool = va.local_temp_bool + 1

        cuadruplos.append(Cuadruplo(30, v_control, v_final, Tx))

        jump_stack.append(len(cuadruplos) - 1)
        cuadruplos.append(Cuadruplo(135, Tx, None, None))
        jump_stack.append(len(cuadruplos) - 1)

def p_for_point_4(p):
    '''
    for_point_4 : empty
    '''
    global cuadruplos
    global v_control
    global operand_stack
    global jump_stack
    global types_stack
    global current_function

    Ty = va.getTemporalAddress(current_function, 1)
    # constant_table["Ty"] = {'type' : 1, 'virtual_dir' : va.constant_int}
    # va.local_temp_int = va.local_temp_int + 1

    if (constant_table.get(str(1)) != None):
        address = constant_table[str(p[-1])]['virtual_dir']
    else:
        constant_table[str(1)] = {'type' : 1, 'virtual_dir' : va.constant_int}
        address = va.constant_int
        va.constant_int = va.constant_int + 1

    cuadruplos.append(Cuadruplo(10, v_control, address, Ty))
    cuadruplos.append(Cuadruplo(60, Ty, None, v_control))
    cuadruplos.append(Cuadruplo(60, Ty, None, operand_stack[-1]))

    Fin = jump_stack.pop()
    Ret = jump_stack.pop()

    cuadruplos.append(Cuadruplo(130,None, None, Ret))
    cuadruplos = fillCuad(Fin, len(cuadruplos), cuadruplos)

    operand_stack.pop()
    types_stack.pop()


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
        raise Exception ("Type mismatch in while loop")
    else:
        result = operand_stack.pop()
        cuadruplos.append(Cuadruplo(135, result, None, None))
        jump_stack.append(len(cuadruplos)-1)


def p_while_point_3(p):
    '''
    while_point_3 : empty
    '''
    global jump_stack
    global cuadruplos
    end = jump_stack.pop()
    ret = jump_stack.pop()
    cuadruplos.append(Cuadruplo(130,None, None, ret))
    cuadruplos = fillCuad(end, len(cuadruplos), cuadruplos)

def p_return(p):
    '''
    return : RETURN LPAR exp check_valid_func RPAR SEMICOLON
    '''

def p_check_valid_func(p):
    '''
    check_valid_func : empty
    '''
    global current_function, func_dir, return_flag, global_vars
    global types_stack, operand_stack, cuadruplos

    if (func_dir.func_directory[current_function]['typeOfR'] == 0):
        raise Exception ("Void functions cannot have return statement")
    
    return_flag = 1

    op_type = types_stack.pop()
    op = operand_stack.pop()

    
    func_type = func_dir.func_directory[current_function]['typeOfR']
    dir = global_vars[current_function]['virtual_dir']


    if (func_type == op_type):
        cuadruplos.append(Cuadruplo(110, dir, None, op))
    else:
        raise Exception("Ivalid return type")

    





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
                raise Exception ("Type mismatch in addition")
            global current_function
            temp = va.getTemporalAddress(current_function, result_type)

            cuadruplos.append(Cuadruplo(operator, left_operand, right_operand, temp))
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
                raise Exception ("Type mismatch in addition")
            global current_function
            temp = va.getTemporalAddress(current_function, result_type)

            cuadruplos.append(Cuadruplo(operator, left_operand, right_operand, temp))
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
                raise Exception ("Type mismatch in addition")
            global current_function
            temp = va.getTemporalAddress(current_function, result_type)

            cuadruplos.append(Cuadruplo(operator, left_operand, right_operand, temp))
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
                raise Exception ("Type mismatch in addition")
            global current_function
            temp = va.getTemporalAddress(current_function, result_type)

            cuadruplos.append(Cuadruplo(operator, left_operand, right_operand, temp))
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
        types_stack.append(2)
        operand_stack.append(va.constant_float)
        va.constant_float = va.constant_float + 1
    
def p_function(p):
    '''
    function : FUNC function_2 SEMICOLON function_4
    '''

def p_function_2(p):
    '''
    function_2 : function_3 ID function_punto1 LPAR param punto_param_2 RPAR L_C_BRACKET body R_C_BRACKET final_func_point
    '''

def p_function_3(p):
    '''
    function_3 : tipo_simple
                    | VOID
    '''
    if (p[1] == 'void'):
        global current_type
        current_type = 'void'

def p_function_4(p):
    '''
    function_4 : function
                    | empty
    '''

def p_function_punto1(p):
    '''
    function_punto1 : empty
    '''
    global current_type, return_flag, global_vars
    type = traduccion(current_type)

    if (type == 0):
        return_flag = 1
    else:
        return_flag = 0

    func_dir.addFunction(p[-1], type)
    if (type != 0):
        global_dir = va.getAddress('program', type)
        global_vars[p[-1]] = {'type' : type, 'dim' : 0, 'virtual_dir' : global_dir}
    global current_function
    current_function = p[-1]

def p_func_agrega_v(p):
    '''
    func_agrega_v : empty
    '''
    global current_function, cuadruplos
    global local_int_cont, local_float_cont, local_string_cont, local_dataframe_cont

    func_dir.addVariables(current_function, var_list.copy())
    func_dir.func_directory[current_function]['quad_counter'] = len(cuadruplos)
    
    int_cont = va.local_int - local_int_cont 
    float_cont = va.local_float - local_float_cont
    string_cont = va.local_string - local_string_cont
    dataframe_cont =  va.local_dataframe - local_dataframe_cont

    va.local_int = local_int_cont
    va.local_float = local_float_cont
    va.local_string = local_string_cont
    va.local_dataframe = local_dataframe_cont

    func_dir.func_directory[current_function]['num_vars'] = [int_cont, float_cont, string_cont, dataframe_cont]


    var_list.clear()


def p_final_func_point(p):
    '''
    final_func_point : empty
    '''
    global temp_int_cont, temp_float_cont, temp_dataf_cont, temp_bool_cont, temp_string_cont
    global func_dir, current_function, cuadruplos

    if (return_flag == 0):
        raise Exception("Function needs to have at least ONE return")

    temp_addresses = [va.local_temp_int - temp_int_cont, va.local_temp_float-temp_float_cont, va.local_temp_bool - temp_bool_cont, va.local_temp_string - temp_string_cont, va.local_temp_dataframe - temp_dataf_cont]
    func_dir.setTempVars(current_function, temp_addresses)

    va.local_temp_int = temp_int_cont
    va.local_temp_float = temp_float_cont
    va.local_temp_bool = temp_bool_cont
    va.local_temp_dataframe = temp_dataf_cont

    func_dir.func_directory[current_function]['vars'].clear()

    cuadruplos.append(Cuadruplo(145, None, None, None))



def p_empty(p):
    '''
    empty : 
    '''

parser = yacc.yacc()

def test_Parser():
  try:
      test_file = open("./tests/pruebaArreglos.txt", "r")
      test = test_file.read()
      test_file.close()
      print ("Test parser")
      parser.parse(test)
      
  except EOFError:
      raise Exception ("Cannot test parser")

if __name__ == '__main__':
        test_Parser()
        cont = 0
        for element in cuadruplos:
            print (cont)
            cont = cont +1 
            element.print()
        # print(operator_stack, operand_stack, types_stack, jump_stack)
        # func_dir.print()
        # import json
        # json_object = json.dumps(func_dir.func_directory, indent = 2) 
        # print(json_object)
        # print(global_vars)
        # print(constant_table)

        with open('func_dir.pickle', 'wb') as handle:
            pickle.dump(func_dir, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open('constants.pickle', 'wb') as handle:
            pickle.dump(constant_table, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open('global_vars.pickle', 'wb') as handle:
            pickle.dump(global_vars, handle, protocol=pickle.HIGHEST_PROTOCOL)

        with open('cuadruplos.pickle', 'wb') as handle:
            pickle.dump(cuadruplos, handle, protocol=pickle.HIGHEST_PROTOCOL)