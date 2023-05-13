# {
#     Tipos:
#     0 void
#     1 int
#     2 float
#     3 bool
#     4 char

#     5 +
#     10 -
#     15 *
#     20 /
#     25 <
#     30 <=
#     35 ==
#     40 >
#     45 >=
#     50 !=
#     55 =
#     60 &&
#     65 ||
#     70 (
#     75 )
{
    # 100 : GOTO
    # 105 : GOTOF
    # 110 : GOTOV
}
# }

# Funcion para traducir de string a valor numerico
def traduccion(symbol):
    symbol = str(symbol)
    if symbol == 'void' : return 0
    elif symbol == 'int' : return 1
    elif symbol == 'float' : return 2
    elif symbol == 'bool' : return 3
    elif symbol == 'char' : return 4
    elif symbol == '+' : return 5
    elif symbol == '-' : return 10
    elif symbol == '*' : return 15
    elif symbol == '/' : return 20
    elif symbol == '<' : return 25
    elif symbol == '<=' : return 30
    elif symbol == '==' : return 35
    elif symbol == '>' : return 40
    elif symbol == '>=' : return 45
    elif symbol == '!=' : return 50
    elif symbol == '=' : return 55
    elif symbol == '&&' : return 60
    elif symbol == '||' : return 65
    else: return "Not valid type"
    


# Agregar != == a float/int con bool?

semantic_cube = {
    1 : {
        1 : {
            5 : 1 ,
            10 : 1,
            15 : 1,
            20 : 1,
            25 : 3,
            30 : 3,
            35 : 3,
            40 : 3,
            45 : 3,
            50 : 3,
            55 : 1
        },

        2: {
            5 : 2 ,
            10 : 2,
            15 : 2,
            20 : 2,
            25 : 3,
            30 : 3,
            35 : 3,
            40 : 3,
            45 : 3,
            50 : 3,
            55 : 2
        }
    },
    2 : {
        1 : {
            5 : 2 ,
            10 : 2,
            15 : 2,
            20 : 2,
            25 : 3,
            30 : 3,
            35 : 3,
            40 : 3,
            45 : 3,
            50 : 3,
            55 : 2
        },

        2: {
            5 : 2 ,
            10 : 2,
            15 : 2,
            20 : 2,
            25 : 3,
            30 : 3,
            35 : 3,
            40 : 3,
            45 : 3,
            50 : 3,
            55 : 2
        }
    },
    3 : {
        3 : {
            35 : 3,
            50 : 3,
            55 : 3,
            60 : 3,
            65 : 3
        }
    },
    4 : {
        4 : {
            35 : 3,
            50 : 3,
            55 : 4
        }
    }
}
