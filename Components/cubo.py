# {
#     Tipos:
#     0 void
#     1 int
#     2 float
#     3 bool
#     4 string
#     5 dataframe

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
#     75 (
#     80 )
{
    # 100 : READ
    # 105 : WRITE
    # 110 : RETURN
    # 115 : VER
    # 130 : GOTO
    # 135 : GOTOF
    # 140 : GOTOV
    # 145 ENDFUNC
    # 150 ERA
    # 155 PARAMETER
    # 160 GOSUB

    # 200 : READ_CSV
    # 205 : MEAN
    # 210 : MODE
    # 215 : MEDIAN
    # 220 : LINEAR REGR
    # 225 : BOX PLOT
    # 230 : HISTOGRAM

}
# }

# Funcion para traducir de string a valor numerico
def traduccion(symbol):
    symbol = str(symbol)
    if symbol == 'void' : return 0
    elif symbol == 'int' : return 1
    elif symbol == 'float' : return 2
    elif symbol == 'bool' : return 3
    elif symbol == 'string' : return 4
    elif symbol == 'dataframe' : return 5
    elif symbol == '+' : return 10
    elif symbol == '-' : return 15
    elif symbol == '*' : return 20
    elif symbol == '/' : return 25
    elif symbol == '<' : return 30
    elif symbol == '<=' : return 35
    elif symbol == '==' : return 40
    elif symbol == '>' : return 45
    elif symbol == '>=' : return 50
    elif symbol == '!=' : return 55
    elif symbol == '=' : return 60
    elif symbol == '&&' : return 65
    elif symbol == '||' : return 70
    else: return "Not valid type"
    

semantic_cube = {
    1 : {
        1 : {
            10 : 1 ,
            15 : 1,
            20 : 1,
            25 : 1,
            30 : 3,
            35 : 3,
            40 : 3,
            45 : 3,
            50 : 3,
            55 : 3,
            60 : 1
        },

        2: {
            10 : 2 ,
            15 : 2,
            20 : 2,
            25 : 2,
            30 : 3,
            35 : 3,
            40 : 3,
            45 : 3,
            50 : 3,
            55 : 3
        }
    },
    2 : {
        1 : {
            10 : 2 ,
            15 : 2,
            20 : 2,
            25 : 2,
            30 : 3,
            35 : 3,
            40 : 3,
            45 : 3,
            50 : 3,
            55 : 3,
            60 : 2
        },

        2: {
            10 : 2 ,
            15 : 2,
            20 : 2,
            25 : 2,
            30 : 3,
            35 : 3,
            40 : 3,
            45 : 3,
            50 : 3,
            55 : 3,
            60 : 2
        }
    },
    3 : {
        3 : {
            40 : 3,
            55 : 3,
            60 : 3,
            65 : 3,
            70 : 3
        }
    },
    4 : {
        4 : {
            40 : 3,
            55 : 3,
            60 : 4
        }
    }
}
