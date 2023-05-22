
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COLON COMMA COMPARE CTE_F CTE_I CTE_S DATAFRAME DIVIDE ELSE EQUAL FLOAT FOR FUNC GREATER GREATER_EQUAL ID IF INT LESS LESS_EQUAL LPAR L_C_BRACKET L_S_BRACKET MAIN MINUS NOT_EQUAL OR PLUS PROGRAM READ RETURN RPAR R_C_BRACKET R_S_BRACKET SEMICOLON STRING TIMES TO VAR VOID WHILE WRITE\n    program : PROGRAM program_point ID COLON modules main\n    \n    program_point : empty\n    \n    modules : modules_2 modules_point modules_3\n    \n    modules_point : empty\n    \n    modules_2 : vars\n                | empty\n    \n    modules_3 : function\n                    | empty\n    \n    main : MAIN main_point LPAR RPAR L_C_BRACKET body R_C_BRACKET SEMICOLON\n    \n    main_point : empty\n    \n    body : vars func_agrega_v estatuto body_2\n    \n    body_2 : estatuto body_2\n                | empty\n    \n    tipo_simple : INT \n                | FLOAT\n                | CHAR\n    \n    tipo_comp : DATAFRAME\n    \n    vars : VAR vars_2 SEMICOLON vars_8\n    \n    vars_2 : tipo_comp vars_3\n                        | tipo_simple vars_4\n    \n    vars_3 : ID vars_5\n    \n    vars_4 : vars_3 \n                | ID vars_6\n    \n    vars_5 : COMMA vars_3\n            | empty\n    \n    vars_6 : punto_id_especial L_S_BRACKET CTE_I R_S_BRACKET vars_7\n                | empty\n    \n    punto_id_especial : empty\n    \n    vars_7 : L_S_BRACKET CTE_I R_S_BRACKET var_mat\n                | var_array\n    \n    var_array : empty\n    \n    var_mat : empty\n    \n    vars_8 : vars \n                | empty\n    \n    param : tipo_simple ID punto_param param_2 \n                | empty\n    \n    param_2 : COMMA param\n                | empty\n    \n    punto_param : empty\n    \n    punto_param_2 : empty\n    \n    variable : ID variable_2 variable_point\n    \n    variable_point : empty\n    \n    variable_2 : L_S_BRACKET exp R_S_BRACKET variable_3 \n                    | empty\n    \n    variable_3 : L_S_BRACKET exp R_S_BRACKET\n                    | empty\n    \n    estatuto : asigna\n                | llamada\n                | read\n                | write\n                | if_1\n                | for_l\n                | while_l\n                | return\n                | func_extra\n    \n    asigna : variable EQUAL add_operator exp asigna_point SEMICOLON\n    \n    asigna_point : empty\n    \n    llamada : ID LPAR exp llamada_2 RPAR SEMICOLON\n    \n    llamada_2 : COMMA exp llamada_2 \n                | empty\n    \n    read : READ LPAR variable read_point RPAR SEMICOLON\n    \n    read_point : empty\n    \n    write : WRITE LPAR write_2 write_3 RPAR SEMICOLON\n    \n    write_2 : exp write_point\n                | CTE_S add_constant_s write_point\n    \n    write_3 : COMMA write_2 write_3 \n                | empty\n    \n    write_point : empty\n    \n    if_1 : IF LPAR exp if_point RPAR L_C_BRACKET estatuto if_2 R_C_BRACKET if_3 SEMICOLON if_point_2\n    \n    if_2 :  estatuto if_2 \n            | empty\n    \n    if_3 : ELSE if_point_3 L_C_BRACKET estatuto if_2 R_C_BRACKET\n            | empty\n    \n    if_point : empty\n    \n    if_point_2 : empty\n    \n    if_point_3 : empty\n    \n    for_l : FOR LPAR ID for_point_1 EQUAL exp for_point_2 TO exp for_point_3 RPAR L_C_BRACKET estatuto for_l_2 R_C_BRACKET SEMICOLON for_point_4\n    \n    for_l_2 : estatuto for_l_2\n                | empty\n    \n    for_point_1 : empty\n    \n    for_point_2 : empty\n    \n    for_point_3 : empty\n    \n    for_point_4 : empty\n    \n    while_l : WHILE while_point LPAR exp RPAR while_point_2 L_C_BRACKET estatuto while_l_2 R_C_BRACKET SEMICOLON while_point_3\n    \n    while_l_2 : estatuto while_l_2\n                    | empty\n    \n    while_point : empty\n    \n    while_point_2 : empty\n    \n    while_point_3 : empty\n    \n    return : RETURN check_valid_func LPAR exp RPAR SEMICOLON\n    \n    check_valid_func : empty\n    \n    func_extra : empty\n    \n    exp : t_exp add_operator_4 exp_2 \n    \n    exp_2 : OR add_operator exp \n            | empty\n    \n    t_exp : g_exp add_operator_4 t_exp_2 \n    \n    t_exp_2 : AND add_operator t_exp \n                | empty\n    \n    g_exp : m_exp g_exp_2 add_operator_3\n    \n    g_exp_2 : LESS_EQUAL add_operator m_exp \n                | LESS add_operator m_exp \n                | GREATER_EQUAL add_operator m_exp \n                | GREATER add_operator m_exp \n                | COMPARE add_operator m_exp \n                | NOT_EQUAL add_operator m_exp \n                | empty\n    \n    m_exp : t add_operator_2 m_exp_2\n    \n    m_exp_2 : PLUS add_operator m_exp \n                | MINUS add_operator m_exp\n                | empty\n    \n    t : f add_operator_1 t_2\n    \n    t_2 : TIMES add_operator t \n            | DIVIDE add_operator t\n            | empty\n    \n    f : LPAR add_floor exp RPAR remove_floor\n            | variable\n            | llamada\n            | f_2\n    \n    f_2 : CTE_I add_constant_i\n            | CTE_F add_constant_f\n    \n    add_floor : empty\n    \n    remove_floor : empty\n    \n    add_operator : empty \n    \n    add_operator_1 : empty \n    \n    add_operator_2 : empty \n    \n    add_operator_3 : empty \n    \n    add_operator_4 : empty \n    \n    add_constant_i : empty\n    \n    add_constant_s : empty\n    \n    add_constant_f : empty\n    \n    function : FUNC function_2 SEMICOLON function_4\n    \n    function_2 : function_3 ID function_punto1 LPAR param punto_param_2 RPAR L_C_BRACKET body R_C_BRACKET final_func_point\n    \n    function_3 : tipo_simple\n                    | VOID\n    \n    function_4 : function\n                    | empty\n    \n    function_punto1 : empty\n    \n    function_punto2 : empty\n    \n    func_agrega_v : empty\n    \n    final_func_point : empty\n    \n    empty : \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,12,75,],[0,-1,-9,]),'ID':([2,3,4,17,18,19,20,21,22,29,37,38,39,40,41,42,44,62,66,67,69,76,77,78,79,80,81,82,83,84,85,94,99,101,102,103,105,107,108,109,110,120,121,123,145,146,154,155,157,163,164,165,166,167,168,182,202,205,209,210,211,212,213,214,216,217,220,221,223,231,235,237,239,240,247,248,249,250,252,253,255,259,271,274,275,277,278,279,283,285,293,297,298,299,300,301,302,303,304,305,307,309,313,314,315,],[-141,5,-2,31,34,-17,-14,-15,-16,-141,51,-133,-134,-18,-33,-34,31,-141,87,-139,97,87,-47,-48,-49,-50,-51,-52,-53,-54,-55,-92,87,-92,-141,122,122,139,122,122,144,122,-123,-141,122,122,122,-121,122,-141,-141,-141,-141,-141,-141,122,-141,-141,122,122,122,122,122,122,-141,-141,-141,-141,122,122,-56,-58,122,122,122,122,122,122,-61,-63,87,-90,87,87,87,-92,122,87,87,-92,-141,-141,-69,-75,87,87,-84,-89,87,87,87,-92,-141,-77,-83,]),'COLON':([5,],[6,]),'VAR':([6,29,54,147,],[11,11,11,11,]),'FUNC':([6,8,9,10,14,15,29,40,41,42,50,],[-141,-141,-5,-6,28,-4,-141,-18,-33,-34,28,]),'MAIN':([6,7,8,9,10,14,15,25,26,27,29,40,41,42,50,55,56,57,],[-141,13,-141,-5,-6,-141,-4,-3,-7,-8,-141,-18,-33,-34,-141,-131,-135,-136,]),'DATAFRAME':([11,],[19,]),'INT':([11,28,63,149,],[20,20,20,20,]),'FLOAT':([11,28,63,149,],[21,21,21,21,]),'CHAR':([11,28,63,149,],[22,22,22,22,]),'LPAR':([13,23,24,51,58,59,87,88,89,90,91,92,93,102,103,105,108,109,111,112,113,114,120,121,122,123,145,146,154,155,157,163,164,165,166,167,168,182,202,205,209,210,211,212,213,214,216,217,220,221,223,231,239,240,247,248,249,250,278,],[-141,35,-10,-141,63,-137,103,107,108,109,110,-141,-141,-141,123,123,123,123,145,-87,146,-91,123,-123,103,-141,123,123,123,-121,123,-141,-141,-141,-141,-141,-141,123,-141,-141,123,123,123,123,123,123,-141,-141,-141,-141,123,123,123,123,123,123,123,123,123,]),'SEMICOLON':([16,30,31,32,33,34,36,43,45,46,48,52,64,65,72,73,74,104,106,118,122,125,126,127,128,129,130,131,132,133,134,135,136,151,152,153,159,160,161,162,169,170,171,172,173,174,175,176,177,178,196,197,199,201,203,204,206,207,208,215,218,219,222,224,225,226,227,233,234,236,237,241,242,243,244,245,246,260,261,262,263,264,265,266,267,268,269,270,281,286,288,292,310,312,],[29,-19,-141,-20,-22,-141,50,-21,-25,-23,-25,-24,-141,75,-26,-30,-31,-141,-44,-141,-141,-141,-141,-141,-141,-141,-116,-117,-118,-141,-141,-41,-42,-29,-32,-141,-141,-127,-141,-141,-106,-141,-125,-141,-124,-119,-128,-120,-130,-141,235,-57,237,-93,-95,-96,-98,-99,-126,-107,-110,-111,-114,-43,-46,252,253,259,-141,-141,-58,-100,-101,-102,-103,-104,-105,-132,-140,-115,-122,-94,-97,-108,-109,-112,-113,-45,-141,293,-73,297,-72,313,]),'VOID':([28,],[39,]),'READ':([29,40,41,42,62,66,67,76,77,78,79,80,81,82,83,84,85,94,99,101,235,237,252,253,255,259,271,274,275,277,279,283,285,293,297,298,299,300,301,302,303,304,305,307,309,313,314,315,],[-141,-18,-33,-34,-141,88,-139,88,-47,-48,-49,-50,-51,-52,-53,-54,-55,-92,88,-92,-56,-58,-61,-63,88,-90,88,88,88,-92,88,88,-92,-141,-141,-69,-75,88,88,-84,-89,88,88,88,-92,-141,-77,-83,]),'WRITE':([29,40,41,42,62,66,67,76,77,78,79,80,81,82,83,84,85,94,99,101,235,237,252,253,255,259,271,274,275,277,279,283,285,293,297,298,299,300,301,302,303,304,305,307,309,313,314,315,],[-141,-18,-33,-34,-141,89,-139,89,-47,-48,-49,-50,-51,-52,-53,-54,-55,-92,89,-92,-56,-58,-61,-63,89,-90,89,89,89,-92,89,89,-92,-141,-141,-69,-75,89,89,-84,-89,89,89,89,-92,-141,-77,-83,]),'IF':([29,40,41,42,62,66,67,76,77,78,79,80,81,82,83,84,85,94,99,101,235,237,252,253,255,259,271,274,275,277,279,283,285,293,297,298,299,300,301,302,303,304,305,307,309,313,314,315,],[-141,-18,-33,-34,-141,90,-139,90,-47,-48,-49,-50,-51,-52,-53,-54,-55,-92,90,-92,-56,-58,-61,-63,90,-90,90,90,90,-92,90,90,-92,-141,-141,-69,-75,90,90,-84,-89,90,90,90,-92,-141,-77,-83,]),'FOR':([29,40,41,42,62,66,67,76,77,78,79,80,81,82,83,84,85,94,99,101,235,237,252,253,255,259,271,274,275,277,279,283,285,293,297,298,299,300,301,302,303,304,305,307,309,313,314,315,],[-141,-18,-33,-34,-141,91,-139,91,-47,-48,-49,-50,-51,-52,-53,-54,-55,-92,91,-92,-56,-58,-61,-63,91,-90,91,91,91,-92,91,91,-92,-141,-141,-69,-75,91,91,-84,-89,91,91,91,-92,-141,-77,-83,]),'WHILE':([29,40,41,42,62,66,67,76,77,78,79,80,81,82,83,84,85,94,99,101,235,237,252,253,255,259,271,274,275,277,279,283,285,293,297,298,299,300,301,302,303,304,305,307,309,313,314,315,],[-141,-18,-33,-34,-141,92,-139,92,-47,-48,-49,-50,-51,-52,-53,-54,-55,-92,92,-92,-56,-58,-61,-63,92,-90,92,92,92,-92,92,92,-92,-141,-141,-69,-75,92,92,-84,-89,92,92,92,-92,-141,-77,-83,]),'RETURN':([29,40,41,42,62,66,67,76,77,78,79,80,81,82,83,84,85,94,99,101,235,237,252,253,255,259,271,274,275,277,279,283,285,293,297,298,299,300,301,302,303,304,305,307,309,313,314,315,],[-141,-18,-33,-34,-141,93,-139,93,-47,-48,-49,-50,-51,-52,-53,-54,-55,-92,93,-92,-56,-58,-61,-63,93,-90,93,93,93,-92,93,93,-92,-141,-141,-69,-75,93,93,-84,-89,93,93,93,-92,-141,-77,-83,]),'R_C_BRACKET':([29,40,41,42,61,62,66,67,76,77,78,79,80,81,82,83,84,85,94,99,100,101,119,194,235,237,252,253,255,259,271,274,275,276,277,279,280,283,284,285,291,293,297,298,299,300,301,302,303,304,305,306,307,308,309,311,313,314,315,],[-141,-18,-33,-34,65,-141,-141,-139,-141,-47,-48,-49,-50,-51,-52,-53,-54,-55,-92,-141,-11,-13,-12,234,-56,-58,-61,-63,-141,-90,-141,-141,-141,281,-71,-141,-70,-141,292,-86,-85,-141,-141,-69,-75,-141,-141,-84,-89,-141,-141,310,-141,312,-79,-78,-141,-77,-83,]),'COMMA':([31,34,97,104,106,116,117,122,124,125,126,127,128,129,130,131,132,133,134,135,136,140,141,142,159,160,161,162,169,170,171,172,173,174,175,176,177,178,184,185,186,187,200,201,203,204,206,207,208,215,218,219,222,224,225,228,229,236,237,241,242,243,244,245,246,262,263,264,265,266,267,268,269,270,],[44,44,-141,-141,-44,149,-39,-141,157,-141,-141,-141,-141,-141,-116,-117,-118,-141,-141,-41,-42,182,-141,-141,-141,-127,-141,-141,-106,-141,-125,-141,-124,-119,-128,-120,-130,-141,-64,-68,-141,-129,157,-93,-95,-96,-98,-99,-126,-107,-110,-111,-114,-43,-46,182,-65,-141,-58,-100,-101,-102,-103,-104,-105,-115,-122,-94,-97,-108,-109,-112,-113,-45,]),'L_S_BRACKET':([34,47,48,64,87,122,139,178,],[-141,53,-28,71,105,105,105,223,]),'RPAR':([35,63,68,70,95,96,97,104,106,116,117,122,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,142,143,148,149,150,156,158,159,160,161,162,169,170,171,172,173,174,175,176,177,178,179,180,181,183,184,185,186,187,188,189,192,193,195,198,200,201,203,204,206,207,208,215,218,219,222,224,225,228,229,236,237,238,241,242,243,244,245,246,254,262,263,264,265,266,267,268,269,270,282,289,290,],[49,-141,-141,-36,115,-40,-141,-141,-44,-141,-39,-141,-141,-141,-141,-141,-141,-141,-116,-117,-118,-141,-141,-41,-42,-141,-141,-141,-141,-141,-141,-35,-141,-38,199,-60,-141,-127,-141,-141,-106,-141,-125,-141,-124,-119,-128,-120,-130,-141,226,-62,227,-67,-64,-68,-141,-129,230,-74,232,233,-37,236,-141,-93,-95,-96,-98,-99,-126,-107,-110,-111,-114,-43,-46,-141,-65,-141,-58,-59,-100,-101,-102,-103,-104,-105,-66,-115,-122,-94,-97,-108,-109,-112,-113,-45,-141,296,-82,]),'L_C_BRACKET':([49,115,230,232,257,258,287,294,295,296,],[54,147,255,-141,274,-88,-141,300,-76,301,]),'CTE_I':([53,71,102,103,105,108,109,120,121,123,145,146,154,155,157,163,164,165,166,167,168,182,202,205,209,210,211,212,213,214,216,217,220,221,223,231,239,240,247,248,249,250,278,],[60,98,-141,133,133,133,133,133,-123,-141,133,133,133,-121,133,-141,-141,-141,-141,-141,-141,133,-141,-141,133,133,133,133,133,133,-141,-141,-141,-141,133,133,133,133,133,133,133,133,133,]),'R_S_BRACKET':([60,98,104,106,122,125,126,127,128,129,130,131,132,133,134,135,136,137,159,160,161,162,169,170,171,172,173,174,175,176,177,178,201,203,204,206,207,208,215,218,219,222,224,225,236,237,241,242,243,244,245,246,251,262,263,264,265,266,267,268,269,270,],[64,118,-141,-44,-141,-141,-141,-141,-141,-141,-116,-117,-118,-141,-141,-41,-42,178,-141,-127,-141,-141,-106,-141,-125,-141,-124,-119,-128,-120,-130,-141,-93,-95,-96,-98,-99,-126,-107,-110,-111,-114,-43,-46,-141,-58,-100,-101,-102,-103,-104,-105,270,-115,-122,-94,-97,-108,-109,-112,-113,-45,]),'EQUAL':([86,87,104,106,135,136,144,178,190,191,224,225,270,],[102,-141,-141,-44,-41,-42,-141,-141,231,-80,-43,-46,-45,]),'CTE_F':([102,103,105,108,109,120,121,123,145,146,154,155,157,163,164,165,166,167,168,182,202,205,209,210,211,212,213,214,216,217,220,221,223,231,239,240,247,248,249,250,278,],[-141,134,134,134,134,134,-123,-141,134,134,134,-121,134,-141,-141,-141,-141,-141,-141,134,-141,-141,134,134,134,134,134,134,-141,-141,-141,-141,134,134,134,134,134,134,134,134,134,]),'TIMES':([104,106,122,129,130,131,132,133,134,135,136,172,173,174,175,176,177,178,224,225,236,237,262,263,270,],[-141,-44,-141,-141,-116,-117,-118,-141,-141,-41,-42,220,-124,-119,-128,-120,-130,-141,-43,-46,-141,-58,-115,-122,-45,]),'DIVIDE':([104,106,122,129,130,131,132,133,134,135,136,172,173,174,175,176,177,178,224,225,236,237,262,263,270,],[-141,-44,-141,-141,-116,-117,-118,-141,-141,-41,-42,221,-124,-119,-128,-120,-130,-141,-43,-46,-141,-58,-115,-122,-45,]),'PLUS':([104,106,122,128,129,130,131,132,133,134,135,136,170,171,172,173,174,175,176,177,178,219,222,224,225,236,237,262,263,268,269,270,],[-141,-44,-141,-141,-141,-116,-117,-118,-141,-141,-41,-42,216,-125,-141,-124,-119,-128,-120,-130,-141,-111,-114,-43,-46,-141,-58,-115,-122,-112,-113,-45,]),'MINUS':([104,106,122,128,129,130,131,132,133,134,135,136,170,171,172,173,174,175,176,177,178,219,222,224,225,236,237,262,263,268,269,270,],[-141,-44,-141,-141,-141,-116,-117,-118,-141,-141,-41,-42,217,-125,-141,-124,-119,-128,-120,-130,-141,-111,-114,-43,-46,-141,-58,-115,-122,-112,-113,-45,]),'LESS_EQUAL':([104,106,122,127,128,129,130,131,132,133,134,135,136,170,171,172,173,174,175,176,177,178,215,218,219,222,224,225,236,237,262,263,266,267,268,269,270,],[-141,-44,-141,163,-141,-141,-116,-117,-118,-141,-141,-41,-42,-141,-125,-141,-124,-119,-128,-120,-130,-141,-107,-110,-111,-114,-43,-46,-141,-58,-115,-122,-108,-109,-112,-113,-45,]),'LESS':([104,106,122,127,128,129,130,131,132,133,134,135,136,170,171,172,173,174,175,176,177,178,215,218,219,222,224,225,236,237,262,263,266,267,268,269,270,],[-141,-44,-141,164,-141,-141,-116,-117,-118,-141,-141,-41,-42,-141,-125,-141,-124,-119,-128,-120,-130,-141,-107,-110,-111,-114,-43,-46,-141,-58,-115,-122,-108,-109,-112,-113,-45,]),'GREATER_EQUAL':([104,106,122,127,128,129,130,131,132,133,134,135,136,170,171,172,173,174,175,176,177,178,215,218,219,222,224,225,236,237,262,263,266,267,268,269,270,],[-141,-44,-141,165,-141,-141,-116,-117,-118,-141,-141,-41,-42,-141,-125,-141,-124,-119,-128,-120,-130,-141,-107,-110,-111,-114,-43,-46,-141,-58,-115,-122,-108,-109,-112,-113,-45,]),'GREATER':([104,106,122,127,128,129,130,131,132,133,134,135,136,170,171,172,173,174,175,176,177,178,215,218,219,222,224,225,236,237,262,263,266,267,268,269,270,],[-141,-44,-141,166,-141,-141,-116,-117,-118,-141,-141,-41,-42,-141,-125,-141,-124,-119,-128,-120,-130,-141,-107,-110,-111,-114,-43,-46,-141,-58,-115,-122,-108,-109,-112,-113,-45,]),'COMPARE':([104,106,122,127,128,129,130,131,132,133,134,135,136,170,171,172,173,174,175,176,177,178,215,218,219,222,224,225,236,237,262,263,266,267,268,269,270,],[-141,-44,-141,167,-141,-141,-116,-117,-118,-141,-141,-41,-42,-141,-125,-141,-124,-119,-128,-120,-130,-141,-107,-110,-111,-114,-43,-46,-141,-58,-115,-122,-108,-109,-112,-113,-45,]),'NOT_EQUAL':([104,106,122,127,128,129,130,131,132,133,134,135,136,170,171,172,173,174,175,176,177,178,215,218,219,222,224,225,236,237,262,263,266,267,268,269,270,],[-141,-44,-141,168,-141,-141,-116,-117,-118,-141,-141,-41,-42,-141,-125,-141,-124,-119,-128,-120,-130,-141,-107,-110,-111,-114,-43,-46,-141,-58,-115,-122,-108,-109,-112,-113,-45,]),'AND':([104,106,122,126,127,128,129,130,131,132,133,134,135,136,160,161,162,169,170,171,172,173,174,175,176,177,178,207,208,215,218,219,222,224,225,236,237,241,242,243,244,245,246,262,263,266,267,268,269,270,],[-141,-44,-141,-141,-141,-141,-141,-116,-117,-118,-141,-141,-41,-42,-127,205,-141,-106,-141,-125,-141,-124,-119,-128,-120,-130,-141,-99,-126,-107,-110,-111,-114,-43,-46,-141,-58,-100,-101,-102,-103,-104,-105,-115,-122,-108,-109,-112,-113,-45,]),'OR':([104,106,122,125,126,127,128,129,130,131,132,133,134,135,136,159,160,161,162,169,170,171,172,173,174,175,176,177,178,204,206,207,208,215,218,219,222,224,225,236,237,241,242,243,244,245,246,262,263,265,266,267,268,269,270,],[-141,-44,-141,-141,-141,-141,-141,-141,-116,-117,-118,-141,-141,-41,-42,202,-127,-141,-141,-106,-141,-125,-141,-124,-119,-128,-120,-130,-141,-96,-98,-99,-126,-107,-110,-111,-114,-43,-46,-141,-58,-100,-101,-102,-103,-104,-105,-115,-122,-97,-108,-109,-112,-113,-45,]),'TO':([104,106,122,125,126,127,128,129,130,131,132,133,134,135,136,159,160,161,162,169,170,171,172,173,174,175,176,177,178,201,203,204,206,207,208,215,218,219,222,224,225,236,237,241,242,243,244,245,246,256,262,263,264,265,266,267,268,269,270,272,273,],[-141,-44,-141,-141,-141,-141,-141,-141,-116,-117,-118,-141,-141,-41,-42,-141,-127,-141,-141,-106,-141,-125,-141,-124,-119,-128,-120,-130,-141,-93,-95,-96,-98,-99,-126,-107,-110,-111,-114,-43,-46,-141,-58,-100,-101,-102,-103,-104,-105,-141,-115,-122,-94,-97,-108,-109,-112,-113,-45,278,-81,]),'CTE_S':([108,182,],[142,142,]),'ELSE':([281,],[287,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'program_point':([2,],[3,]),'empty':([2,6,8,13,14,29,31,34,50,51,62,63,64,66,68,76,87,92,93,97,99,102,104,116,118,122,123,124,125,126,127,128,129,133,134,138,139,140,141,142,143,144,149,153,159,161,162,163,164,165,166,167,168,170,172,178,186,200,202,205,216,217,220,221,228,232,234,236,255,256,271,274,275,279,281,282,283,287,293,297,300,301,304,305,307,313,],[4,10,15,24,27,42,45,48,57,59,67,70,74,94,96,101,106,112,114,117,101,121,136,150,152,106,155,158,160,160,169,171,173,175,177,180,106,183,185,187,189,191,70,197,203,206,208,121,121,121,121,121,121,218,222,225,185,158,121,121,121,121,121,121,183,258,261,263,94,273,277,94,277,285,288,290,285,295,299,303,94,94,277,309,309,315,]),'modules':([6,],[7,]),'modules_2':([6,],[8,]),'vars':([6,29,54,147,],[9,41,62,62,]),'main':([7,],[12,]),'modules_point':([8,],[14,]),'vars_2':([11,],[16,]),'tipo_comp':([11,],[17,]),'tipo_simple':([11,28,63,149,],[18,38,69,69,]),'main_point':([13,],[23,]),'modules_3':([14,],[25,]),'function':([14,50,],[26,56,]),'vars_3':([17,18,44,],[30,33,52,]),'vars_4':([18,],[32,]),'function_2':([28,],[36,]),'function_3':([28,],[37,]),'vars_8':([29,],[40,]),'vars_5':([31,34,],[43,43,]),'vars_6':([34,],[46,]),'punto_id_especial':([34,],[47,]),'function_4':([50,],[55,]),'function_punto1':([51,],[58,]),'body':([54,147,],[61,194,]),'func_agrega_v':([62,],[66,]),'param':([63,149,],[68,195,]),'vars_7':([64,],[72,]),'var_array':([64,],[73,]),'estatuto':([66,76,99,255,271,274,275,279,283,300,301,304,305,307,],[76,99,99,271,275,279,275,283,283,304,305,275,307,307,]),'asigna':([66,76,99,255,271,274,275,279,283,300,301,304,305,307,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'llamada':([66,76,99,103,105,108,109,120,145,146,154,157,182,209,210,211,212,213,214,223,231,239,240,247,248,249,250,255,271,274,275,278,279,283,300,301,304,305,307,],[78,78,78,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,131,78,78,78,78,131,78,78,78,78,78,78,78,]),'read':([66,76,99,255,271,274,275,279,283,300,301,304,305,307,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'write':([66,76,99,255,271,274,275,279,283,300,301,304,305,307,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'if_1':([66,76,99,255,271,274,275,279,283,300,301,304,305,307,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'for_l':([66,76,99,255,271,274,275,279,283,300,301,304,305,307,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'while_l':([66,76,99,255,271,274,275,279,283,300,301,304,305,307,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'return':([66,76,99,255,271,274,275,279,283,300,301,304,305,307,],[84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'func_extra':([66,76,99,255,271,274,275,279,283,300,301,304,305,307,],[85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'variable':([66,76,99,103,105,107,108,109,120,145,146,154,157,182,209,210,211,212,213,214,223,231,239,240,247,248,249,250,255,271,274,275,278,279,283,300,301,304,305,307,],[86,86,86,130,130,138,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,86,86,86,86,130,86,86,86,86,86,86,86,]),'punto_param_2':([68,],[95,]),'body_2':([76,99,],[100,119,]),'variable_2':([87,122,139,],[104,104,104,]),'while_point':([92,],[111,]),'check_valid_func':([93,],[113,]),'punto_param':([97,],[116,]),'add_operator':([102,163,164,165,166,167,168,202,205,216,217,220,221,],[120,209,210,211,212,213,214,239,240,247,248,249,250,]),'exp':([103,105,108,109,120,145,146,154,157,182,223,231,239,278,],[124,137,141,143,153,192,193,198,200,141,251,256,264,282,]),'t_exp':([103,105,108,109,120,145,146,154,157,182,223,231,239,240,278,],[125,125,125,125,125,125,125,125,125,125,125,125,125,265,125,]),'g_exp':([103,105,108,109,120,145,146,154,157,182,223,231,239,240,278,],[126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,]),'m_exp':([103,105,108,109,120,145,146,154,157,182,209,210,211,212,213,214,223,231,239,240,247,248,278,],[127,127,127,127,127,127,127,127,127,127,241,242,243,244,245,246,127,127,127,127,266,267,127,]),'t':([103,105,108,109,120,145,146,154,157,182,209,210,211,212,213,214,223,231,239,240,247,248,249,250,278,],[128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,268,269,128,]),'f':([103,105,108,109,120,145,146,154,157,182,209,210,211,212,213,214,223,231,239,240,247,248,249,250,278,],[129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,]),'f_2':([103,105,108,109,120,145,146,154,157,182,209,210,211,212,213,214,223,231,239,240,247,248,249,250,278,],[132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,]),'variable_point':([104,],[135,]),'write_2':([108,182,],[140,228,]),'param_2':([116,],[148,]),'var_mat':([118,],[151,]),'add_floor':([123,],[154,]),'llamada_2':([124,200,],[156,238,]),'add_operator_4':([125,126,],[159,161,]),'g_exp_2':([127,],[162,]),'add_operator_2':([128,],[170,]),'add_operator_1':([129,],[172,]),'add_constant_i':([133,],[174,]),'add_constant_f':([134,],[176,]),'read_point':([138,],[179,]),'write_3':([140,228,],[181,254,]),'write_point':([141,186,],[184,229,]),'add_constant_s':([142,],[186,]),'if_point':([143,],[188,]),'for_point_1':([144,],[190,]),'asigna_point':([153,],[196,]),'exp_2':([159,],[201,]),'t_exp_2':([161,],[204,]),'add_operator_3':([162,],[207,]),'m_exp_2':([170,],[215,]),'t_2':([172,],[219,]),'variable_3':([178,],[224,]),'while_point_2':([232,],[257,]),'final_func_point':([234,],[260,]),'remove_floor':([236,],[262,]),'for_point_2':([256,],[272,]),'if_2':([271,275,304,],[276,280,306,]),'while_l_2':([279,283,],[284,291,]),'if_3':([281,],[286,]),'for_point_3':([282,],[289,]),'if_point_3':([287,],[294,]),'if_point_2':([293,],[298,]),'while_point_3':([297,],[302,]),'for_l_2':([305,307,],[308,311,]),'for_point_4':([313,],[314,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM program_point ID COLON modules main','program',6,'p_program','parser_1.py',46),
  ('program_point -> empty','program_point',1,'p_program_point','parser_1.py',51),
  ('modules -> modules_2 modules_point modules_3','modules',3,'p_modules','parser_1.py',58),
  ('modules_point -> empty','modules_point',1,'p_modules_point','parser_1.py',63),
  ('modules_2 -> vars','modules_2',1,'p_modules_2','parser_1.py',80),
  ('modules_2 -> empty','modules_2',1,'p_modules_2','parser_1.py',81),
  ('modules_3 -> function','modules_3',1,'p_modules_3','parser_1.py',86),
  ('modules_3 -> empty','modules_3',1,'p_modules_3','parser_1.py',87),
  ('main -> MAIN main_point LPAR RPAR L_C_BRACKET body R_C_BRACKET SEMICOLON','main',8,'p_main','parser_1.py',92),
  ('main_point -> empty','main_point',1,'p_main_point','parser_1.py',97),
  ('body -> vars func_agrega_v estatuto body_2','body',4,'p_body','parser_1.py',105),
  ('body_2 -> estatuto body_2','body_2',2,'p_body_2','parser_1.py',111),
  ('body_2 -> empty','body_2',1,'p_body_2','parser_1.py',112),
  ('tipo_simple -> INT','tipo_simple',1,'p_tipo_simple','parser_1.py',117),
  ('tipo_simple -> FLOAT','tipo_simple',1,'p_tipo_simple','parser_1.py',118),
  ('tipo_simple -> CHAR','tipo_simple',1,'p_tipo_simple','parser_1.py',119),
  ('tipo_comp -> DATAFRAME','tipo_comp',1,'p_tipo_comp','parser_1.py',126),
  ('vars -> VAR vars_2 SEMICOLON vars_8','vars',4,'p_vars','parser_1.py',133),
  ('vars_2 -> tipo_comp vars_3','vars_2',2,'p_vars_2','parser_1.py',139),
  ('vars_2 -> tipo_simple vars_4','vars_2',2,'p_vars_2','parser_1.py',140),
  ('vars_3 -> ID vars_5','vars_3',2,'p_vars_3','parser_1.py',145),
  ('vars_4 -> vars_3','vars_4',1,'p_vars_4','parser_1.py',160),
  ('vars_4 -> ID vars_6','vars_4',2,'p_vars_4','parser_1.py',161),
  ('vars_5 -> COMMA vars_3','vars_5',2,'p_vars_5','parser_1.py',166),
  ('vars_5 -> empty','vars_5',1,'p_vars_5','parser_1.py',167),
  ('vars_6 -> punto_id_especial L_S_BRACKET CTE_I R_S_BRACKET vars_7','vars_6',5,'p_vars_6','parser_1.py',172),
  ('vars_6 -> empty','vars_6',1,'p_vars_6','parser_1.py',173),
  ('punto_id_especial -> empty','punto_id_especial',1,'p_punto_id_especial','parser_1.py',177),
  ('vars_7 -> L_S_BRACKET CTE_I R_S_BRACKET var_mat','vars_7',4,'p_vars_7','parser_1.py',184),
  ('vars_7 -> var_array','vars_7',1,'p_vars_7','parser_1.py',185),
  ('var_array -> empty','var_array',1,'p_var_array','parser_1.py',190),
  ('var_mat -> empty','var_mat',1,'p_var_mat','parser_1.py',200),
  ('vars_8 -> vars','vars_8',1,'p_vars_8','parser_1.py',211),
  ('vars_8 -> empty','vars_8',1,'p_vars_8','parser_1.py',212),
  ('param -> tipo_simple ID punto_param param_2','param',4,'p_param','parser_1.py',217),
  ('param -> empty','param',1,'p_param','parser_1.py',218),
  ('param_2 -> COMMA param','param_2',2,'p_param_2','parser_1.py',223),
  ('param_2 -> empty','param_2',1,'p_param_2','parser_1.py',224),
  ('punto_param -> empty','punto_param',1,'p_punto_param','parser_1.py',229),
  ('punto_param_2 -> empty','punto_param_2',1,'p_punto_param_2','parser_1.py',241),
  ('variable -> ID variable_2 variable_point','variable',3,'p_variable','parser_1.py',250),
  ('variable_point -> empty','variable_point',1,'p_variable_point','parser_1.py',255),
  ('variable_2 -> L_S_BRACKET exp R_S_BRACKET variable_3','variable_2',4,'p_variable_2','parser_1.py',277),
  ('variable_2 -> empty','variable_2',1,'p_variable_2','parser_1.py',278),
  ('variable_3 -> L_S_BRACKET exp R_S_BRACKET','variable_3',3,'p_variable_3','parser_1.py',283),
  ('variable_3 -> empty','variable_3',1,'p_variable_3','parser_1.py',284),
  ('estatuto -> asigna','estatuto',1,'p_estatuto','parser_1.py',289),
  ('estatuto -> llamada','estatuto',1,'p_estatuto','parser_1.py',290),
  ('estatuto -> read','estatuto',1,'p_estatuto','parser_1.py',291),
  ('estatuto -> write','estatuto',1,'p_estatuto','parser_1.py',292),
  ('estatuto -> if_1','estatuto',1,'p_estatuto','parser_1.py',293),
  ('estatuto -> for_l','estatuto',1,'p_estatuto','parser_1.py',294),
  ('estatuto -> while_l','estatuto',1,'p_estatuto','parser_1.py',295),
  ('estatuto -> return','estatuto',1,'p_estatuto','parser_1.py',296),
  ('estatuto -> func_extra','estatuto',1,'p_estatuto','parser_1.py',297),
  ('asigna -> variable EQUAL add_operator exp asigna_point SEMICOLON','asigna',6,'p_asigna','parser_1.py',302),
  ('asigna_point -> empty','asigna_point',1,'p_asigna_point','parser_1.py',307),
  ('llamada -> ID LPAR exp llamada_2 RPAR SEMICOLON','llamada',6,'p_llamada','parser_1.py',333),
  ('llamada_2 -> COMMA exp llamada_2','llamada_2',3,'p_llamada_2','parser_1.py',338),
  ('llamada_2 -> empty','llamada_2',1,'p_llamada_2','parser_1.py',339),
  ('read -> READ LPAR variable read_point RPAR SEMICOLON','read',6,'p_read','parser_1.py',344),
  ('read_point -> empty','read_point',1,'p_read_point','parser_1.py',349),
  ('write -> WRITE LPAR write_2 write_3 RPAR SEMICOLON','write',6,'p_write','parser_1.py',360),
  ('write_2 -> exp write_point','write_2',2,'p_write_2','parser_1.py',365),
  ('write_2 -> CTE_S add_constant_s write_point','write_2',3,'p_write_2','parser_1.py',366),
  ('write_3 -> COMMA write_2 write_3','write_3',3,'p_write_3','parser_1.py',371),
  ('write_3 -> empty','write_3',1,'p_write_3','parser_1.py',372),
  ('write_point -> empty','write_point',1,'p_write_point','parser_1.py',377),
  ('if_1 -> IF LPAR exp if_point RPAR L_C_BRACKET estatuto if_2 R_C_BRACKET if_3 SEMICOLON if_point_2','if_1',12,'p_if_1','parser_1.py',390),
  ('if_2 -> estatuto if_2','if_2',2,'p_if_2','parser_1.py',395),
  ('if_2 -> empty','if_2',1,'p_if_2','parser_1.py',396),
  ('if_3 -> ELSE if_point_3 L_C_BRACKET estatuto if_2 R_C_BRACKET','if_3',6,'p_if_3','parser_1.py',401),
  ('if_3 -> empty','if_3',1,'p_if_3','parser_1.py',402),
  ('if_point -> empty','if_point',1,'p_if_point','parser_1.py',407),
  ('if_point_2 -> empty','if_point_2',1,'p_if_point_2','parser_1.py',425),
  ('if_point_3 -> empty','if_point_3',1,'p_if_point_3','parser_1.py',435),
  ('for_l -> FOR LPAR ID for_point_1 EQUAL exp for_point_2 TO exp for_point_3 RPAR L_C_BRACKET estatuto for_l_2 R_C_BRACKET SEMICOLON for_point_4','for_l',17,'p_for_l','parser_1.py',447),
  ('for_l_2 -> estatuto for_l_2','for_l_2',2,'p_for_l_2','parser_1.py',453),
  ('for_l_2 -> empty','for_l_2',1,'p_for_l_2','parser_1.py',454),
  ('for_point_1 -> empty','for_point_1',1,'p_for_point_1','parser_1.py',459),
  ('for_point_2 -> empty','for_point_2',1,'p_for_point_2','parser_1.py',476),
  ('for_point_3 -> empty','for_point_3',1,'p_for_point_3','parser_1.py',501),
  ('for_point_4 -> empty','for_point_4',1,'p_for_point_4','parser_1.py',534),
  ('while_l -> WHILE while_point LPAR exp RPAR while_point_2 L_C_BRACKET estatuto while_l_2 R_C_BRACKET SEMICOLON while_point_3','while_l',12,'p_while_l','parser_1.py',562),
  ('while_l_2 -> estatuto while_l_2','while_l_2',2,'p_while_l_2','parser_1.py',567),
  ('while_l_2 -> empty','while_l_2',1,'p_while_l_2','parser_1.py',568),
  ('while_point -> empty','while_point',1,'p_while_point','parser_1.py',573),
  ('while_point_2 -> empty','while_point_2',1,'p_while_point_2','parser_1.py',581),
  ('while_point_3 -> empty','while_point_3',1,'p_while_point_3','parser_1.py',601),
  ('return -> RETURN check_valid_func LPAR exp RPAR SEMICOLON','return',6,'p_return','parser_1.py',612),
  ('check_valid_func -> empty','check_valid_func',1,'p_check_valid_func','parser_1.py',617),
  ('func_extra -> empty','func_extra',1,'p_func_extra','parser_1.py',626),
  ('exp -> t_exp add_operator_4 exp_2','exp',3,'p_exp','parser_1.py',631),
  ('exp_2 -> OR add_operator exp','exp_2',3,'p_exp_2','parser_1.py',636),
  ('exp_2 -> empty','exp_2',1,'p_exp_2','parser_1.py',637),
  ('t_exp -> g_exp add_operator_4 t_exp_2','t_exp',3,'p_t_exp','parser_1.py',642),
  ('t_exp_2 -> AND add_operator t_exp','t_exp_2',3,'p_t_exp_2','parser_1.py',647),
  ('t_exp_2 -> empty','t_exp_2',1,'p_t_exp_2','parser_1.py',648),
  ('g_exp -> m_exp g_exp_2 add_operator_3','g_exp',3,'p_g_exp','parser_1.py',653),
  ('g_exp_2 -> LESS_EQUAL add_operator m_exp','g_exp_2',3,'p_g_exp_2','parser_1.py',658),
  ('g_exp_2 -> LESS add_operator m_exp','g_exp_2',3,'p_g_exp_2','parser_1.py',659),
  ('g_exp_2 -> GREATER_EQUAL add_operator m_exp','g_exp_2',3,'p_g_exp_2','parser_1.py',660),
  ('g_exp_2 -> GREATER add_operator m_exp','g_exp_2',3,'p_g_exp_2','parser_1.py',661),
  ('g_exp_2 -> COMPARE add_operator m_exp','g_exp_2',3,'p_g_exp_2','parser_1.py',662),
  ('g_exp_2 -> NOT_EQUAL add_operator m_exp','g_exp_2',3,'p_g_exp_2','parser_1.py',663),
  ('g_exp_2 -> empty','g_exp_2',1,'p_g_exp_2','parser_1.py',664),
  ('m_exp -> t add_operator_2 m_exp_2','m_exp',3,'p_m_exp','parser_1.py',669),
  ('m_exp_2 -> PLUS add_operator m_exp','m_exp_2',3,'p_m_exp_2','parser_1.py',674),
  ('m_exp_2 -> MINUS add_operator m_exp','m_exp_2',3,'p_m_exp_2','parser_1.py',675),
  ('m_exp_2 -> empty','m_exp_2',1,'p_m_exp_2','parser_1.py',676),
  ('t -> f add_operator_1 t_2','t',3,'p_t','parser_1.py',681),
  ('t_2 -> TIMES add_operator t','t_2',3,'p_t_2','parser_1.py',686),
  ('t_2 -> DIVIDE add_operator t','t_2',3,'p_t_2','parser_1.py',687),
  ('t_2 -> empty','t_2',1,'p_t_2','parser_1.py',688),
  ('f -> LPAR add_floor exp RPAR remove_floor','f',5,'p_f','parser_1.py',693),
  ('f -> variable','f',1,'p_f','parser_1.py',694),
  ('f -> llamada','f',1,'p_f','parser_1.py',695),
  ('f -> f_2','f',1,'p_f','parser_1.py',696),
  ('f_2 -> CTE_I add_constant_i','f_2',2,'p_f_2','parser_1.py',701),
  ('f_2 -> CTE_F add_constant_f','f_2',2,'p_f_2','parser_1.py',702),
  ('add_floor -> empty','add_floor',1,'p_add_floor','parser_1.py',707),
  ('remove_floor -> empty','remove_floor',1,'p_remove_floor','parser_1.py',714),
  ('add_operator -> empty','add_operator',1,'p_add_operator','parser_1.py',721),
  ('add_operator_1 -> empty','add_operator_1',1,'p_add_operator_1','parser_1.py',730),
  ('add_operator_2 -> empty','add_operator_2',1,'p_add_operator_2','parser_1.py',759),
  ('add_operator_3 -> empty','add_operator_3',1,'p_add_operator_3','parser_1.py',788),
  ('add_operator_4 -> empty','add_operator_4',1,'p_add_operator_4','parser_1.py',817),
  ('add_constant_i -> empty','add_constant_i',1,'p_add_constant_i','parser_1.py',845),
  ('add_constant_s -> empty','add_constant_s',1,'p_add_constant_s','parser_1.py',863),
  ('add_constant_f -> empty','add_constant_f',1,'p_add_constant_f','parser_1.py',880),
  ('function -> FUNC function_2 SEMICOLON function_4','function',4,'p_function','parser_1.py',897),
  ('function_2 -> function_3 ID function_punto1 LPAR param punto_param_2 RPAR L_C_BRACKET body R_C_BRACKET final_func_point','function_2',11,'p_function_2','parser_1.py',902),
  ('function_3 -> tipo_simple','function_3',1,'p_function_3','parser_1.py',907),
  ('function_3 -> VOID','function_3',1,'p_function_3','parser_1.py',908),
  ('function_4 -> function','function_4',1,'p_function_4','parser_1.py',913),
  ('function_4 -> empty','function_4',1,'p_function_4','parser_1.py',914),
  ('function_punto1 -> empty','function_punto1',1,'p_function_punto1','parser_1.py',919),
  ('function_punto2 -> empty','function_punto2',1,'p_function_punto2','parser_1.py',930),
  ('func_agrega_v -> empty','func_agrega_v',1,'p_func_agrega_v','parser_1.py',938),
  ('final_func_point -> empty','final_func_point',1,'p_final_func_point','parser_1.py',950),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',971),
]
