import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    '''
    program : PROGRAM ID COLON modules main
    '''


def p_modules(p):
    '''
    modules : modules_2 modules_3
    '''

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
    body : vars estatuto body_2
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

def p_tipo_comp(p):
    '''
    tipo_comp : DATAFRAME
    '''

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
    vars_6 : L_S_BRACKET CTE_I R_S_BRACKET vars_7
                | empty
    '''

def p_vars_7(p):
    '''
    vars_7 : L_S_BRACKET CTE_I R_S_BRACKET
                | empty
    '''

def p_vars_8(p):
    '''
    vars_8 : vars 
                | empty
    '''

def p_param(p):
    '''
    param : tipo_simple param_2 ID
                | empty
    '''

def p_param_2(p):
    '''
    param_2 : COMMA tipo_simple
                | empty
    '''

def p_variable(p):
    '''
    variable : ID variable_2
    '''

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
    asigna : variable EQUAL exp SEMICOLON
    '''

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
    read : READ LPAR variable RPAR SEMICOLON
    '''

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
    exp : t_exp exp_2
    '''

def p_exp_2(p):
    '''
    exp_2 : OR exp
            | empty
    '''

def p_t_exp(p):
    '''
    t_exp : g_exp t_exp_2
    '''

def p_t_exp_2(p):
    '''
    t_exp_2 : AND t_exp
                | empty
    '''

def p_g_exp(p):
    '''
    g_exp : m_exp g_exp_2
    '''

def p_g_exp_2(p):
    '''
    g_exp_2 : LESS_EQUAL g_exp_3
                | LESS g_exp_3
                | GREATER_EQUAL g_exp_3
                | GREATER g_exp_3
                | COMPARE g_exp_3
                | NOT_EQUAL g_exp_3
                | empty
    '''

def p_g_exp_3(p):
    '''
    g_exp_3 : m_exp
    '''

def p_m_exp(p):
    '''
    m_exp : t m_exp_2
    '''

def p_m_exp_2(p):
    '''
    m_exp_2 : PLUS m_exp
                | MINUS m_exp
                | empty
    '''

def p_t(p):
    '''
    t : f t_2
    '''

def p_t_2(p):
    '''
    t_2 : TIMES t
            | DIVIDE t
            | empty
    '''

def p_f(p):
    '''
    f : LPAR m_exp RPAR
            | variable
            | llamada
            | f_2
    '''

def p_f_2(p):
    '''
    f_2 : CTE_I
            | CTE_F
    '''

def p_function(p):
    '''
    function : FUNC function_2 SEMICOLON
    '''

def p_function_2(p):
    '''
    function_2 : tipo_simple ID LPAR param RPAR L_C_BRACKET body RETURN LPAR exp RPAR SEMICOLON R_C_BRACKET
                    | VOID ID LPAR param RPAR L_C_BRACKET body R_C_BRACKET
    '''

def p_empty(p):
    '''
    empty : 
    '''

parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)