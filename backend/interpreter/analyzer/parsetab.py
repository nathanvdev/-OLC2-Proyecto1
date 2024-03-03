
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftDEQUALDIFERENTMINORMINOREQUALGREATERGREATEREQUALleftPLUSLESSleftBYDIVIDEDMODULrightUMENOSAND BY CONSOLE DEQUAL DIFERENT DIVIDED DOT DOUBLEDOT EQUAL FALSE FLOAT GREATER GREATEREQUAL ID LESS LLAVEA LLAVEC LOG MINOR MINOREQUAL MODUL NOT NUMBER OR PARA PARC PLUS RBOOLEAN RCONST RELSE RFLOAT RFOR RIF RNUMBER RSTRING RVAR RWHILE SEMICOLON STRING TRUEstart    : instrucciones instrucciones    : instrucciones instruccion\n                        | instruccion instruccion  : print\n                    | declare\n                    | declareConst\n                    | assignVar\n                    | if_else\n                    | while_\n                    | for_print    : CONSOLE DOT LOG PARA expression PARCdeclare  : RVAR ID DOUBLEDOT type EQUAL expression\n                | RVAR ID EQUAL expression\n                | RVAR ID DOUBLEDOT typedeclareConst : RCONST ID DOUBLEDOT type EQUAL expression\n                    | RCONST ID EQUAL expression\n                    | RCONST ID DOUBLEDOT typeassignVar    : ID EQUAL expression\n                    | ID PLUS EQUAL expression\n                    | ID LESS EQUAL expressionif_else  : RIF PARA expression PARC LLAVEA instrucciones LLAVEC elseelse : RELSE LLAVEA instrucciones LLAVEC\n            | RELSE if_else\n            |while_   : RWHILE PARA expression PARC LLAVEA instrucciones LLAVECfor_ : RFOR PARA declare SEMICOLON relacional SEMICOLON id_ PLUS PLUS PARC LLAVEA instrucciones LLAVEC\n            | RFOR PARA declare SEMICOLON relacional SEMICOLON id_ LESS LESS PARC LLAVEA instrucciones LLAVECexpression   : primitivo \n                    | aritmetica\n                    | relacional\n                    | logica\n                    | id_id_   : IDaritmetica   : expression PLUS expression\n                    | expression BY expression\n                    | expression DIVIDED expression\n                    | expression LESS expression\n                    | expression MODUL expression\n                    | LESS expression %prec UMENOSrelacional   : expression DEQUAL expression\n                    | expression DIFERENT expression\n                    | expression MINOR expression\n                    | expression MINOREQUAL expression\n                    | expression GREATER expression\n                    | expression GREATEREQUAL expressionlogica   : boolean AND boolean\n                | boolean OR boolean\n                | NOT booleanprimitivo    : NUMBER\n                    | FLOAT\n                    | STRING\n                    | booleanboolean  : TRUE\n                | FALSEtype     : RNUMBER\n                | RFLOAT\n                | RSTRING\n                | RBOOLEAN'
    
