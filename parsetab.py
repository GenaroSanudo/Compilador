
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COLON COMMA COMPARE CTE_F CTE_I CTE_S DATAFRAME DIVIDE ELSE EQUAL FLOAT FOR FUNC GREATER GREATER_EQUAL ID IF INT LESS LESS_EQUAL LPAR L_C_BRACKET L_S_BRACKET MAIN MINUS NOT_EQUAL OR PLUS PROGRAM READ RETURN RPAR R_C_BRACKET R_S_BRACKET SEMICOLON STRING TIMES TO VAR VOID WHILE WRITE\n    program : PROGRAM program_point ID COLON modules main\n    \n    program_point : empty\n    \n    modules : modules_2 modules_point modules_3\n    \n    modules_point : empty\n    \n    modules_2 : vars\n                | empty\n    \n    modules_3 : function\n                    | empty\n    \n    main : MAIN LPAR RPAR L_C_BRACKET body R_C_BRACKET SEMICOLON\n    \n    body : vars estatuto body_2\n    \n    body_2 : estatuto body_2\n                | empty\n    \n    tipo_simple : INT \n                | FLOAT\n                | CHAR\n    \n    tipo_comp : DATAFRAME\n    \n    vars : VAR vars_2 SEMICOLON vars_8\n    \n    vars_2 : tipo_comp vars_3\n                        | tipo_simple vars_4\n    \n    vars_3 : ID vars_5\n    \n    vars_4 : vars_3 \n                | ID vars_6\n    \n    vars_5 : COMMA vars_3\n            | empty\n    \n    vars_6 : punto_id_especial L_S_BRACKET CTE_I R_S_BRACKET vars_7\n                | empty\n    \n    punto_id_especial : empty\n    \n    vars_7 : L_S_BRACKET CTE_I R_S_BRACKET var_mat\n                | var_array\n    \n    var_array : empty\n    \n    var_mat : empty\n    \n    vars_8 : vars \n                | empty\n    \n    param : tipo_simple param_2 punto_param ID\n                | empty\n    \n    param_2 : COMMA param\n    \n    punto_param : empty\n    \n    variable : ID variable_2\n    \n    variable_2 : L_S_BRACKET exp R_S_BRACKET variable_3 \n                    | empty\n    \n    variable_3 : L_S_BRACKET exp R_S_BRACKET\n                    | empty\n    \n    estatuto : asigna\n                | llamada\n                | read\n                | write\n                | if_1\n                | for_l\n                | while_l\n                | func_extra\n    \n    asigna : variable EQUAL exp SEMICOLON\n    \n    llamada : ID LPAR exp llamada_2 RPAR SEMICOLON\n    \n    llamada_2 : COMMA exp llamada_2 \n                | empty\n    \n    read : READ LPAR variable RPAR SEMICOLON\n    \n    write : WRITE LPAR write_2 write_3 RPAR SEMICOLON\n    \n    write_2 : exp\n                | CTE_S\n    \n    write_3 : COMMA write_2 write_3 \n                | empty\n    \n    if_1 : IF LPAR exp RPAR L_C_BRACKET estatuto if_2 R_C_BRACKET if_3 SEMICOLON\n    \n    if_2 : estatuto if_2 \n            | empty\n    \n    if_3 : ELSE L_C_BRACKET estatuto if_2 R_C_BRACKET\n    \n    for_l : FOR LPAR ID RPAR EQUAL exp TO exp RPAR L_C_BRACKET estatuto for_l_2 R_C_BRACKET SEMICOLON\n    \n    for_l_2 : estatuto for_l_2\n                | empty\n    \n    while_l : WHILE LPAR exp RPAR L_C_BRACKET estatuto while_l_2 R_C_BRACKET SEMICOLON\n    \n    while_l_2 : estatuto while_l_2\n                    | empty\n    \n    func_extra : empty\n    \n    exp : t_exp exp_2\n    \n    exp_2 : OR exp\n            | empty\n    \n    t_exp : g_exp t_exp_2\n    \n    t_exp_2 : AND t_exp\n                | empty\n    \n    g_exp : m_exp g_exp_2\n    \n    g_exp_2 : LESS_EQUAL g_exp_3\n                | LESS g_exp_3\n                | GREATER_EQUAL g_exp_3\n                | GREATER g_exp_3\n                | COMPARE g_exp_3\n                | NOT_EQUAL g_exp_3\n                | empty\n    \n    g_exp_3 : m_exp\n    \n    m_exp : t m_exp_2\n    \n    m_exp_2 : PLUS m_exp\n                | MINUS m_exp\n                | empty\n    \n    t : f t_2\n    \n    t_2 : TIMES t\n            | DIVIDE t\n            | empty\n    \n    f : LPAR m_exp RPAR\n            | variable\n            | llamada\n            | f_2\n    \n    f_2 : CTE_I\n            | CTE_F\n    \n    function : FUNC function_2 SEMICOLON\n    \n    function_2 : tipo_simple ID LPAR param RPAR L_C_BRACKET body RETURN LPAR exp RPAR SEMICOLON R_C_BRACKET \n                    | VOID ID LPAR param RPAR L_C_BRACKET body R_C_BRACKET\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,12,81,],[0,-1,-9,]),'ID':([2,3,4,17,18,19,20,21,22,28,36,37,38,39,40,42,54,59,60,61,62,63,64,65,66,67,75,78,82,84,85,86,88,90,91,92,93,94,95,96,111,127,128,129,133,135,138,141,142,143,144,145,146,149,150,153,154,158,163,168,188,191,194,195,196,201,204,206,208,209,211,213,214,215,217,228,230,231,232,234,235,237,239,243,],[-104,5,-2,30,33,-16,-13,-14,-15,-104,49,50,-17,-32,-33,30,69,69,-43,-44,-45,-46,-47,-48,-49,-50,-71,-35,69,-71,114,114,114,120,114,114,125,114,-104,-104,114,168,-37,-36,-51,114,114,114,114,114,114,114,114,114,114,114,114,114,114,-34,114,-55,69,114,69,-52,-56,69,69,114,69,-71,114,69,-71,-68,-61,69,69,69,69,69,-71,-65,]),'COLON':([5,],[6,]),'VAR':([6,28,47,130,131,],[11,11,11,11,11,]),'FUNC':([6,8,9,10,14,15,28,38,39,40,],[-104,-104,-5,-6,27,-4,-104,-17,-32,-33,]),'MAIN':([6,7,8,9,10,14,15,24,25,26,28,38,39,40,48,],[-104,13,-104,-5,-6,-104,-4,-3,-7,-8,-104,-17,-32,-33,-101,]),'DATAFRAME':([11,],[19,]),'INT':([11,27,55,56,96,],[20,20,20,20,20,]),'FLOAT':([11,27,55,56,96,],[21,21,21,21,21,]),'CHAR':([11,27,55,56,96,],[22,22,22,22,22,]),'LPAR':([13,49,50,69,70,71,72,73,74,85,86,88,91,92,94,111,114,135,138,141,142,143,144,145,146,149,150,153,154,158,163,188,195,197,209,214,],[23,55,56,86,90,91,92,93,94,111,111,111,111,111,111,111,86,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,209,111,111,]),'SEMICOLON':([16,29,30,31,32,33,35,41,43,44,46,51,58,80,87,89,100,101,102,104,105,106,107,108,109,110,112,113,114,115,116,134,136,137,139,140,147,148,151,152,155,160,161,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,189,190,192,198,199,200,201,210,223,224,225,233,240,242,],[28,-18,-104,-19,-21,-104,48,-20,-24,-22,-24,-23,81,-104,-38,-40,-25,-29,-30,-96,133,-104,-104,-104,-104,-104,-97,-98,-104,-99,-100,-72,-74,-75,-77,-78,-85,-87,-90,-91,-94,-104,191,-104,-73,-76,-79,-86,-80,-81,-82,-83,-84,-88,-89,-92,-93,-95,201,-39,-42,204,-103,-28,-31,-52,-41,228,229,230,-102,-64,243,]),'COMMA':([20,21,22,30,33,76,87,89,104,106,107,108,109,110,112,113,114,115,116,117,121,122,123,134,136,137,139,140,147,148,151,152,155,160,172,173,174,175,176,177,178,179,180,181,182,183,184,185,187,189,190,193,201,210,],[-13,-14,-15,42,42,96,-38,-40,-96,-104,-104,-104,-104,-104,-97,-98,-104,-99,-100,158,163,-57,-58,-72,-74,-75,-77,-78,-85,-87,-90,-91,-94,-104,-73,-76,-79,-86,-80,-81,-82,-83,-84,-88,-89,-92,-93,-95,158,-39,-42,163,-52,-41,]),'RPAR':([23,55,56,77,78,79,87,89,104,106,107,108,109,110,112,113,114,115,116,117,119,120,121,122,123,124,125,126,134,136,137,139,140,147,148,151,152,155,156,157,159,160,162,164,168,172,173,174,175,176,177,178,179,180,181,182,183,184,185,187,189,190,193,201,202,205,210,218,221,],[34,-104,-104,97,-35,98,-38,-40,-96,-104,-104,-104,-104,-104,-97,-98,-104,-99,-100,-104,161,-104,-104,-57,-58,165,166,167,-72,-74,-75,-77,-78,-85,-87,-90,-91,-94,185,186,-54,-104,192,-60,-34,-73,-76,-79,-86,-80,-81,-82,-83,-84,-88,-89,-92,-93,-95,-104,-39,-42,-104,-52,-53,-59,-41,224,227,]),'VOID':([27,],[37,]),'READ':([28,38,39,40,54,59,60,61,62,63,64,65,66,67,75,82,84,133,191,194,196,201,204,206,208,211,213,215,217,228,230,231,232,234,235,237,239,243,],[-104,-17,-32,-33,70,70,-43,-44,-45,-46,-47,-48,-49,-50,-71,70,-71,-51,-55,70,70,-52,-56,70,70,70,-71,70,-71,-68,-61,70,70,70,70,70,-71,-65,]),'WRITE':([28,38,39,40,54,59,60,61,62,63,64,65,66,67,75,82,84,133,191,194,196,201,204,206,208,211,213,215,217,228,230,231,232,234,235,237,239,243,],[-104,-17,-32,-33,71,71,-43,-44,-45,-46,-47,-48,-49,-50,-71,71,-71,-51,-55,71,71,-52,-56,71,71,71,-71,71,-71,-68,-61,71,71,71,71,71,-71,-65,]),'IF':([28,38,39,40,54,59,60,61,62,63,64,65,66,67,75,82,84,133,191,194,196,201,204,206,208,211,213,215,217,228,230,231,232,234,235,237,239,243,],[-104,-17,-32,-33,72,72,-43,-44,-45,-46,-47,-48,-49,-50,-71,72,-71,-51,-55,72,72,-52,-56,72,72,72,-71,72,-71,-68,-61,72,72,72,72,72,-71,-65,]),'FOR':([28,38,39,40,54,59,60,61,62,63,64,65,66,67,75,82,84,133,191,194,196,201,204,206,208,211,213,215,217,228,230,231,232,234,235,237,239,243,],[-104,-17,-32,-33,73,73,-43,-44,-45,-46,-47,-48,-49,-50,-71,73,-71,-51,-55,73,73,-52,-56,73,73,73,-71,73,-71,-68,-61,73,73,73,73,73,-71,-65,]),'WHILE':([28,38,39,40,54,59,60,61,62,63,64,65,66,67,75,82,84,133,191,194,196,201,204,206,208,211,213,215,217,228,230,231,232,234,235,237,239,243,],[-104,-17,-32,-33,74,74,-43,-44,-45,-46,-47,-48,-49,-50,-71,74,-71,-51,-55,74,74,-52,-56,74,74,74,-71,74,-71,-68,-61,74,74,74,74,74,-71,-65,]),'R_C_BRACKET':([28,38,39,40,53,54,59,60,61,62,63,64,65,66,67,75,82,83,84,103,133,170,191,194,196,201,204,206,208,211,212,213,215,216,217,219,222,228,229,230,231,232,234,235,236,237,238,239,241,243,],[-104,-17,-32,-33,58,-104,-104,-43,-44,-45,-46,-47,-48,-49,-50,-71,-104,-10,-12,-11,-51,198,-55,-104,-104,-52,-56,-104,-104,-104,220,-63,-104,223,-70,-62,-69,-68,233,-61,-104,-104,-104,-104,240,-104,242,-67,-66,-65,]),'RETURN':([28,38,39,40,54,59,60,61,62,63,64,65,66,67,75,82,83,84,103,133,169,191,201,204,228,230,243,],[-104,-17,-32,-33,-104,-104,-43,-44,-45,-46,-47,-48,-49,-50,-71,-104,-10,-12,-11,-51,197,-55,-52,-56,-68,-61,-65,]),'L_S_BRACKET':([33,45,46,69,80,114,120,160,],[-104,52,-27,88,99,88,88,188,]),'L_C_BRACKET':([34,97,98,165,167,226,227,],[47,130,131,194,196,231,232,]),'CTE_I':([52,85,86,88,91,92,94,99,111,135,138,141,142,143,144,145,146,149,150,153,154,158,163,188,195,209,214,],[57,115,115,115,115,115,115,132,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,]),'R_S_BRACKET':([57,87,89,104,106,107,108,109,110,112,113,114,115,116,118,132,134,136,137,139,140,147,148,151,152,155,160,172,173,174,175,176,177,178,179,180,181,182,183,184,185,189,190,201,203,210,],[80,-38,-40,-96,-104,-104,-104,-104,-104,-97,-98,-104,-99,-100,160,171,-72,-74,-75,-77,-78,-85,-87,-90,-91,-94,-104,-73,-76,-79,-86,-80,-81,-82,-83,-84,-88,-89,-92,-93,-95,-39,-42,-52,210,-41,]),'EQUAL':([68,69,87,89,160,166,189,190,210,],[85,-104,-38,-40,-104,195,-39,-42,-41,]),'CTE_F':([85,86,88,91,92,94,111,135,138,141,142,143,144,145,146,149,150,153,154,158,163,188,195,209,214,],[116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,]),'TIMES':([87,89,104,110,112,113,114,115,116,160,185,189,190,201,210,],[-38,-40,-96,153,-97,-98,-104,-99,-100,-104,-95,-39,-42,-52,-41,]),'DIVIDE':([87,89,104,110,112,113,114,115,116,160,185,189,190,201,210,],[-38,-40,-96,154,-97,-98,-104,-99,-100,-104,-95,-39,-42,-52,-41,]),'PLUS':([87,89,104,109,110,112,113,114,115,116,152,155,160,183,184,185,189,190,201,210,],[-38,-40,-96,149,-104,-97,-98,-104,-99,-100,-91,-94,-104,-92,-93,-95,-39,-42,-52,-41,]),'MINUS':([87,89,104,109,110,112,113,114,115,116,152,155,160,183,184,185,189,190,201,210,],[-38,-40,-96,150,-104,-97,-98,-104,-99,-100,-91,-94,-104,-92,-93,-95,-39,-42,-52,-41,]),'LESS_EQUAL':([87,89,104,108,109,110,112,113,114,115,116,148,151,152,155,160,181,182,183,184,185,189,190,201,210,],[-38,-40,-96,141,-104,-104,-97,-98,-104,-99,-100,-87,-90,-91,-94,-104,-88,-89,-92,-93,-95,-39,-42,-52,-41,]),'LESS':([87,89,104,108,109,110,112,113,114,115,116,148,151,152,155,160,181,182,183,184,185,189,190,201,210,],[-38,-40,-96,142,-104,-104,-97,-98,-104,-99,-100,-87,-90,-91,-94,-104,-88,-89,-92,-93,-95,-39,-42,-52,-41,]),'GREATER_EQUAL':([87,89,104,108,109,110,112,113,114,115,116,148,151,152,155,160,181,182,183,184,185,189,190,201,210,],[-38,-40,-96,143,-104,-104,-97,-98,-104,-99,-100,-87,-90,-91,-94,-104,-88,-89,-92,-93,-95,-39,-42,-52,-41,]),'GREATER':([87,89,104,108,109,110,112,113,114,115,116,148,151,152,155,160,181,182,183,184,185,189,190,201,210,],[-38,-40,-96,144,-104,-104,-97,-98,-104,-99,-100,-87,-90,-91,-94,-104,-88,-89,-92,-93,-95,-39,-42,-52,-41,]),'COMPARE':([87,89,104,108,109,110,112,113,114,115,116,148,151,152,155,160,181,182,183,184,185,189,190,201,210,],[-38,-40,-96,145,-104,-104,-97,-98,-104,-99,-100,-87,-90,-91,-94,-104,-88,-89,-92,-93,-95,-39,-42,-52,-41,]),'NOT_EQUAL':([87,89,104,108,109,110,112,113,114,115,116,148,151,152,155,160,181,182,183,184,185,189,190,201,210,],[-38,-40,-96,146,-104,-104,-97,-98,-104,-99,-100,-87,-90,-91,-94,-104,-88,-89,-92,-93,-95,-39,-42,-52,-41,]),'AND':([87,89,104,107,108,109,110,112,113,114,115,116,140,147,148,151,152,155,160,174,175,176,177,178,179,180,181,182,183,184,185,189,190,201,210,],[-38,-40,-96,138,-104,-104,-104,-97,-98,-104,-99,-100,-78,-85,-87,-90,-91,-94,-104,-79,-86,-80,-81,-82,-83,-84,-88,-89,-92,-93,-95,-39,-42,-52,-41,]),'OR':([87,89,104,106,107,108,109,110,112,113,114,115,116,137,139,140,147,148,151,152,155,160,173,174,175,176,177,178,179,180,181,182,183,184,185,189,190,201,210,],[-38,-40,-96,135,-104,-104,-104,-104,-97,-98,-104,-99,-100,-75,-77,-78,-85,-87,-90,-91,-94,-104,-76,-79,-86,-80,-81,-82,-83,-84,-88,-89,-92,-93,-95,-39,-42,-52,-41,]),'TO':([87,89,104,106,107,108,109,110,112,113,114,115,116,134,136,137,139,140,147,148,151,152,155,160,172,173,174,175,176,177,178,179,180,181,182,183,184,185,189,190,201,207,210,],[-38,-40,-96,-104,-104,-104,-104,-104,-97,-98,-104,-99,-100,-72,-74,-75,-77,-78,-85,-87,-90,-91,-94,-104,-73,-76,-79,-86,-80,-81,-82,-83,-84,-88,-89,-92,-93,-95,-39,-42,-52,214,-41,]),'CTE_S':([91,163,],[123,123,]),'ELSE':([220,],[226,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_point':([2,],[3,]),'empty':([2,6,8,14,28,30,33,54,55,56,59,69,80,82,95,96,106,107,108,109,110,114,117,120,121,160,171,187,193,194,196,206,208,211,215,231,232,234,235,237,],[4,10,15,26,40,43,46,75,78,78,84,89,102,84,128,78,136,139,147,151,155,89,159,89,164,190,200,159,164,75,75,213,217,213,217,75,75,213,239,239,]),'modules':([6,],[7,]),'modules_2':([6,],[8,]),'vars':([6,28,47,130,131,],[9,39,54,54,54,]),'main':([7,],[12,]),'modules_point':([8,],[14,]),'vars_2':([11,],[16,]),'tipo_comp':([11,],[17,]),'tipo_simple':([11,27,55,56,96,],[18,36,76,76,76,]),'modules_3':([14,],[24,]),'function':([14,],[25,]),'vars_3':([17,18,42,],[29,32,51,]),'vars_4':([18,],[31,]),'function_2':([27,],[35,]),'vars_8':([28,],[38,]),'vars_5':([30,33,],[41,41,]),'vars_6':([33,],[44,]),'punto_id_especial':([33,],[45,]),'body':([47,130,131,],[53,169,170,]),'estatuto':([54,59,82,194,196,206,208,211,215,231,232,234,235,237,],[59,82,82,206,208,211,215,211,215,234,235,211,237,237,]),'asigna':([54,59,82,194,196,206,208,211,215,231,232,234,235,237,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'llamada':([54,59,82,85,86,88,91,92,94,111,135,138,141,142,143,144,145,146,149,150,153,154,158,163,188,194,195,196,206,208,209,211,214,215,231,232,234,235,237,],[61,61,61,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,61,112,61,61,61,112,61,112,61,61,61,61,61,61,]),'read':([54,59,82,194,196,206,208,211,215,231,232,234,235,237,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'write':([54,59,82,194,196,206,208,211,215,231,232,234,235,237,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'if_1':([54,59,82,194,196,206,208,211,215,231,232,234,235,237,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'for_l':([54,59,82,194,196,206,208,211,215,231,232,234,235,237,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'while_l':([54,59,82,194,196,206,208,211,215,231,232,234,235,237,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'func_extra':([54,59,82,194,196,206,208,211,215,231,232,234,235,237,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'variable':([54,59,82,85,86,88,90,91,92,94,111,135,138,141,142,143,144,145,146,149,150,153,154,158,163,188,194,195,196,206,208,209,211,214,215,231,232,234,235,237,],[68,68,68,104,104,104,119,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,68,104,68,68,68,104,68,104,68,68,68,68,68,68,]),'param':([55,56,96,],[77,79,129,]),'body_2':([59,82,],[83,103,]),'variable_2':([69,114,120,],[87,87,87,]),'param_2':([76,],[95,]),'vars_7':([80,],[100,]),'var_array':([80,],[101,]),'exp':([85,86,88,91,92,94,135,158,163,188,195,209,214,],[105,117,118,122,124,126,172,187,122,203,207,218,221,]),'t_exp':([85,86,88,91,92,94,135,138,158,163,188,195,209,214,],[106,106,106,106,106,106,106,173,106,106,106,106,106,106,]),'g_exp':([85,86,88,91,92,94,135,138,158,163,188,195,209,214,],[107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'m_exp':([85,86,88,91,92,94,111,135,138,141,142,143,144,145,146,149,150,158,163,188,195,209,214,],[108,108,108,108,108,108,156,108,108,175,175,175,175,175,175,181,182,108,108,108,108,108,108,]),'t':([85,86,88,91,92,94,111,135,138,141,142,143,144,145,146,149,150,153,154,158,163,188,195,209,214,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,183,184,109,109,109,109,109,109,]),'f':([85,86,88,91,92,94,111,135,138,141,142,143,144,145,146,149,150,153,154,158,163,188,195,209,214,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,]),'f_2':([85,86,88,91,92,94,111,135,138,141,142,143,144,145,146,149,150,153,154,158,163,188,195,209,214,],[113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,]),'write_2':([91,163,],[121,193,]),'punto_param':([95,],[127,]),'exp_2':([106,],[134,]),'t_exp_2':([107,],[137,]),'g_exp_2':([108,],[140,]),'m_exp_2':([109,],[148,]),'t_2':([110,],[152,]),'llamada_2':([117,187,],[157,202,]),'write_3':([121,193,],[162,205,]),'g_exp_3':([141,142,143,144,145,146,],[174,176,177,178,179,180,]),'variable_3':([160,],[189,]),'var_mat':([171,],[199,]),'if_2':([206,211,234,],[212,219,236,]),'while_l_2':([208,215,],[216,222,]),'if_3':([220,],[225,]),'for_l_2':([235,237,],[238,241,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM program_point ID COLON modules main','program',6,'p_program','parser_1.py',17),
  ('program_point -> empty','program_point',1,'p_program_point','parser_1.py',22),
  ('modules -> modules_2 modules_point modules_3','modules',3,'p_modules','parser_1.py',29),
  ('modules_point -> empty','modules_point',1,'p_modules_point','parser_1.py',34),
  ('modules_2 -> vars','modules_2',1,'p_modules_2','parser_1.py',48),
  ('modules_2 -> empty','modules_2',1,'p_modules_2','parser_1.py',49),
  ('modules_3 -> function','modules_3',1,'p_modules_3','parser_1.py',54),
  ('modules_3 -> empty','modules_3',1,'p_modules_3','parser_1.py',55),
  ('main -> MAIN LPAR RPAR L_C_BRACKET body R_C_BRACKET SEMICOLON','main',7,'p_main','parser_1.py',60),
  ('body -> vars estatuto body_2','body',3,'p_body','parser_1.py',65),
  ('body_2 -> estatuto body_2','body_2',2,'p_body_2','parser_1.py',71),
  ('body_2 -> empty','body_2',1,'p_body_2','parser_1.py',72),
  ('tipo_simple -> INT','tipo_simple',1,'p_tipo_simple','parser_1.py',77),
  ('tipo_simple -> FLOAT','tipo_simple',1,'p_tipo_simple','parser_1.py',78),
  ('tipo_simple -> CHAR','tipo_simple',1,'p_tipo_simple','parser_1.py',79),
  ('tipo_comp -> DATAFRAME','tipo_comp',1,'p_tipo_comp','parser_1.py',87),
  ('vars -> VAR vars_2 SEMICOLON vars_8','vars',4,'p_vars','parser_1.py',95),
  ('vars_2 -> tipo_comp vars_3','vars_2',2,'p_vars_2','parser_1.py',101),
  ('vars_2 -> tipo_simple vars_4','vars_2',2,'p_vars_2','parser_1.py',102),
  ('vars_3 -> ID vars_5','vars_3',2,'p_vars_3','parser_1.py',107),
  ('vars_4 -> vars_3','vars_4',1,'p_vars_4','parser_1.py',116),
  ('vars_4 -> ID vars_6','vars_4',2,'p_vars_4','parser_1.py',117),
  ('vars_5 -> COMMA vars_3','vars_5',2,'p_vars_5','parser_1.py',122),
  ('vars_5 -> empty','vars_5',1,'p_vars_5','parser_1.py',123),
  ('vars_6 -> punto_id_especial L_S_BRACKET CTE_I R_S_BRACKET vars_7','vars_6',5,'p_vars_6','parser_1.py',128),
  ('vars_6 -> empty','vars_6',1,'p_vars_6','parser_1.py',129),
  ('punto_id_especial -> empty','punto_id_especial',1,'p_punto_id_especial','parser_1.py',133),
  ('vars_7 -> L_S_BRACKET CTE_I R_S_BRACKET var_mat','vars_7',4,'p_vars_7','parser_1.py',140),
  ('vars_7 -> var_array','vars_7',1,'p_vars_7','parser_1.py',141),
  ('var_array -> empty','var_array',1,'p_var_array','parser_1.py',147),
  ('var_mat -> empty','var_mat',1,'p_var_mat','parser_1.py',157),
  ('vars_8 -> vars','vars_8',1,'p_vars_8','parser_1.py',168),
  ('vars_8 -> empty','vars_8',1,'p_vars_8','parser_1.py',169),
  ('param -> tipo_simple param_2 punto_param ID','param',4,'p_param','parser_1.py',174),
  ('param -> empty','param',1,'p_param','parser_1.py',175),
  ('param_2 -> COMMA param','param_2',2,'p_param_2','parser_1.py',180),
  ('punto_param -> empty','punto_param',1,'p_punto_param','parser_1.py',185),
  ('variable -> ID variable_2','variable',2,'p_variable','parser_1.py',191),
  ('variable_2 -> L_S_BRACKET exp R_S_BRACKET variable_3','variable_2',4,'p_variable_2','parser_1.py',196),
  ('variable_2 -> empty','variable_2',1,'p_variable_2','parser_1.py',197),
  ('variable_3 -> L_S_BRACKET exp R_S_BRACKET','variable_3',3,'p_variable_3','parser_1.py',202),
  ('variable_3 -> empty','variable_3',1,'p_variable_3','parser_1.py',203),
  ('estatuto -> asigna','estatuto',1,'p_estatuto','parser_1.py',208),
  ('estatuto -> llamada','estatuto',1,'p_estatuto','parser_1.py',209),
  ('estatuto -> read','estatuto',1,'p_estatuto','parser_1.py',210),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser_1.py',211),
  ('estatuto -> if_1','estatuto',1,'p_estatuto','parser_1.py',212),
  ('estatuto -> for_l','estatuto',1,'p_estatuto','parser_1.py',213),
  ('estatuto -> while_l','estatuto',1,'p_estatuto','parser_1.py',214),
  ('estatuto -> func_extra','estatuto',1,'p_estatuto','parser_1.py',215),
  ('asigna -> variable EQUAL exp SEMICOLON','asigna',4,'p_asigna','parser_1.py',220),
  ('llamada -> ID LPAR exp llamada_2 RPAR SEMICOLON','llamada',6,'p_llamada','parser_1.py',225),
  ('llamada_2 -> COMMA exp llamada_2','llamada_2',3,'p_llamada_2','parser_1.py',230),
  ('llamada_2 -> empty','llamada_2',1,'p_llamada_2','parser_1.py',231),
  ('read -> READ LPAR variable RPAR SEMICOLON','read',5,'p_read','parser_1.py',236),
  ('write -> WRITE LPAR write_2 write_3 RPAR SEMICOLON','write',6,'p_write','parser_1.py',241),
  ('write_2 -> exp','write_2',1,'p_write_2','parser_1.py',246),
  ('write_2 -> CTE_S','write_2',1,'p_write_2','parser_1.py',247),
  ('write_3 -> COMMA write_2 write_3','write_3',3,'p_write_3','parser_1.py',252),
  ('write_3 -> empty','write_3',1,'p_write_3','parser_1.py',253),
  ('if_1 -> IF LPAR exp RPAR L_C_BRACKET estatuto if_2 R_C_BRACKET if_3 SEMICOLON','if_1',10,'p_if_1','parser_1.py',258),
  ('if_2 -> estatuto if_2','if_2',2,'p_if_2','parser_1.py',263),
  ('if_2 -> empty','if_2',1,'p_if_2','parser_1.py',264),
  ('if_3 -> ELSE L_C_BRACKET estatuto if_2 R_C_BRACKET','if_3',5,'p_if_3','parser_1.py',269),
  ('for_l -> FOR LPAR ID RPAR EQUAL exp TO exp RPAR L_C_BRACKET estatuto for_l_2 R_C_BRACKET SEMICOLON','for_l',14,'p_for_l','parser_1.py',274),
  ('for_l_2 -> estatuto for_l_2','for_l_2',2,'p_for_l_2','parser_1.py',279),
  ('for_l_2 -> empty','for_l_2',1,'p_for_l_2','parser_1.py',280),
  ('while_l -> WHILE LPAR exp RPAR L_C_BRACKET estatuto while_l_2 R_C_BRACKET SEMICOLON','while_l',9,'p_while_l','parser_1.py',285),
  ('while_l_2 -> estatuto while_l_2','while_l_2',2,'p_while_l_2','parser_1.py',290),
  ('while_l_2 -> empty','while_l_2',1,'p_while_l_2','parser_1.py',291),
  ('func_extra -> empty','func_extra',1,'p_func_extra','parser_1.py',296),
  ('exp -> t_exp exp_2','exp',2,'p_exp','parser_1.py',301),
  ('exp_2 -> OR exp','exp_2',2,'p_exp_2','parser_1.py',306),
  ('exp_2 -> empty','exp_2',1,'p_exp_2','parser_1.py',307),
  ('t_exp -> g_exp t_exp_2','t_exp',2,'p_t_exp','parser_1.py',312),
  ('t_exp_2 -> AND t_exp','t_exp_2',2,'p_t_exp_2','parser_1.py',317),
  ('t_exp_2 -> empty','t_exp_2',1,'p_t_exp_2','parser_1.py',318),
  ('g_exp -> m_exp g_exp_2','g_exp',2,'p_g_exp','parser_1.py',323),
  ('g_exp_2 -> LESS_EQUAL g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',328),
  ('g_exp_2 -> LESS g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',329),
  ('g_exp_2 -> GREATER_EQUAL g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',330),
  ('g_exp_2 -> GREATER g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',331),
  ('g_exp_2 -> COMPARE g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',332),
  ('g_exp_2 -> NOT_EQUAL g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',333),
  ('g_exp_2 -> empty','g_exp_2',1,'p_g_exp_2','parser_1.py',334),
  ('g_exp_3 -> m_exp','g_exp_3',1,'p_g_exp_3','parser_1.py',339),
  ('m_exp -> t m_exp_2','m_exp',2,'p_m_exp','parser_1.py',344),
  ('m_exp_2 -> PLUS m_exp','m_exp_2',2,'p_m_exp_2','parser_1.py',349),
  ('m_exp_2 -> MINUS m_exp','m_exp_2',2,'p_m_exp_2','parser_1.py',350),
  ('m_exp_2 -> empty','m_exp_2',1,'p_m_exp_2','parser_1.py',351),
  ('t -> f t_2','t',2,'p_t','parser_1.py',356),
  ('t_2 -> TIMES t','t_2',2,'p_t_2','parser_1.py',361),
  ('t_2 -> DIVIDE t','t_2',2,'p_t_2','parser_1.py',362),
  ('t_2 -> empty','t_2',1,'p_t_2','parser_1.py',363),
  ('f -> LPAR m_exp RPAR','f',3,'p_f','parser_1.py',368),
  ('f -> variable','f',1,'p_f','parser_1.py',369),
  ('f -> llamada','f',1,'p_f','parser_1.py',370),
  ('f -> f_2','f',1,'p_f','parser_1.py',371),
  ('f_2 -> CTE_I','f_2',1,'p_f_2','parser_1.py',376),
  ('f_2 -> CTE_F','f_2',1,'p_f_2','parser_1.py',377),
  ('function -> FUNC function_2 SEMICOLON','function',3,'p_function','parser_1.py',382),
  ('function_2 -> tipo_simple ID LPAR param RPAR L_C_BRACKET body RETURN LPAR exp RPAR SEMICOLON R_C_BRACKET','function_2',13,'p_function_2','parser_1.py',387),
  ('function_2 -> VOID ID LPAR param RPAR L_C_BRACKET body R_C_BRACKET','function_2',8,'p_function_2','parser_1.py',388),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',393),
]
