# lexer.py imports lex to build the lexer for the compiler
import ply.lex as lex

reserved = {
    'program' : 'PROGRAM',
    'main' : 'MAIN',
    'var' : 'VAR',
    'func' : 'FUNC',
    'return' : 'RETURN',
    # Types
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'string' : 'STRING', #?
    'void' : 'VOID',
    'dataframe' : 'DATAFRAME', #?
    # Conditional
    'if' : 'IF',
    'else' : 'ELSE',
    #Loops
    'while' : 'WHILE',
    'for' : 'FOR',
    'to' : 'TO',
    # Read/Write
    'read' : 'READ',
    'write' : 'WRITE',
}



tokens = [
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'COMMA',
    'SEMICOLON',
    'COLON', #FALTA ESTE
    'LESS_EQUAL',
    'LESS',
    'GREATER_EQUAL',
    'GREATER',
    'NOT_EQUAL',
    'COMPARE',
    'EQUAL',
    'LPAR',
    'RPAR',
    'L_S_BRACKET',
    'R_S_BRACKET',
    'L_C_BRACKET',
    'R_C_BRACKET',
    'AND',
    'OR',
    'CTE_I',
    'CTE_F',
    'CTE_S',
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_LESS_EQUAL = r'<='
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_GREATER = r'>'
t_NOT_EQUAL = r'\!='
t_COMPARE = r'\=='
t_EQUAL = r'\='
t_LPAR = r'\('
t_RPAR = r'\)'
t_L_S_BRACKET = r'\['
t_R_S_BRACKET = r'\]'
t_L_C_BRACKET = r'\{'
t_R_C_BRACKET = r'\}'
t_AND = r'\&&'
t_OR = r'\|\|'

# Ignores spaces and tabs

t_ignore = ' \t \n'

def t_ID(t):
    #primero puede ser _ ?
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_CTE_F(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CTE_I(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_CTE_S(t):
    r'\".*\"'
    return t

def t_error(t):
    print ("Illegal Character")
    t.lexer.skip(1)

lexer = lex.lex()

# test_file = open("./tests/test.txt", "r")
# test = test_file.read()
# test_file.close()

# lex.input(test)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     # print(tok)
    