
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COLON COMMA COMPARE CTE_F CTE_I CTE_S DATAFRAME DIVIDE ELSE EQUAL FLOAT FOR FUNC GREATER GREATER_EQUAL ID IF INT LESS LESS_EQUAL LPAR L_C_BRACKET L_S_BRACKET MAIN MINUS NOT_EQUAL OR PLUS PROGRAM READ RETURN RPAR R_C_BRACKET R_S_BRACKET SEMICOLON STRING TIMES TO VAR VOID WHILE WRITE\n    program : PROGRAM ID COLON modules main\n    \n    modules : modules_2 modules_3\n    \n    modules_2 : vars\n                | empty\n    \n    modules_3 : function\n                    | empty\n    \n    main : MAIN LPAR RPAR L_C_BRACKET body R_C_BRACKET SEMICOLON\n    \n    body : vars estatuto body_2\n    \n    body_2 : estatuto body_2\n                | empty\n    \n    tipo_simple : INT \n                | FLOAT\n                | CHAR\n    \n    tipo_comp : DATAFRAME\n    \n    vars : VAR vars_2 SEMICOLON vars_8\n    \n    vars_2 : tipo_comp vars_3\n                        | tipo_simple vars_4\n    \n    vars_3 : ID vars_5\n    \n    vars_4 : vars_3 \n                | ID vars_6\n    \n    vars_5 : COMMA vars_3\n            | empty\n    \n    vars_6 : L_S_BRACKET CTE_I R_S_BRACKET vars_7\n                | empty\n    \n    vars_7 : L_S_BRACKET CTE_I R_S_BRACKET\n                | empty\n    \n    vars_8 : vars \n                | empty\n    \n    param : tipo_simple param_2 ID\n                | empty\n    \n    param_2 : COMMA tipo_simple\n                | empty\n    \n    variable : ID variable_2\n    \n    variable_2 : L_S_BRACKET exp R_S_BRACKET variable_3 \n                    | empty\n    \n    variable_3 : L_S_BRACKET exp R_S_BRACKET\n                    | empty\n    \n    estatuto : asigna\n                | llamada\n                | read\n                | write\n                | if_1\n                | for_l\n                | while_l\n                | func_extra\n    \n    asigna : variable EQUAL exp SEMICOLON\n    \n    llamada : ID LPAR exp llamada_2 RPAR SEMICOLON\n    \n    llamada_2 : COMMA exp llamada_2 \n                | empty\n    \n    read : READ LPAR variable RPAR SEMICOLON\n    \n    write : WRITE LPAR write_2 write_3 RPAR SEMICOLON\n    \n    write_2 : exp\n                | CTE_S\n    \n    write_3 : COMMA write_2 write_3 \n                | empty\n    \n    if_1 : IF LPAR exp RPAR L_C_BRACKET estatuto if_2 R_C_BRACKET if_3 SEMICOLON\n    \n    if_2 : estatuto if_2 \n            | empty\n    \n    if_3 : ELSE L_C_BRACKET estatuto if_2 R_C_BRACKET\n    \n    for_l : FOR LPAR ID RPAR EQUAL exp TO exp RPAR L_C_BRACKET estatuto for_l_2 R_C_BRACKET SEMICOLON\n    \n    for_l_2 : estatuto for_l_2\n                | empty\n    \n    while_l : WHILE LPAR exp RPAR L_C_BRACKET estatuto while_l_2 R_C_BRACKET SEMICOLON\n    \n    while_l_2 : estatuto while_l_2\n                    | empty\n    \n    func_extra : empty\n    \n    exp : t_exp exp_2\n    \n    exp_2 : OR exp\n            | empty\n    \n    t_exp : g_exp t_exp_2\n    \n    t_exp_2 : AND t_exp\n                | empty\n    \n    g_exp : m_exp g_exp_2\n    \n    g_exp_2 : LESS_EQUAL g_exp_3\n                | LESS g_exp_3\n                | GREATER_EQUAL g_exp_3\n                | GREATER g_exp_3\n                | COMPARE g_exp_3\n                | NOT_EQUAL g_exp_3\n                | empty\n    \n    g_exp_3 : m_exp\n    \n    m_exp : t m_exp_2\n    \n    m_exp_2 : PLUS m_exp\n                | MINUS m_exp\n                | empty\n    \n    t : f t_2\n    \n    t_2 : TIMES t\n            | DIVIDE t\n            | empty\n    \n    f : LPAR m_exp RPAR\n            | variable\n            | llamada\n            | f_2\n    \n    f_2 : CTE_I\n            | CTE_F\n    \n    function : FUNC function_2 SEMICOLON\n    \n    function_2 : tipo_simple ID LPAR param RPAR L_C_BRACKET body RETURN LPAR exp RPAR SEMICOLON R_C_BRACKET\n                    | VOID ID LPAR param RPAR L_C_BRACKET body R_C_BRACKET\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,10,84,],[0,-1,-7,]),'ID':([2,17,18,19,20,21,22,25,26,27,37,38,39,41,52,53,59,60,61,62,63,64,65,66,67,75,76,78,85,87,88,89,91,93,94,95,96,97,99,111,130,132,135,138,139,140,141,142,143,146,147,150,151,155,160,183,186,189,190,191,192,193,196,198,200,203,205,206,207,209,220,222,223,224,225,226,228,230,234,],[3,29,32,-14,-11,-12,-13,35,36,-99,-15,-27,-28,29,69,-99,69,-38,-39,-40,-41,-42,-43,-44,-45,-66,98,-32,69,-66,114,114,114,120,114,114,125,114,-31,114,-46,114,114,114,114,114,114,114,114,114,114,114,114,114,114,114,-50,69,114,69,114,-47,-51,69,69,69,-66,114,69,-66,-63,-56,69,69,69,69,69,-66,-60,]),'COLON':([3,],[4,]),'VAR':([4,27,46,100,101,],[9,9,9,9,9,]),'FUNC':([4,6,7,8,27,37,38,39,],[-99,15,-3,-4,-99,-15,-27,-28,]),'MAIN':([4,5,6,7,8,12,13,14,27,34,37,38,39,],[-99,11,-99,-3,-4,-2,-5,-6,-99,-96,-15,-27,-28,]),'DATAFRAME':([9,],[19,]),'INT':([9,15,47,48,77,],[20,20,20,20,20,]),'FLOAT':([9,15,47,48,77,],[21,21,21,21,21,]),'CHAR':([9,15,47,48,77,],[22,22,22,22,22,]),'LPAR':([11,35,36,69,70,71,72,73,74,88,89,91,94,95,97,111,114,132,135,138,139,140,141,142,143,146,147,150,151,155,160,165,183,190,192,206,],[23,47,48,89,93,94,95,96,97,111,111,111,111,111,111,111,89,111,111,111,111,111,111,111,111,111,111,111,111,111,111,192,111,111,111,111,]),'VOID':([15,],[26,]),'SEMICOLON':([16,24,28,29,30,31,32,40,42,43,45,49,57,58,82,83,90,92,104,105,106,107,108,109,110,112,113,114,115,116,129,131,133,134,136,137,144,145,148,149,152,157,158,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,184,185,187,193,202,210,215,217,221,231,233,],[27,34,-16,-99,-17,-19,-99,-18,-22,-20,-22,-21,-99,84,-23,-26,-33,-35,-91,130,-99,-99,-99,-99,-99,-92,-93,-99,-94,-95,-25,-67,-69,-70,-72,-73,-80,-82,-85,-86,-89,-99,186,-98,-68,-71,-74,-81,-75,-76,-77,-78,-79,-83,-84,-87,-88,-90,193,-34,-37,196,-47,-36,216,220,222,-97,-59,234,]),'COMMA':([20,21,22,29,32,53,90,92,104,106,107,108,109,110,112,113,114,115,116,117,121,122,123,131,133,134,136,137,144,145,148,149,152,157,167,168,169,170,171,172,173,174,175,176,177,178,179,180,182,184,185,188,193,202,],[-11,-12,-13,41,41,77,-33,-35,-91,-99,-99,-99,-99,-99,-92,-93,-99,-94,-95,155,160,-52,-53,-67,-69,-70,-72,-73,-80,-82,-85,-86,-89,-99,-68,-71,-74,-81,-75,-76,-77,-78,-79,-83,-84,-87,-88,-90,155,-34,-37,160,-47,-36,]),'RPAR':([23,47,48,54,55,56,90,92,98,104,106,107,108,109,110,112,113,114,115,116,117,119,120,121,122,123,124,125,126,131,133,134,136,137,144,145,148,149,152,153,154,156,157,159,161,167,168,169,170,171,172,173,174,175,176,177,178,179,180,182,184,185,188,193,194,197,201,202,213,],[33,-99,-99,79,-30,80,-33,-35,-29,-91,-99,-99,-99,-99,-99,-92,-93,-99,-94,-95,-99,158,-99,-99,-52,-53,162,163,164,-67,-69,-70,-72,-73,-80,-82,-85,-86,-89,180,181,-49,-99,187,-55,-68,-71,-74,-81,-75,-76,-77,-78,-79,-83,-84,-87,-88,-90,-99,-34,-37,-99,-47,-48,-54,210,-36,219,]),'READ':([27,37,38,39,52,59,60,61,62,63,64,65,66,67,75,85,87,130,186,189,191,193,196,198,200,203,205,207,209,220,222,223,224,225,226,228,230,234,],[-99,-15,-27,-28,70,70,-38,-39,-40,-41,-42,-43,-44,-45,-66,70,-66,-46,-50,70,70,-47,-51,70,70,70,-66,70,-66,-63,-56,70,70,70,70,70,-66,-60,]),'WRITE':([27,37,38,39,52,59,60,61,62,63,64,65,66,67,75,85,87,130,186,189,191,193,196,198,200,203,205,207,209,220,222,223,224,225,226,228,230,234,],[-99,-15,-27,-28,71,71,-38,-39,-40,-41,-42,-43,-44,-45,-66,71,-66,-46,-50,71,71,-47,-51,71,71,71,-66,71,-66,-63,-56,71,71,71,71,71,-66,-60,]),'IF':([27,37,38,39,52,59,60,61,62,63,64,65,66,67,75,85,87,130,186,189,191,193,196,198,200,203,205,207,209,220,222,223,224,225,226,228,230,234,],[-99,-15,-27,-28,72,72,-38,-39,-40,-41,-42,-43,-44,-45,-66,72,-66,-46,-50,72,72,-47,-51,72,72,72,-66,72,-66,-63,-56,72,72,72,72,72,-66,-60,]),'FOR':([27,37,38,39,52,59,60,61,62,63,64,65,66,67,75,85,87,130,186,189,191,193,196,198,200,203,205,207,209,220,222,223,224,225,226,228,230,234,],[-99,-15,-27,-28,73,73,-38,-39,-40,-41,-42,-43,-44,-45,-66,73,-66,-46,-50,73,73,-47,-51,73,73,73,-66,73,-66,-63,-56,73,73,73,73,73,-66,-60,]),'WHILE':([27,37,38,39,52,59,60,61,62,63,64,65,66,67,75,85,87,130,186,189,191,193,196,198,200,203,205,207,209,220,222,223,224,225,226,228,230,234,],[-99,-15,-27,-28,74,74,-38,-39,-40,-41,-42,-43,-44,-45,-66,74,-66,-46,-50,74,74,-47,-51,74,74,74,-66,74,-66,-63,-56,74,74,74,74,74,-66,-60,]),'R_C_BRACKET':([27,37,38,39,51,52,59,60,61,62,63,64,65,66,67,75,85,86,87,103,128,130,186,189,191,193,196,198,200,203,204,205,207,208,209,211,214,216,220,222,223,224,225,226,227,228,229,230,232,234,],[-99,-15,-27,-28,58,-99,-99,-38,-39,-40,-41,-42,-43,-44,-45,-66,-99,-8,-10,-9,166,-46,-50,-99,-99,-47,-51,-99,-99,-99,212,-58,-99,215,-65,-57,-64,221,-63,-56,-99,-99,-99,-99,231,-99,233,-62,-61,-60,]),'RETURN':([27,37,38,39,52,59,60,61,62,63,64,65,66,67,75,85,86,87,103,127,130,186,193,196,220,222,234,],[-99,-15,-27,-28,-99,-99,-38,-39,-40,-41,-42,-43,-44,-45,-66,-99,-8,-10,-9,165,-46,-50,-47,-51,-63,-56,-60,]),'L_S_BRACKET':([32,57,69,114,120,157,],[44,81,91,91,91,183,]),'L_C_BRACKET':([33,79,80,162,164,218,219,],[46,100,101,189,191,223,224,]),'CTE_I':([44,81,88,89,91,94,95,97,111,132,135,138,139,140,141,142,143,146,147,150,151,155,160,183,190,192,206,],[50,102,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,115,]),'R_S_BRACKET':([50,90,92,102,104,106,107,108,109,110,112,113,114,115,116,118,131,133,134,136,137,144,145,148,149,152,157,167,168,169,170,171,172,173,174,175,176,177,178,179,180,184,185,193,195,202,],[57,-33,-35,129,-91,-99,-99,-99,-99,-99,-92,-93,-99,-94,-95,157,-67,-69,-70,-72,-73,-80,-82,-85,-86,-89,-99,-68,-71,-74,-81,-75,-76,-77,-78,-79,-83,-84,-87,-88,-90,-34,-37,-47,202,-36,]),'EQUAL':([68,69,90,92,157,163,184,185,202,],[88,-99,-33,-35,-99,190,-34,-37,-36,]),'CTE_F':([88,89,91,94,95,97,111,132,135,138,139,140,141,142,143,146,147,150,151,155,160,183,190,192,206,],[116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,116,]),'TIMES':([90,92,104,110,112,113,114,115,116,157,180,184,185,193,202,],[-33,-35,-91,150,-92,-93,-99,-94,-95,-99,-90,-34,-37,-47,-36,]),'DIVIDE':([90,92,104,110,112,113,114,115,116,157,180,184,185,193,202,],[-33,-35,-91,151,-92,-93,-99,-94,-95,-99,-90,-34,-37,-47,-36,]),'PLUS':([90,92,104,109,110,112,113,114,115,116,149,152,157,178,179,180,184,185,193,202,],[-33,-35,-91,146,-99,-92,-93,-99,-94,-95,-86,-89,-99,-87,-88,-90,-34,-37,-47,-36,]),'MINUS':([90,92,104,109,110,112,113,114,115,116,149,152,157,178,179,180,184,185,193,202,],[-33,-35,-91,147,-99,-92,-93,-99,-94,-95,-86,-89,-99,-87,-88,-90,-34,-37,-47,-36,]),'LESS_EQUAL':([90,92,104,108,109,110,112,113,114,115,116,145,148,149,152,157,176,177,178,179,180,184,185,193,202,],[-33,-35,-91,138,-99,-99,-92,-93,-99,-94,-95,-82,-85,-86,-89,-99,-83,-84,-87,-88,-90,-34,-37,-47,-36,]),'LESS':([90,92,104,108,109,110,112,113,114,115,116,145,148,149,152,157,176,177,178,179,180,184,185,193,202,],[-33,-35,-91,139,-99,-99,-92,-93,-99,-94,-95,-82,-85,-86,-89,-99,-83,-84,-87,-88,-90,-34,-37,-47,-36,]),'GREATER_EQUAL':([90,92,104,108,109,110,112,113,114,115,116,145,148,149,152,157,176,177,178,179,180,184,185,193,202,],[-33,-35,-91,140,-99,-99,-92,-93,-99,-94,-95,-82,-85,-86,-89,-99,-83,-84,-87,-88,-90,-34,-37,-47,-36,]),'GREATER':([90,92,104,108,109,110,112,113,114,115,116,145,148,149,152,157,176,177,178,179,180,184,185,193,202,],[-33,-35,-91,141,-99,-99,-92,-93,-99,-94,-95,-82,-85,-86,-89,-99,-83,-84,-87,-88,-90,-34,-37,-47,-36,]),'COMPARE':([90,92,104,108,109,110,112,113,114,115,116,145,148,149,152,157,176,177,178,179,180,184,185,193,202,],[-33,-35,-91,142,-99,-99,-92,-93,-99,-94,-95,-82,-85,-86,-89,-99,-83,-84,-87,-88,-90,-34,-37,-47,-36,]),'NOT_EQUAL':([90,92,104,108,109,110,112,113,114,115,116,145,148,149,152,157,176,177,178,179,180,184,185,193,202,],[-33,-35,-91,143,-99,-99,-92,-93,-99,-94,-95,-82,-85,-86,-89,-99,-83,-84,-87,-88,-90,-34,-37,-47,-36,]),'AND':([90,92,104,107,108,109,110,112,113,114,115,116,137,144,145,148,149,152,157,169,170,171,172,173,174,175,176,177,178,179,180,184,185,193,202,],[-33,-35,-91,135,-99,-99,-99,-92,-93,-99,-94,-95,-73,-80,-82,-85,-86,-89,-99,-74,-81,-75,-76,-77,-78,-79,-83,-84,-87,-88,-90,-34,-37,-47,-36,]),'OR':([90,92,104,106,107,108,109,110,112,113,114,115,116,134,136,137,144,145,148,149,152,157,168,169,170,171,172,173,174,175,176,177,178,179,180,184,185,193,202,],[-33,-35,-91,132,-99,-99,-99,-99,-92,-93,-99,-94,-95,-70,-72,-73,-80,-82,-85,-86,-89,-99,-71,-74,-81,-75,-76,-77,-78,-79,-83,-84,-87,-88,-90,-34,-37,-47,-36,]),'TO':([90,92,104,106,107,108,109,110,112,113,114,115,116,131,133,134,136,137,144,145,148,149,152,157,167,168,169,170,171,172,173,174,175,176,177,178,179,180,184,185,193,199,202,],[-33,-35,-91,-99,-99,-99,-99,-99,-92,-93,-99,-94,-95,-67,-69,-70,-72,-73,-80,-82,-85,-86,-89,-99,-68,-71,-74,-81,-75,-76,-77,-78,-79,-83,-84,-87,-88,-90,-34,-37,-47,206,-36,]),'CTE_S':([94,160,],[123,123,]),'ELSE':([212,],[218,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'modules':([4,],[5,]),'modules_2':([4,],[6,]),'vars':([4,27,46,100,101,],[7,38,52,52,52,]),'empty':([4,6,27,29,32,47,48,52,53,57,59,69,85,106,107,108,109,110,114,117,120,121,157,182,188,189,191,198,200,203,207,223,224,225,226,228,],[8,14,39,42,45,55,55,75,78,83,87,92,87,133,136,144,148,152,92,156,92,161,185,156,161,75,75,205,209,205,209,75,75,205,230,230,]),'main':([5,],[10,]),'modules_3':([6,],[12,]),'function':([6,],[13,]),'vars_2':([9,],[16,]),'tipo_comp':([9,],[17,]),'tipo_simple':([9,15,47,48,77,],[18,25,53,53,99,]),'function_2':([15,],[24,]),'vars_3':([17,18,41,],[28,31,49,]),'vars_4':([18,],[30,]),'vars_8':([27,],[37,]),'vars_5':([29,32,],[40,40,]),'vars_6':([32,],[43,]),'body':([46,100,101,],[51,127,128,]),'param':([47,48,],[54,56,]),'estatuto':([52,59,85,189,191,198,200,203,207,223,224,225,226,228,],[59,85,85,198,200,203,207,203,207,225,226,203,228,228,]),'asigna':([52,59,85,189,191,198,200,203,207,223,224,225,226,228,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'llamada':([52,59,85,88,89,91,94,95,97,111,132,135,138,139,140,141,142,143,146,147,150,151,155,160,183,189,190,191,192,198,200,203,206,207,223,224,225,226,228,],[61,61,61,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,112,61,112,61,112,61,61,61,112,61,61,61,61,61,61,]),'read':([52,59,85,189,191,198,200,203,207,223,224,225,226,228,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'write':([52,59,85,189,191,198,200,203,207,223,224,225,226,228,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'if_1':([52,59,85,189,191,198,200,203,207,223,224,225,226,228,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'for_l':([52,59,85,189,191,198,200,203,207,223,224,225,226,228,],[65,65,65,65,65,65,65,65,65,65,65,65,65,65,]),'while_l':([52,59,85,189,191,198,200,203,207,223,224,225,226,228,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'func_extra':([52,59,85,189,191,198,200,203,207,223,224,225,226,228,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'variable':([52,59,85,88,89,91,93,94,95,97,111,132,135,138,139,140,141,142,143,146,147,150,151,155,160,183,189,190,191,192,198,200,203,206,207,223,224,225,226,228,],[68,68,68,104,104,104,119,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,68,104,68,104,68,68,68,104,68,68,68,68,68,68,]),'param_2':([53,],[76,]),'vars_7':([57,],[82,]),'body_2':([59,85,],[86,103,]),'variable_2':([69,114,120,],[90,90,90,]),'exp':([88,89,91,94,95,97,132,155,160,183,190,192,206,],[105,117,118,122,124,126,167,182,122,195,199,201,213,]),'t_exp':([88,89,91,94,95,97,132,135,155,160,183,190,192,206,],[106,106,106,106,106,106,106,168,106,106,106,106,106,106,]),'g_exp':([88,89,91,94,95,97,132,135,155,160,183,190,192,206,],[107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'m_exp':([88,89,91,94,95,97,111,132,135,138,139,140,141,142,143,146,147,155,160,183,190,192,206,],[108,108,108,108,108,108,153,108,108,170,170,170,170,170,170,176,177,108,108,108,108,108,108,]),'t':([88,89,91,94,95,97,111,132,135,138,139,140,141,142,143,146,147,150,151,155,160,183,190,192,206,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,178,179,109,109,109,109,109,109,]),'f':([88,89,91,94,95,97,111,132,135,138,139,140,141,142,143,146,147,150,151,155,160,183,190,192,206,],[110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,]),'f_2':([88,89,91,94,95,97,111,132,135,138,139,140,141,142,143,146,147,150,151,155,160,183,190,192,206,],[113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,113,]),'write_2':([94,160,],[121,188,]),'exp_2':([106,],[131,]),'t_exp_2':([107,],[134,]),'g_exp_2':([108,],[137,]),'m_exp_2':([109,],[145,]),'t_2':([110,],[149,]),'llamada_2':([117,182,],[154,194,]),'write_3':([121,188,],[159,197,]),'g_exp_3':([138,139,140,141,142,143,],[169,171,172,173,174,175,]),'variable_3':([157,],[184,]),'if_2':([198,203,225,],[204,211,227,]),'while_l_2':([200,207,],[208,214,]),'if_3':([212,],[217,]),'for_l_2':([226,228,],[229,232,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID COLON modules main','program',5,'p_program','parser_1.py',6),
  ('modules -> modules_2 modules_3','modules',2,'p_modules','parser_1.py',12),
  ('modules_2 -> vars','modules_2',1,'p_modules_2','parser_1.py',17),
  ('modules_2 -> empty','modules_2',1,'p_modules_2','parser_1.py',18),
  ('modules_3 -> function','modules_3',1,'p_modules_3','parser_1.py',23),
  ('modules_3 -> empty','modules_3',1,'p_modules_3','parser_1.py',24),
  ('main -> MAIN LPAR RPAR L_C_BRACKET body R_C_BRACKET SEMICOLON','main',7,'p_main','parser_1.py',29),
  ('body -> vars estatuto body_2','body',3,'p_body','parser_1.py',34),
  ('body_2 -> estatuto body_2','body_2',2,'p_body_2','parser_1.py',40),
  ('body_2 -> empty','body_2',1,'p_body_2','parser_1.py',41),
  ('tipo_simple -> INT','tipo_simple',1,'p_tipo_simple','parser_1.py',46),
  ('tipo_simple -> FLOAT','tipo_simple',1,'p_tipo_simple','parser_1.py',47),
  ('tipo_simple -> CHAR','tipo_simple',1,'p_tipo_simple','parser_1.py',48),
  ('tipo_comp -> DATAFRAME','tipo_comp',1,'p_tipo_comp','parser_1.py',53),
  ('vars -> VAR vars_2 SEMICOLON vars_8','vars',4,'p_vars','parser_1.py',58),
  ('vars_2 -> tipo_comp vars_3','vars_2',2,'p_vars_2','parser_1.py',63),
  ('vars_2 -> tipo_simple vars_4','vars_2',2,'p_vars_2','parser_1.py',64),
  ('vars_3 -> ID vars_5','vars_3',2,'p_vars_3','parser_1.py',69),
  ('vars_4 -> vars_3','vars_4',1,'p_vars_4','parser_1.py',74),
  ('vars_4 -> ID vars_6','vars_4',2,'p_vars_4','parser_1.py',75),
  ('vars_5 -> COMMA vars_3','vars_5',2,'p_vars_5','parser_1.py',80),
  ('vars_5 -> empty','vars_5',1,'p_vars_5','parser_1.py',81),
  ('vars_6 -> L_S_BRACKET CTE_I R_S_BRACKET vars_7','vars_6',4,'p_vars_6','parser_1.py',86),
  ('vars_6 -> empty','vars_6',1,'p_vars_6','parser_1.py',87),
  ('vars_7 -> L_S_BRACKET CTE_I R_S_BRACKET','vars_7',3,'p_vars_7','parser_1.py',92),
  ('vars_7 -> empty','vars_7',1,'p_vars_7','parser_1.py',93),
  ('vars_8 -> vars','vars_8',1,'p_vars_8','parser_1.py',98),
  ('vars_8 -> empty','vars_8',1,'p_vars_8','parser_1.py',99),
  ('param -> tipo_simple param_2 ID','param',3,'p_param','parser_1.py',104),
  ('param -> empty','param',1,'p_param','parser_1.py',105),
  ('param_2 -> COMMA tipo_simple','param_2',2,'p_param_2','parser_1.py',110),
  ('param_2 -> empty','param_2',1,'p_param_2','parser_1.py',111),
  ('variable -> ID variable_2','variable',2,'p_variable','parser_1.py',116),
  ('variable_2 -> L_S_BRACKET exp R_S_BRACKET variable_3','variable_2',4,'p_variable_2','parser_1.py',121),
  ('variable_2 -> empty','variable_2',1,'p_variable_2','parser_1.py',122),
  ('variable_3 -> L_S_BRACKET exp R_S_BRACKET','variable_3',3,'p_variable_3','parser_1.py',127),
  ('variable_3 -> empty','variable_3',1,'p_variable_3','parser_1.py',128),
  ('estatuto -> asigna','estatuto',1,'p_estatuto','parser_1.py',133),
  ('estatuto -> llamada','estatuto',1,'p_estatuto','parser_1.py',134),
  ('estatuto -> read','estatuto',1,'p_estatuto','parser_1.py',135),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser_1.py',136),
  ('estatuto -> if_1','estatuto',1,'p_estatuto','parser_1.py',137),
  ('estatuto -> for_l','estatuto',1,'p_estatuto','parser_1.py',138),
  ('estatuto -> while_l','estatuto',1,'p_estatuto','parser_1.py',139),
  ('estatuto -> func_extra','estatuto',1,'p_estatuto','parser_1.py',140),
  ('asigna -> variable EQUAL exp SEMICOLON','asigna',4,'p_asigna','parser_1.py',145),
  ('llamada -> ID LPAR exp llamada_2 RPAR SEMICOLON','llamada',6,'p_llamada','parser_1.py',150),
  ('llamada_2 -> COMMA exp llamada_2','llamada_2',3,'p_llamada_2','parser_1.py',155),
  ('llamada_2 -> empty','llamada_2',1,'p_llamada_2','parser_1.py',156),
  ('read -> READ LPAR variable RPAR SEMICOLON','read',5,'p_read','parser_1.py',161),
  ('write -> WRITE LPAR write_2 write_3 RPAR SEMICOLON','write',6,'p_write','parser_1.py',166),
  ('write_2 -> exp','write_2',1,'p_write_2','parser_1.py',171),
  ('write_2 -> CTE_S','write_2',1,'p_write_2','parser_1.py',172),
  ('write_3 -> COMMA write_2 write_3','write_3',3,'p_write_3','parser_1.py',177),
  ('write_3 -> empty','write_3',1,'p_write_3','parser_1.py',178),
  ('if_1 -> IF LPAR exp RPAR L_C_BRACKET estatuto if_2 R_C_BRACKET if_3 SEMICOLON','if_1',10,'p_if_1','parser_1.py',183),
  ('if_2 -> estatuto if_2','if_2',2,'p_if_2','parser_1.py',188),
  ('if_2 -> empty','if_2',1,'p_if_2','parser_1.py',189),
  ('if_3 -> ELSE L_C_BRACKET estatuto if_2 R_C_BRACKET','if_3',5,'p_if_3','parser_1.py',194),
  ('for_l -> FOR LPAR ID RPAR EQUAL exp TO exp RPAR L_C_BRACKET estatuto for_l_2 R_C_BRACKET SEMICOLON','for_l',14,'p_for_l','parser_1.py',199),
  ('for_l_2 -> estatuto for_l_2','for_l_2',2,'p_for_l_2','parser_1.py',204),
  ('for_l_2 -> empty','for_l_2',1,'p_for_l_2','parser_1.py',205),
  ('while_l -> WHILE LPAR exp RPAR L_C_BRACKET estatuto while_l_2 R_C_BRACKET SEMICOLON','while_l',9,'p_while_l','parser_1.py',210),
  ('while_l_2 -> estatuto while_l_2','while_l_2',2,'p_while_l_2','parser_1.py',215),
  ('while_l_2 -> empty','while_l_2',1,'p_while_l_2','parser_1.py',216),
  ('func_extra -> empty','func_extra',1,'p_func_extra','parser_1.py',221),
  ('exp -> t_exp exp_2','exp',2,'p_exp','parser_1.py',226),
  ('exp_2 -> OR exp','exp_2',2,'p_exp_2','parser_1.py',231),
  ('exp_2 -> empty','exp_2',1,'p_exp_2','parser_1.py',232),
  ('t_exp -> g_exp t_exp_2','t_exp',2,'p_t_exp','parser_1.py',237),
  ('t_exp_2 -> AND t_exp','t_exp_2',2,'p_t_exp_2','parser_1.py',242),
  ('t_exp_2 -> empty','t_exp_2',1,'p_t_exp_2','parser_1.py',243),
  ('g_exp -> m_exp g_exp_2','g_exp',2,'p_g_exp','parser_1.py',248),
  ('g_exp_2 -> LESS_EQUAL g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',253),
  ('g_exp_2 -> LESS g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',254),
  ('g_exp_2 -> GREATER_EQUAL g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',255),
  ('g_exp_2 -> GREATER g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',256),
  ('g_exp_2 -> COMPARE g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',257),
  ('g_exp_2 -> NOT_EQUAL g_exp_3','g_exp_2',2,'p_g_exp_2','parser_1.py',258),
  ('g_exp_2 -> empty','g_exp_2',1,'p_g_exp_2','parser_1.py',259),
  ('g_exp_3 -> m_exp','g_exp_3',1,'p_g_exp_3','parser_1.py',264),
  ('m_exp -> t m_exp_2','m_exp',2,'p_m_exp','parser_1.py',269),
  ('m_exp_2 -> PLUS m_exp','m_exp_2',2,'p_m_exp_2','parser_1.py',274),
  ('m_exp_2 -> MINUS m_exp','m_exp_2',2,'p_m_exp_2','parser_1.py',275),
  ('m_exp_2 -> empty','m_exp_2',1,'p_m_exp_2','parser_1.py',276),
  ('t -> f t_2','t',2,'p_t','parser_1.py',281),
  ('t_2 -> TIMES t','t_2',2,'p_t_2','parser_1.py',286),
  ('t_2 -> DIVIDE t','t_2',2,'p_t_2','parser_1.py',287),
  ('t_2 -> empty','t_2',1,'p_t_2','parser_1.py',288),
  ('f -> LPAR m_exp RPAR','f',3,'p_f','parser_1.py',293),
  ('f -> variable','f',1,'p_f','parser_1.py',294),
  ('f -> llamada','f',1,'p_f','parser_1.py',295),
  ('f -> f_2','f',1,'p_f','parser_1.py',296),
  ('f_2 -> CTE_I','f_2',1,'p_f_2','parser_1.py',301),
  ('f_2 -> CTE_F','f_2',1,'p_f_2','parser_1.py',302),
  ('function -> FUNC function_2 SEMICOLON','function',3,'p_function','parser_1.py',307),
  ('function_2 -> tipo_simple ID LPAR param RPAR L_C_BRACKET body RETURN LPAR exp RPAR SEMICOLON R_C_BRACKET','function_2',13,'p_function_2','parser_1.py',312),
  ('function_2 -> VOID ID LPAR param RPAR L_C_BRACKET body R_C_BRACKET','function_2',8,'p_function_2','parser_1.py',313),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',318),
]