_lr_action_items = {'CONSOLE':([0,2,3,4,5,6,7,8,9,10,18,31,32,33,34,35,36,37,38,39,40,41,44,45,54,55,56,57,58,59,73,74,75,76,77,78,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,102,103,104,105,106,108,109,111,115,116,119,122,123,124,125,126,127,128,],[11,11,-3,-4,-5,-6,-7,-8,-9,-10,-2,-33,-18,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,-14,-55,-56,-57,-58,-13,-39,-48,-19,-20,-17,-16,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,11,11,-11,-12,-15,11,11,-24,-25,-21,11,-23,11,-22,11,11,11,11,-26,-27,]),'RVAR':([0,2,3,4,5,6,7,8,9,10,18,27,31,32,33,34,35,36,37,38,39,40,41,44,45,54,55,56,57,58,59,73,74,75,76,77,78,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,102,103,104,105,106,108,109,111,115,116,119,122,123,124,125,126,127,128,],[12,12,-3,-4,-5,-6,-7,-8,-9,-10,-2,12,-33,-18,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,-14,-55,-56,-57,-58,-13,-39,-48,-19,-20,-17,-16,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,12,12,-11,-12,-15,12,12,-24,-25,-21,12,-23,12,-22,12,12,12,12,-26,-27,]),'RCONST':([0,2,3,4,5,6,7,8,9,10,18,31,32,33,34,35,36,37,38,39,40,41,44,45,54,55,56,57,58,59,73,74,75,76,77,78,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,102,103,104,105,106,108,109,111,115,116,119,122,123,124,125,126,127,128,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-2,-33,-18,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,-14,-55,-56,-57,-58,-13,-39,-48,-19,-20,-17,-16,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,14,14,-11,-12,-15,14,14,-24,-25,-21,14,-23,14,-22,14,14,14,14,-26,-27,]),'ID':([0,2,3,4,5,6,7,8,9,10,12,14,18,21,25,26,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,73,74,75,76,77,78,81,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,102,103,104,105,106,107,108,109,111,115,116,119,122,123,124,125,126,127,128,],[13,13,-3,-4,-5,-6,-7,-8,-9,-10,20,24,-2,31,31,31,31,-33,-18,-28,-29,-30,-31,-32,-49,-50,-51,-52,31,-53,-54,31,31,31,31,-14,-55,-56,-57,-58,-13,31,31,31,31,31,31,31,31,31,31,31,-39,-48,-19,-20,-17,-16,31,31,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,31,13,13,-11,-12,-15,13,13,31,-24,-25,-21,13,-23,13,-22,13,13,13,13,-26,-27,]),'RIF':([0,2,3,4,5,6,7,8,9,10,18,31,32,33,34,35,36,37,38,39,40,41,44,45,54,55,56,57,58,59,73,74,75,76,77,78,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,102,103,104,105,106,108,109,111,112,115,116,119,122,123,124,125,126,127,128,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-2,-33,-18,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,-14,-55,-56,-57,-58,-13,-39,-48,-19,-20,-17,-16,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,15,15,-11,-12,-15,15,15,-24,-25,-21,15,15,-23,15,-22,15,15,15,15,-26,-27,]),'RWHILE':([0,2,3,4,5,6,7,8,9,10,18,31,32,33,34,35,36,37,38,39,40,41,44,45,54,55,56,57,58,59,73,74,75,76,77,78,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,102,103,104,105,106,108,109,111,115,116,119,122,123,124,125,126,127,128,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-2,-33,-18,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,-14,-55,-56,-57,-58,-13,-39,-48,-19,-20,-17,-16,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,16,16,-11,-12,-15,16,16,-24,-25,-21,16,-23,16,-22,16,16,16,16,-26,-27,]),'RFOR':([0,2,3,4,5,6,7,8,9,10,18,31,32,33,34,35,36,37,38,39,40,41,44,45,54,55,56,57,58,59,73,74,75,76,77,78,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,102,103,104,105,106,108,109,111,115,116,119,122,123,124,125,126,127,128,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-2,-33,-18,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,-14,-55,-56,-57,-58,-13,-39,-48,-19,-20,-17,-16,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,17,17,-11,-12,-15,17,17,-24,-25,-21,17,-23,17,-22,17,17,17,17,-26,-27,]),'$end':([1,2,3,4,5,6,7,8,9,10,18,31,32,33,34,35,36,37,38,39,40,41,44,45,54,55,56,57,58,59,73,74,75,76,77,78,84,85,86,87,88,89,90,91,92,93,94,95,96,102,103,104,108,109,111,116,122,127,128,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-2,-33,-18,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,-14,-55,-56,-57,-58,-13,-39,-48,-19,-20,-17,-16,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,-11,-12,-15,-24,-25,-21,-23,-22,-26,-27,]),'LLAVEC':([3,4,5,6,7,8,9,10,18,31,32,33,34,35,36,37,38,39,40,41,44,45,54,55,56,57,58,59,73,74,75,76,77,78,84,85,86,87,88,89,90,91,92,93,94,95,96,102,103,104,105,106,108,109,111,116,119,122,125,126,127,128,],[-3,-4,-5,-6,-7,-8,-9,-10,-2,-33,-18,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,-14,-55,-56,-57,-58,-13,-39,-48,-19,-20,-17,-16,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,-11,-12,-15,108,109,-24,-25,-21,-23,122,-22,127,128,-26,-27,]),'DOT':([11,],[19,]),'EQUAL':([13,20,22,23,24,54,55,56,57,58,77,],[21,30,46,47,49,83,-55,-56,-57,-58,97,]),'PLUS':([13,31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,110,113,],[22,-33,60,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,60,60,60,-39,-48,60,60,60,60,-34,-35,-36,-37,-38,60,60,60,60,60,60,-46,-47,-30,60,60,60,113,117,]),'LESS':([13,21,25,26,30,31,32,33,34,35,36,37,38,39,40,41,42,44,45,46,47,49,50,51,53,59,60,61,62,63,64,65,66,67,68,69,70,73,74,75,76,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,100,101,103,104,110,114,],[23,42,42,42,42,-33,63,-28,-29,-30,-31,-32,-49,-50,-51,-52,42,-53,-54,42,42,42,63,63,42,63,42,42,42,42,42,42,42,42,42,42,42,-39,-48,63,63,63,42,63,42,-34,-35,-36,-37,-38,63,63,63,63,63,63,-46,-47,42,-30,63,63,63,114,118,]),'PARA':([15,16,17,28,],[25,26,27,53,]),'LOG':([19,],[28,]),'DOUBLEDOT':([20,24,],[29,48,]),'NUMBER':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'FLOAT':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'STRING':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'NOT':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,],[43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'TRUE':([21,25,26,30,42,43,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,71,72,81,83,97,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'FALSE':([21,25,26,30,42,43,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,71,72,81,83,97,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'RNUMBER':([29,48,],[55,55,]),'RFLOAT':([29,48,],[56,56,]),'RSTRING':([29,48,],[57,57,]),'RBOOLEAN':([29,48,],[58,58,]),'BY':([31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,],[-33,61,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,61,61,61,-39,-48,61,61,61,61,61,-35,-36,61,-38,61,61,61,61,61,61,-46,-47,-30,61,61,61,]),'DIVIDED':([31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,],[-33,62,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,62,62,62,-39,-48,62,62,62,62,62,-35,-36,62,-38,62,62,62,62,62,62,-46,-47,-30,62,62,62,]),'MODUL':([31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,],[-33,64,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,64,64,64,-39,-48,64,64,64,64,64,-35,-36,64,-38,64,64,64,64,64,64,-46,-47,-30,64,64,64,]),'DEQUAL':([31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,],[-33,65,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,65,65,65,-39,-48,65,65,65,65,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,-30,65,65,65,]),'DIFERENT':([31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,],[-33,66,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,66,66,66,-39,-48,66,66,66,66,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,-30,66,66,66,]),'MINOR':([31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,],[-33,67,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,67,67,67,-39,-48,67,67,67,67,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,-30,67,67,67,]),'MINOREQUAL':([31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,],[-33,68,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,68,68,68,-39,-48,68,68,68,68,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,-30,68,68,68,]),'GREATER':([31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,],[-33,69,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,69,69,69,-39,-48,69,69,69,69,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,-30,69,69,69,]),'GREATEREQUAL':([31,32,33,34,35,36,37,38,39,40,41,44,45,50,51,59,73,74,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,95,96,100,101,103,104,],[-33,70,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,70,70,70,-39,-48,70,70,70,70,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,-30,70,70,70,]),'PARC':([31,33,34,35,36,37,38,39,40,41,44,45,50,51,73,74,82,84,85,86,87,88,89,90,91,92,93,94,95,96,117,118,],[-33,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,79,80,-39,-48,102,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,120,121,]),'SEMICOLON':([31,33,34,35,36,37,38,39,40,41,44,45,52,54,55,56,57,58,59,73,74,84,85,86,87,88,89,90,91,92,93,94,95,96,100,103,],[-33,-28,-29,-30,-31,-32,-49,-50,-51,-52,-53,-54,81,-14,-55,-56,-57,-58,-13,-39,-48,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,107,-12,]),'AND':([41,44,45,],[71,-53,-54,]),'OR':([41,44,45,],[72,-53,-54,]),'LLAVEA':([79,80,112,120,121,],[98,99,115,123,124,]),'RELSE':([108,],[112,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'instrucciones':([0,98,99,115,123,124,],[2,105,106,119,125,126,]),'instruccion':([0,2,98,99,105,106,115,119,123,124,125,126,],[3,18,3,3,18,18,3,18,3,3,18,18,]),'print':([0,2,98,99,105,106,115,119,123,124,125,126,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'declare':([0,2,27,98,99,105,106,115,119,123,124,125,126,],[5,5,52,5,5,5,5,5,5,5,5,5,5,]),'declareConst':([0,2,98,99,105,106,115,119,123,124,125,126,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'assignVar':([0,2,98,99,105,106,115,119,123,124,125,126,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'if_else':([0,2,98,99,105,106,112,115,119,123,124,125,126,],[8,8,8,8,8,8,116,8,8,8,8,8,8,]),'while_':([0,2,98,99,105,106,115,119,123,124,125,126,],[9,9,9,9,9,9,9,9,9,9,9,9,]),'for_':([0,2,98,99,105,106,115,119,123,124,125,126,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'expression':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,],[32,50,51,59,73,75,76,78,82,84,85,86,87,88,89,90,91,92,93,94,101,103,104,]),'primitivo':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'aritmetica':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'relacional':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,100,35,35,]),'logica':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'id_':([21,25,26,30,42,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,81,83,97,107,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,110,]),'boolean':([21,25,26,30,42,43,46,47,49,53,60,61,62,63,64,65,66,67,68,69,70,71,72,81,83,97,],[41,41,41,41,41,74,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,95,96,41,41,41,]),'type':([29,48,],[54,77,]),'else':([108,],[111,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> instrucciones','start',1,'p_start','grammar.py',139),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','grammar.py',146),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','grammar.py',147),
  ('instruccion -> print','instruccion',1,'p_instruccion','grammar.py',156),
  ('instruccion -> declare','instruccion',1,'p_instruccion','grammar.py',157),
  ('instruccion -> declareConst','instruccion',1,'p_instruccion','grammar.py',158),
  ('instruccion -> assignVar','instruccion',1,'p_instruccion','grammar.py',159),
  ('instruccion -> if_else','instruccion',1,'p_instruccion','grammar.py',160),
  ('instruccion -> while_','instruccion',1,'p_instruccion','grammar.py',161),
  ('instruccion -> for_','instruccion',1,'p_instruccion','grammar.py',162),
  ('print -> CONSOLE DOT LOG PARA expression PARC','print',6,'p_print','grammar.py',167),
  ('declare -> RVAR ID DOUBLEDOT type EQUAL expression','declare',6,'p_declare','grammar.py',172),
  ('declare -> RVAR ID EQUAL expression','declare',4,'p_declare','grammar.py',173),
  ('declare -> RVAR ID DOUBLEDOT type','declare',4,'p_declare','grammar.py',174),
  ('declareConst -> RCONST ID DOUBLEDOT type EQUAL expression','declareConst',6,'p_declareConst','grammar.py',188),
  ('declareConst -> RCONST ID EQUAL expression','declareConst',4,'p_declareConst','grammar.py',189),
  ('declareConst -> RCONST ID DOUBLEDOT type','declareConst',4,'p_declareConst','grammar.py',190),
  ('assignVar -> ID EQUAL expression','assignVar',3,'p_assignVar','grammar.py',203),
  ('assignVar -> ID PLUS EQUAL expression','assignVar',4,'p_assignVar','grammar.py',204),
  ('assignVar -> ID LESS EQUAL expression','assignVar',4,'p_assignVar','grammar.py',205),
  ('if_else -> RIF PARA expression PARC LLAVEA instrucciones LLAVEC else','if_else',8,'p_if_else','grammar.py',216),
  ('else -> RELSE LLAVEA instrucciones LLAVEC','else',4,'p_else','grammar.py',222),
  ('else -> RELSE if_else','else',2,'p_else','grammar.py',223),
  ('else -> <empty>','else',0,'p_else','grammar.py',224),
  ('while_ -> RWHILE PARA expression PARC LLAVEA instrucciones LLAVEC','while_',7,'p_while','grammar.py',234),
  ('for_ -> RFOR PARA declare SEMICOLON relacional SEMICOLON id_ PLUS PLUS PARC LLAVEA instrucciones LLAVEC','for_',13,'p_for','grammar.py',240),
  ('for_ -> RFOR PARA declare SEMICOLON relacional SEMICOLON id_ LESS LESS PARC LLAVEA instrucciones LLAVEC','for_',13,'p_for','grammar.py',241),
  ('expression -> primitivo','expression',1,'p_expression','grammar.py',249),
  ('expression -> aritmetica','expression',1,'p_expression','grammar.py',250),
  ('expression -> relacional','expression',1,'p_expression','grammar.py',251),
  ('expression -> logica','expression',1,'p_expression','grammar.py',252),
  ('expression -> id_','expression',1,'p_expression','grammar.py',253),
  ('id_ -> ID','id_',1,'p_id_','grammar.py',258),
  ('aritmetica -> expression PLUS expression','aritmetica',3,'p_aritmetica','grammar.py',265),
  ('aritmetica -> expression BY expression','aritmetica',3,'p_aritmetica','grammar.py',266),
  ('aritmetica -> expression DIVIDED expression','aritmetica',3,'p_aritmetica','grammar.py',267),
  ('aritmetica -> expression LESS expression','aritmetica',3,'p_aritmetica','grammar.py',268),
  ('aritmetica -> expression MODUL expression','aritmetica',3,'p_aritmetica','grammar.py',269),
  ('aritmetica -> LESS expression','aritmetica',2,'p_aritmetica','grammar.py',270),
  ('relacional -> expression DEQUAL expression','relacional',3,'p_relacional','grammar.py',296),
  ('relacional -> expression DIFERENT expression','relacional',3,'p_relacional','grammar.py',297),
  ('relacional -> expression MINOR expression','relacional',3,'p_relacional','grammar.py',298),
  ('relacional -> expression MINOREQUAL expression','relacional',3,'p_relacional','grammar.py',299),
  ('relacional -> expression GREATER expression','relacional',3,'p_relacional','grammar.py',300),
  ('relacional -> expression GREATEREQUAL expression','relacional',3,'p_relacional','grammar.py',301),
  ('logica -> boolean AND boolean','logica',3,'p_logica','grammar.py',325),
  ('logica -> boolean OR boolean','logica',3,'p_logica','grammar.py',326),
  ('logica -> NOT boolean','logica',2,'p_logica','grammar.py',327),
  ('primitivo -> NUMBER','primitivo',1,'p_primitivo','grammar.py',340),
  ('primitivo -> FLOAT','primitivo',1,'p_primitivo','grammar.py',341),
  ('primitivo -> STRING','primitivo',1,'p_primitivo','grammar.py',342),
  ('primitivo -> boolean','primitivo',1,'p_primitivo','grammar.py',343),
  ('boolean -> TRUE','boolean',1,'p_boolean','grammar.py',358),
  ('boolean -> FALSE','boolean',1,'p_boolean','grammar.py',359),
  ('type -> RNUMBER','type',1,'p_type','grammar.py',370),
  ('type -> RFLOAT','type',1,'p_type','grammar.py',371),
  ('type -> RSTRING','type',1,'p_type','grammar.py',372),
  ('type -> RBOOLEAN','type',1,'p_type','grammar.py',373),
]
