
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND ASS ATE COLON COM DIV ENTAO EQU ESCREVA FIM FLUTUANTE GEQ GRT ID INTEIRO LBR LEIA LEQ LET LPAR NEQ NOT OR RBR REPITA RETORNA RPAR SE SENAO SUB TIMESprograma : lista_declaracoes\n        lista_declaracoes : lista_declaracoes declaracao\n            | declaracao\n            | error\n        \n        declaracao : declaracao_variaveis\n            | inicializacao_variaveis\n            | declaracao_funcao\n            | error\n        declaracao_variaveis : tipo COLON lista_variaveisdeclaracao_variaveis : tipo COLON errorinicializacao_variaveis : atribuicao\n        declaracao_funcao_nova : INTEIRO ID LPAR lista_parametros RPAR corpo retorna FIM\n            | FLUTUANTE ID LPAR lista_parametros RPAR corpo retorna FIM\n            | ID LPAR lista_parametros RPAR corpo FIM\n        declaracao_funcao_nova : INTEIRO ID LPAR lista_parametros RPAR corpo error FIM\n            | FLUTUANTE ID LPAR lista_parametros RPAR corpo error FIM\n        \n        declaracao_funcao : tipo cabecalho\n            | cabecalho\n        \n        declaracao_funcao : tipo cabecalho error\n            | cabecalho error\n        cabecalho : ID LPAR lista_parametros RPAR corpo FIMcabecalho : ID LPAR lista_parametros RPAR corpo errortipo : INTEIRO\n            | FLUTUANTE\n        lista_variaveis : lista_variaveis COM var\n            | var\n        lista_variaveis : lista_variaveis COM error\n        atribuicao : var simbolo_atribuicao expressao\n            | condicional\n            | NOT condicional\n        \n        condicional : expressao_simples operador_relacional expressao_aditiva\n            | LPAR condicional RPAR\n            | condicional simbolo_condicional condicional\n            | condicional simbolo_condicional error\n            | LPAR error RPAR\n            | error simbolo_condicional condicional\n        \n        simbolo_condicional : OR\n            | AND\n        simbolo_atribuicao : ASSatribuicao : var simbolo_atribuicao error\n        corpo : corpo acao\n            | empty\n        \n        acao : expressao\n            | declaracao_variaveis\n            | se\n            | repita\n            | leia\n            | escreva\n            | retorna\n        \n        se : SE expressao ENTAO corpo FIM\n            | SE expressao ENTAO corpo SENAO corpo FIM\n        \n        se : SE expressao error corpo FIM\n            | error SENAO corpo FIM\n            | SE expressao SENAO corpo error\n        repita : REPITA corpo ATE expressaorepita : REPITA corpo errorleia : LEIA LPAR expressao RPARescreva : ESCREVA LPAR expressao RPARretorna :  RETORNA LPAR expressao RPARretorna :  RETORNA LPAR error RPAR\n        var : ID\n            | ID indice\n            | ID lista_dimensions\n        \n        expressao : expressao_simples\n            | atribuicao\n        \n        lista_parametros : lista_parametros COM parametro\n            | parametro\n            | empty\n        \n        indice : indice LBR expressao RBR\n            | LBR expressao RBR\n        \n        indice : indice LBR error RBR\n            | LBR error RBR\n            | error RBR\n            | LBR error\n        \n        expressao_simples : expressao_aditiva\n            | expressao_simples operador_relacional expressao_aditiva\n        \n        parametro : tipo COLON var\n            | parametro\n        \n        lista_dimensions : dimension\n            | lista_dimensions dimension\n        dimension : LBR RBR\n        operador_relacional : LET\n            | GRT\n            | EQU\n            | NEQ\n            | LEQ\n            | GEQ\n        \n        expressao_aditiva : expressao_multiplicativa\n            | expressao_aditiva operador_soma expressao_multiplicativa\n        \n        expressao_multiplicativa : expressao_unaria\n            | expressao_multiplicativa operador_multiplicacao expressao_unaria\n        \n        operador_soma : ADD\n            | SUB\n        \n        operador_multiplicacao : TIMES\n            | DIV\n        \n        expressao_unaria : fator\n            | operador_soma fator\n        \n        fator : LPAR expressao RPAR\n            | var\n            | chamada_funcao\n            | numero\n        \n        numero : INTEIRO\n            | FLUTUANTE\n        chamada_funcao : ID LPAR lista_argumentos RPAR\n        lista_argumentos : lista_argumentos COM expressao\n            | expressao\n            | empty\n        empty :'
    
_lr_action_items = {'SUB':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,22,23,24,25,28,29,30,31,32,33,35,36,37,38,39,40,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,72,73,74,75,76,77,78,79,80,81,82,90,91,93,94,95,96,97,98,99,100,103,104,105,106,109,110,117,119,120,123,124,125,126,127,128,129,130,131,132,134,135,136,137,139,141,143,145,146,147,148,149,150,151,152,153,154,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[2,-100,-93,-101,-96,-7,-18,-4,-103,2,-92,2,2,-102,-3,2,-29,-11,-5,-6,-88,-90,-99,-61,-20,-37,2,-38,2,-30,-102,-103,-99,-61,2,-97,-65,-8,-2,2,-84,-87,2,-86,-85,-83,-82,-94,-95,2,2,-39,2,2,-63,-79,-62,-17,-36,-89,2,-64,-35,-32,-98,-33,-34,2,-91,-28,-40,-74,-81,-80,-73,2,-19,-10,-61,-26,-9,2,-104,2,-108,-70,-72,2,2,-42,-69,-71,-27,-25,-45,-47,-48,-22,-21,-43,2,-108,-46,-49,-41,-44,-108,2,2,2,2,2,-108,-108,-108,-56,2,-53,2,2,2,-55,-57,-58,-59,-60,-54,-50,-108,-52,2,-51,]),'SENAO':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,44,63,65,66,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,97,98,99,100,104,109,110,117,120,123,124,125,126,127,128,129,130,132,136,137,139,141,144,151,153,159,160,162,164,165,166,167,168,169,170,172,174,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-63,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-10,-61,-26,-9,-104,-70,-72,-31,-42,-69,-71,-27,-25,-45,-47,-48,143,-43,-46,-49,-41,-44,150,-108,143,143,-53,171,-55,-57,-58,-59,-60,143,-50,-52,-51,]),'$end':([1,3,4,5,6,7,9,15,16,17,18,19,20,22,23,24,26,28,33,35,36,37,38,40,44,46,47,63,65,66,67,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,96,97,98,99,100,104,109,110,117,123,124,125,126,130,131,],[-100,-101,-96,-7,-18,-4,-75,-3,-1,-29,-11,-5,-6,-88,-90,-99,0,-20,-30,-102,-103,-99,-61,-97,-65,-8,-2,-63,-79,-62,-17,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-19,-10,-61,-26,-9,-104,-70,-72,-31,-69,-71,-27,-25,-22,-21,]),'SE':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,44,63,65,66,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,97,98,99,100,104,106,109,110,117,119,120,123,124,125,126,127,128,129,132,135,136,137,139,141,143,145,149,150,151,152,153,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-63,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-10,-61,-26,-9,-104,-108,-70,-72,-31,134,-42,-69,-71,-27,-25,-45,-47,-48,-43,-108,-46,-49,-41,-44,-108,134,134,-108,-108,-108,-56,-53,134,134,134,-55,-57,-58,-59,-60,-54,-50,-108,-52,134,-51,]),'REPITA':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,44,63,65,66,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,97,98,99,100,104,106,109,110,117,119,120,123,124,125,126,127,128,129,132,135,136,137,139,141,143,145,149,150,151,152,153,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-63,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-10,-61,-26,-9,-104,-108,-70,-72,-31,135,-42,-69,-71,-27,-25,-45,-47,-48,-43,-108,-46,-49,-41,-44,-108,135,135,-108,-108,-108,-56,-53,135,135,135,-55,-57,-58,-59,-60,-54,-50,-108,-52,135,-51,]),'LBR':([25,38,63,65,66,90,91,93,94,98,109,110,123,124,],[62,62,92,-79,95,-74,-81,-80,-73,62,-70,-72,-69,-71,]),'RETORNA':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,44,63,65,66,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,97,98,99,100,104,106,109,110,117,119,120,123,124,125,126,127,128,129,132,135,136,137,139,141,143,145,149,150,151,152,153,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-63,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-10,-61,-26,-9,-104,-108,-70,-72,-31,142,-42,-69,-71,-27,-25,-45,-47,-48,-43,-108,-46,-49,-41,-44,-108,142,142,-108,-108,-108,-56,-53,142,142,142,-55,-57,-58,-59,-60,-54,-50,-108,-52,142,-51,]),'ASS':([24,25,38,63,65,66,90,91,93,94,109,110,123,124,],[60,-61,-61,-63,-79,-62,-74,-81,-80,-73,-70,-72,-69,-71,]),'RPAR':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,41,42,43,44,45,61,63,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,91,93,94,98,101,102,104,109,110,115,117,118,121,122,123,124,155,156,157,158,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-64,74,75,-65,76,-108,-63,-79,-62,-36,-89,-108,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,104,-68,-67,-106,106,-74,-81,-80,-73,-61,-108,-107,-104,-70,-72,-68,-31,-105,-66,-77,-69,-71,165,166,167,168,]),'RBR':([1,3,4,9,17,22,23,24,33,35,36,37,38,40,44,62,63,64,65,66,70,71,73,74,75,76,77,78,79,80,81,82,89,90,91,92,93,94,104,109,110,111,112,117,123,124,],[-100,-101,-96,-75,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,91,-63,94,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,109,110,-81,91,-80,-73,-104,-70,-72,123,124,-31,-69,-71,]),'LEQ':([1,3,4,8,9,14,21,22,23,24,25,35,36,37,38,40,41,63,65,66,71,73,76,79,80,90,91,93,94,104,109,110,117,123,124,],[-100,-101,-96,-103,-75,-102,52,-88,-90,-99,-61,-102,-103,-99,-61,-97,52,-63,-79,-62,-89,52,-98,-76,-91,-74,-81,-80,-73,-104,-70,-72,-76,-69,-71,]),'error':([0,1,3,4,5,6,7,8,9,11,13,14,15,16,17,18,19,20,22,23,24,25,28,29,30,31,33,35,36,37,38,39,40,44,46,47,48,59,60,61,62,63,65,66,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,90,91,93,94,95,96,97,98,99,100,104,105,106,109,110,113,117,119,120,123,124,125,126,127,128,129,130,131,132,134,135,136,137,139,141,143,144,145,146,147,148,149,150,151,152,153,154,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[7,-100,-101,-96,-7,28,-4,-103,-75,34,42,-102,-3,46,-29,-11,-5,-6,-88,-90,-99,64,-20,-37,34,-38,-30,-102,-103,-99,64,34,-97,-65,-8,-2,78,82,-39,34,90,-63,-79,-62,96,97,-36,-89,34,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,112,-19,-10,64,-26,-9,-104,34,-108,-70,-72,125,-31,130,-42,-69,-71,-27,-25,-45,-47,-48,-22,-21,-43,34,-108,-46,-49,-41,-44,-108,152,153,34,34,158,159,-108,-108,-108,-56,34,-53,169,159,159,-55,-57,-58,-59,-60,-54,-50,-108,-52,159,-51,]),'FIM':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,44,63,65,66,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,97,98,99,100,104,106,109,110,117,119,120,123,124,125,126,127,128,129,132,136,137,139,141,143,149,151,152,153,160,162,163,164,165,166,167,168,169,170,171,172,173,174,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-63,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-10,-61,-26,-9,-104,-108,-70,-72,-31,131,-42,-69,-71,-27,-25,-45,-47,-48,-43,-46,-49,-41,-44,-108,160,-108,-108,-56,-53,170,172,-55,-57,-58,-59,-60,-54,-50,-108,-52,174,-51,]),'FLUTUANTE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,28,29,30,31,32,33,35,36,37,38,39,40,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,72,73,74,75,76,77,78,79,80,81,82,90,91,93,94,95,96,97,98,99,100,101,103,104,105,106,107,109,110,117,119,120,123,124,125,126,127,128,129,130,131,132,134,135,136,137,139,141,143,145,146,147,148,149,150,151,152,153,154,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[8,-100,-93,-101,-96,-7,-18,-4,-103,-75,-92,36,36,36,-102,-3,8,-29,-11,-5,-6,-88,-90,-99,-20,-37,36,-38,36,-30,-102,-103,-99,-61,36,-97,-65,-8,-2,36,-84,-87,36,-86,-85,-83,-82,-94,-95,36,36,-39,8,36,-63,-79,-62,-17,-36,-89,36,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,36,-19,-10,-61,-26,-9,116,36,-104,36,-108,116,-70,-72,-31,8,-42,-69,-71,-27,-25,-45,-47,-48,-22,-21,-43,36,-108,-46,-49,-41,-44,-108,8,36,36,36,8,-108,-108,-108,-56,36,-53,8,8,8,-55,-57,-58,-59,-60,-54,-50,-108,-52,8,-51,]),'GRT':([1,3,4,8,9,14,21,22,23,24,25,35,36,37,38,40,41,63,65,66,71,73,76,79,80,90,91,93,94,104,109,110,117,123,124,],[-100,-101,-96,-103,-75,-102,54,-88,-90,-99,-61,-102,-103,-99,-61,-97,54,-63,-79,-62,-89,54,-98,-76,-91,-74,-81,-80,-73,-104,-70,-72,-76,-69,-71,]),'COM':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,44,61,63,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,90,91,93,94,98,99,100,101,102,104,109,110,115,117,118,121,122,123,124,125,126,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-108,-63,-79,-62,-36,-89,-108,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,105,-68,-67,-106,107,-74,-81,-80,-73,-61,-26,113,-108,-107,-104,-70,-72,-68,-31,-105,-66,-77,-69,-71,-27,-25,]),'TIMES':([1,3,4,8,14,22,23,24,25,35,36,37,38,40,63,65,66,71,76,80,90,91,93,94,104,109,110,123,124,],[-100,-101,-96,-103,-102,56,-90,-99,-61,-102,-103,-99,-61,-97,-63,-79,-62,56,-98,-91,-74,-81,-80,-73,-104,-70,-72,-69,-71,]),'ATE':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,44,63,65,66,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,97,98,99,100,104,109,110,117,120,123,124,125,126,127,128,129,132,135,136,137,139,141,145,153,160,164,165,166,167,168,169,170,172,174,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-63,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-10,-61,-26,-9,-104,-70,-72,-31,-42,-69,-71,-27,-25,-45,-47,-48,-43,-108,-46,-49,-41,-44,154,-56,-53,-55,-57,-58,-59,-60,-54,-50,-52,-51,]),'AND':([1,3,4,7,17,22,23,33,34,35,36,37,38,40,42,43,46,63,65,66,70,71,74,75,76,77,78,79,80,82,90,91,93,94,104,109,110,112,117,123,124,130,153,158,159,169,],[-100,-101,-96,31,31,-88,-90,31,31,-102,-103,-99,-61,-97,31,31,31,-63,-79,-62,31,-89,-35,-32,-98,31,31,-31,-91,31,31,-81,-80,-73,-104,-70,-72,31,-31,-69,-71,31,31,31,31,31,]),'LEIA':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,44,63,65,66,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,97,98,99,100,104,106,109,110,117,119,120,123,124,125,126,127,128,129,132,135,136,137,139,141,143,145,149,150,151,152,153,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-63,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-10,-61,-26,-9,-104,-108,-70,-72,-31,138,-42,-69,-71,-27,-25,-45,-47,-48,-43,-108,-46,-49,-41,-44,-108,138,138,-108,-108,-108,-56,-53,138,138,138,-55,-57,-58,-59,-60,-54,-50,-108,-52,138,-51,]),'NOT':([0,1,3,4,5,6,7,8,9,13,14,15,16,17,18,19,20,22,23,24,28,33,35,36,37,38,39,40,44,46,47,59,60,61,62,63,65,66,67,70,71,72,73,74,75,76,77,78,79,80,81,82,90,91,93,94,95,96,97,98,99,100,104,105,106,109,110,117,119,120,123,124,125,126,127,128,129,130,131,132,134,135,136,137,139,141,143,145,146,147,148,149,150,151,152,153,154,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[11,-100,-101,-96,-7,-18,-4,-103,-75,11,-102,-3,11,-29,-11,-5,-6,-88,-90,-99,-20,-30,-102,-103,-99,-61,11,-97,-65,-8,-2,11,-39,11,11,-63,-79,-62,-17,-36,-89,11,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,11,-19,-10,-61,-26,-9,-104,11,-108,-70,-72,-31,11,-42,-69,-71,-27,-25,-45,-47,-48,-22,-21,-43,11,-108,-46,-49,-41,-44,-108,11,11,11,11,11,-108,-108,-108,-56,11,-53,11,11,11,-55,-57,-58,-59,-60,-54,-50,-108,-52,11,-51,]),'LPAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,25,28,29,30,31,32,33,35,36,37,38,39,40,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,90,91,93,94,95,96,97,98,99,100,103,104,105,106,109,110,117,119,120,123,124,125,126,127,128,129,130,131,132,134,135,136,137,138,139,140,141,142,143,145,146,147,148,149,150,151,152,153,154,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[13,-100,-93,-101,-96,-7,-18,-4,-103,-75,-92,13,39,13,-102,-3,13,-29,-11,-5,-6,-88,-90,-99,61,-20,-37,13,-38,39,-30,-102,-103,-99,72,13,-97,-65,-8,-2,13,-84,-87,39,-86,-85,-83,-82,-94,-95,39,13,-39,13,13,-63,-79,-62,-17,101,-36,-89,13,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,13,-19,-10,-61,-26,-9,39,-104,13,-108,-70,-72,-31,13,-42,-69,-71,-27,-25,-45,-47,-48,-22,-21,-43,13,-108,-46,-49,146,-41,147,-44,148,-108,13,13,13,13,13,-108,-108,-108,-56,13,-53,13,13,13,-55,-57,-58,-59,-60,-54,-50,-108,-52,13,-51,]),'INTEIRO':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,28,29,30,31,32,33,35,36,37,38,39,40,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,72,73,74,75,76,77,78,79,80,81,82,90,91,93,94,95,96,97,98,99,100,101,103,104,105,106,107,109,110,117,119,120,123,124,125,126,127,128,129,130,131,132,134,135,136,137,139,141,143,145,146,147,148,149,150,151,152,153,154,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[14,-100,-93,-101,-96,-7,-18,-4,-103,-75,-92,35,35,35,-102,-3,14,-29,-11,-5,-6,-88,-90,-99,-20,-37,35,-38,35,-30,-102,-103,-99,-61,35,-97,-65,-8,-2,35,-84,-87,35,-86,-85,-83,-82,-94,-95,35,35,-39,14,35,-63,-79,-62,-17,-36,-89,35,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,35,-19,-10,-61,-26,-9,114,35,-104,35,-108,114,-70,-72,-31,14,-42,-69,-71,-27,-25,-45,-47,-48,-22,-21,-43,35,-108,-46,-49,-41,-44,-108,14,35,35,35,14,-108,-108,-108,-56,35,-53,14,14,14,-55,-57,-58,-59,-60,-54,-50,-108,-52,14,-51,]),'ADD':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,22,23,24,25,28,29,30,31,32,33,35,36,37,38,39,40,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,70,71,72,73,74,75,76,77,78,79,80,81,82,90,91,93,94,95,96,97,98,99,100,103,104,105,106,109,110,117,119,120,123,124,125,126,127,128,129,130,131,132,134,135,136,137,139,141,143,145,146,147,148,149,150,151,152,153,154,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[10,-100,-93,-101,-96,-7,-18,-4,-103,10,-92,10,10,-102,-3,10,-29,-11,-5,-6,-88,-90,-99,-61,-20,-37,10,-38,10,-30,-102,-103,-99,-61,10,-97,-65,-8,-2,10,-84,-87,10,-86,-85,-83,-82,-94,-95,10,10,-39,10,10,-63,-79,-62,-17,-36,-89,10,-64,-35,-32,-98,-33,-34,10,-91,-28,-40,-74,-81,-80,-73,10,-19,-10,-61,-26,-9,10,-104,10,-108,-70,-72,10,10,-42,-69,-71,-27,-25,-45,-47,-48,-22,-21,-43,10,-108,-46,-49,-41,-44,-108,10,10,10,10,10,-108,-108,-108,-56,10,-53,10,10,10,-55,-57,-58,-59,-60,-54,-50,-108,-52,10,-51,]),'EQU':([1,3,4,8,9,14,21,22,23,24,25,35,36,37,38,40,41,63,65,66,71,73,76,79,80,90,91,93,94,104,109,110,117,123,124,],[-100,-101,-96,-103,-75,-102,49,-88,-90,-99,-61,-102,-103,-99,-61,-97,49,-63,-79,-62,-89,49,-98,-76,-91,-74,-81,-80,-73,-104,-70,-72,-76,-69,-71,]),'GEQ':([1,3,4,8,9,14,21,22,23,24,25,35,36,37,38,40,41,63,65,66,71,73,76,79,80,90,91,93,94,104,109,110,117,123,124,],[-100,-101,-96,-103,-75,-102,50,-88,-90,-99,-61,-102,-103,-99,-61,-97,50,-63,-79,-62,-89,50,-98,-76,-91,-74,-81,-80,-73,-104,-70,-72,-76,-69,-71,]),'COLON':([8,14,27,88,114,116,133,],[-24,-23,68,108,-23,-24,68,]),'ENTAO':([1,3,4,9,17,22,23,24,33,35,36,37,38,40,44,63,65,66,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,104,109,110,117,123,124,144,],[-100,-101,-96,-75,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-63,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-104,-70,-72,-31,-69,-71,151,]),'OR':([1,3,4,7,17,22,23,33,34,35,36,37,38,40,42,43,46,63,65,66,70,71,74,75,76,77,78,79,80,82,90,91,93,94,104,109,110,112,117,123,124,130,153,158,159,169,],[-100,-101,-96,29,29,-88,-90,29,29,-102,-103,-99,-61,-97,29,29,29,-63,-79,-62,29,-89,-35,-32,-98,29,29,-31,-91,29,29,-81,-80,-73,-104,-70,-72,29,-31,-69,-71,29,29,29,29,29,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,23,24,27,28,29,30,31,32,33,35,36,37,38,39,40,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,65,66,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,90,91,93,94,95,96,97,98,99,100,103,104,105,106,108,109,110,113,117,119,120,123,124,125,126,127,128,129,130,131,132,134,135,136,137,139,141,143,145,146,147,148,149,150,151,152,153,154,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[25,-100,-93,-101,-96,-7,-18,-4,-24,-75,-92,38,38,38,-23,-3,25,-29,-11,-5,-6,-88,-90,-99,69,-20,-37,38,-38,38,-30,-102,-103,-99,-61,38,-97,-65,-8,-2,38,-84,-87,38,-86,-85,-83,-82,-94,-95,38,38,-39,38,38,-63,-79,-62,-17,98,-36,-89,38,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,38,-19,-10,-61,-26,-9,38,-104,38,-108,98,-70,-72,98,-31,38,-42,-69,-71,-27,-25,-45,-47,-48,-22,-21,-43,38,-108,-46,-49,-41,-44,-108,38,38,38,38,38,-108,-108,-108,-56,38,-53,38,38,38,-55,-57,-58,-59,-60,-54,-50,-108,-52,38,-51,]),'LET':([1,3,4,8,9,14,21,22,23,24,25,35,36,37,38,40,41,63,65,66,71,73,76,79,80,90,91,93,94,104,109,110,117,123,124,],[-100,-101,-96,-103,-75,-102,55,-88,-90,-99,-61,-102,-103,-99,-61,-97,55,-63,-79,-62,-89,55,-98,-76,-91,-74,-81,-80,-73,-104,-70,-72,-76,-69,-71,]),'NEQ':([1,3,4,8,9,14,21,22,23,24,25,35,36,37,38,40,41,63,65,66,71,73,76,79,80,90,91,93,94,104,109,110,117,123,124,],[-100,-101,-96,-103,-75,-102,53,-88,-90,-99,-61,-102,-103,-99,-61,-97,53,-63,-79,-62,-89,53,-98,-76,-91,-74,-81,-80,-73,-104,-70,-72,-76,-69,-71,]),'DIV':([1,3,4,8,14,22,23,24,25,35,36,37,38,40,63,65,66,71,76,80,90,91,93,94,104,109,110,123,124,],[-100,-101,-96,-103,-102,57,-90,-99,-61,-102,-103,-99,-61,-97,-63,-79,-62,57,-98,-91,-74,-81,-80,-73,-104,-70,-72,-69,-71,]),'ESCREVA':([1,3,4,8,9,14,17,22,23,24,33,35,36,37,38,40,44,63,65,66,70,71,73,74,75,76,77,78,79,80,81,82,90,91,93,94,97,98,99,100,104,106,109,110,117,119,120,123,124,125,126,127,128,129,132,135,136,137,139,141,143,145,149,150,151,152,153,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,],[-100,-101,-96,-103,-75,-102,-29,-88,-90,-99,-30,-102,-103,-99,-61,-97,-65,-63,-79,-62,-36,-89,-64,-35,-32,-98,-33,-34,-31,-91,-28,-40,-74,-81,-80,-73,-10,-61,-26,-9,-104,-108,-70,-72,-31,140,-42,-69,-71,-27,-25,-45,-47,-48,-43,-108,-46,-49,-41,-44,-108,140,140,-108,-108,-108,-56,-53,140,140,140,-55,-57,-58,-59,-60,-54,-50,-108,-52,140,-51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'chamada_funcao':([0,11,12,13,16,30,32,39,48,51,58,59,61,62,72,95,103,105,119,134,145,146,147,148,149,154,161,162,163,173,],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]),'expressao_unaria':([0,11,13,16,30,32,39,48,51,58,59,61,62,72,95,103,105,119,134,145,146,147,148,149,154,161,162,163,173,],[23,23,23,23,23,23,23,23,23,80,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'numero':([0,11,12,13,16,30,32,39,48,51,58,59,61,62,72,95,103,105,119,134,145,146,147,148,149,154,161,162,163,173,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'se':([119,145,149,161,162,163,173,],[127,127,127,127,127,127,127,]),'empty':([61,72,101,106,135,143,150,151,152,171,],[84,102,115,120,120,120,120,120,120,120,]),'var':([0,11,12,13,16,30,32,39,48,51,58,59,61,62,68,72,95,103,105,108,113,119,134,145,146,147,148,149,154,161,162,163,173,],[24,37,37,24,24,37,37,24,37,37,37,24,24,24,99,24,24,37,24,122,126,24,24,24,24,24,24,24,24,24,24,24,24,]),'operador_multiplicacao':([22,71,],[58,58,]),'expressao_simples':([0,11,13,16,30,39,48,59,61,62,72,95,105,119,134,145,146,147,148,149,154,161,162,163,173,],[21,21,41,21,21,73,21,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'cabecalho':([0,16,27,],[6,6,67,]),'operador_soma':([0,9,11,13,16,30,32,39,48,51,58,59,61,62,72,79,95,103,105,117,119,134,145,146,147,148,149,154,161,162,163,173,],[12,32,12,12,12,12,12,12,12,12,12,12,12,12,12,32,12,12,12,32,12,12,12,12,12,12,12,12,12,12,12,12,]),'lista_argumentos':([61,72,],[83,83,]),'expressao_multiplicativa':([0,11,13,16,30,32,39,48,51,59,61,62,72,95,103,105,119,134,145,146,147,148,149,154,161,162,163,173,],[22,22,22,22,22,71,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'simbolo_condicional':([7,17,33,34,42,43,46,70,77,78,82,90,112,130,153,158,159,169,],[30,48,48,30,30,48,30,48,48,30,30,30,30,30,30,30,30,30,]),'dimension':([25,38,63,98,],[65,65,93,65,]),'expressao_aditiva':([0,11,13,16,30,39,48,51,59,61,62,72,95,103,105,119,134,145,146,147,148,149,154,161,162,163,173,],[9,9,9,9,9,9,9,79,9,9,9,9,9,117,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'declaracao_funcao':([0,16,],[5,5,]),'lista_variaveis':([68,],[100,]),'repita':([119,145,149,161,162,163,173,],[136,136,136,136,136,136,136,]),'leia':([119,145,149,161,162,163,173,],[128,128,128,128,128,128,128,]),'simbolo_atribuicao':([24,],[59,]),'fator':([0,11,12,13,16,30,32,39,48,51,58,59,61,62,72,95,103,105,119,134,145,146,147,148,149,154,161,162,163,173,],[4,4,40,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'acao':([119,145,149,161,162,163,173,],[139,139,139,139,139,139,139,]),'operador_relacional':([21,41,73,],[51,51,103,]),'lista_dimensions':([25,38,98,],[63,63,63,]),'declaracao':([0,16,],[15,47,]),'lista_declaracoes':([0,],[16,]),'condicional':([0,11,13,16,30,39,48,59,61,62,72,95,105,119,134,145,146,147,148,149,154,161,162,163,173,],[17,33,43,17,70,17,77,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'atribuicao':([0,13,16,39,59,61,62,72,95,105,119,134,145,146,147,148,149,154,161,162,163,173,],[18,44,18,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'declaracao_variaveis':([0,16,119,145,149,161,162,163,173,],[19,19,141,141,141,141,141,141,141,]),'inicializacao_variaveis':([0,16,],[20,20,]),'escreva':([119,145,149,161,162,163,173,],[129,129,129,129,129,129,129,]),'corpo':([106,135,143,150,151,152,171,],[119,145,149,161,162,163,173,]),'expressao':([13,39,59,61,62,72,95,105,119,134,145,146,147,148,149,154,161,162,163,173,],[45,45,81,86,89,86,111,118,132,144,132,155,156,157,132,164,132,132,132,132,]),'lista_parametros':([61,101,],[87,87,]),'retorna':([119,145,149,161,162,163,173,],[137,137,137,137,137,137,137,]),'programa':([0,],[26,]),'indice':([25,38,98,],[66,66,66,]),'tipo':([0,16,61,101,107,119,145,149,161,162,163,173,],[27,27,88,88,88,133,133,133,133,133,133,133,]),'parametro':([61,101,107,],[85,85,121,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','myparser.py',66),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','myparser.py',77),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','myparser.py',78),
  ('lista_declaracoes -> error','lista_declaracoes',1,'p_lista_declaracoes','myparser.py',79),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','myparser.py',95),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','myparser.py',96),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','myparser.py',97),
  ('declaracao -> error','declaracao',1,'p_declaracao','myparser.py',98),
  ('declaracao_variaveis -> tipo COLON lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','myparser.py',108),
  ('declaracao_variaveis -> tipo COLON error','declaracao_variaveis',3,'p_declaracao_variaveis_error','myparser.py',114),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','myparser.py',118),
  ('declaracao_funcao_nova -> INTEIRO ID LPAR lista_parametros RPAR corpo retorna FIM','declaracao_funcao_nova',8,'p_declaracao_funcao_nova','myparser.py',124),
  ('declaracao_funcao_nova -> FLUTUANTE ID LPAR lista_parametros RPAR corpo retorna FIM','declaracao_funcao_nova',8,'p_declaracao_funcao_nova','myparser.py',125),
  ('declaracao_funcao_nova -> ID LPAR lista_parametros RPAR corpo FIM','declaracao_funcao_nova',6,'p_declaracao_funcao_nova','myparser.py',126),
  ('declaracao_funcao_nova -> INTEIRO ID LPAR lista_parametros RPAR corpo error FIM','declaracao_funcao_nova',8,'p_declaracao_funcao_nova_error','myparser.py',145),
  ('declaracao_funcao_nova -> FLUTUANTE ID LPAR lista_parametros RPAR corpo error FIM','declaracao_funcao_nova',8,'p_declaracao_funcao_nova_error','myparser.py',146),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','myparser.py',152),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','myparser.py',153),
  ('declaracao_funcao -> tipo cabecalho error','declaracao_funcao',3,'p_declaracao_funcao_error','myparser.py',165),
  ('declaracao_funcao -> cabecalho error','declaracao_funcao',2,'p_declaracao_funcao_error','myparser.py',166),
  ('cabecalho -> ID LPAR lista_parametros RPAR corpo FIM','cabecalho',6,'p_cabecalho','myparser.py',171),
  ('cabecalho -> ID LPAR lista_parametros RPAR corpo error','cabecalho',6,'p_cabecalho_error','myparser.py',184),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','myparser.py',188),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','myparser.py',189),
  ('lista_variaveis -> lista_variaveis COM var','lista_variaveis',3,'p_lista_variaveis','myparser.py',194),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','myparser.py',195),
  ('lista_variaveis -> lista_variaveis COM error','lista_variaveis',3,'p_lista_variaveis_error','myparser.py',206),
  ('atribuicao -> var simbolo_atribuicao expressao','atribuicao',3,'p_atribuicao','myparser.py',211),
  ('atribuicao -> condicional','atribuicao',1,'p_atribuicao','myparser.py',212),
  ('atribuicao -> NOT condicional','atribuicao',2,'p_atribuicao','myparser.py',213),
  ('condicional -> expressao_simples operador_relacional expressao_aditiva','condicional',3,'p_condicional','myparser.py',230),
  ('condicional -> LPAR condicional RPAR','condicional',3,'p_condicional','myparser.py',231),
  ('condicional -> condicional simbolo_condicional condicional','condicional',3,'p_condicional','myparser.py',232),
  ('condicional -> condicional simbolo_condicional error','condicional',3,'p_condicional','myparser.py',233),
  ('condicional -> LPAR error RPAR','condicional',3,'p_condicional','myparser.py',234),
  ('condicional -> error simbolo_condicional condicional','condicional',3,'p_condicional','myparser.py',235),
  ('simbolo_condicional -> OR','simbolo_condicional',1,'p_simbolo_condicional','myparser.py',253),
  ('simbolo_condicional -> AND','simbolo_condicional',1,'p_simbolo_condicional','myparser.py',254),
  ('simbolo_atribuicao -> ASS','simbolo_atribuicao',1,'p_simbolo_atribuicao','myparser.py',259),
  ('atribuicao -> var simbolo_atribuicao error','atribuicao',3,'p_atribuicao_error','myparser.py',263),
  ('corpo -> corpo acao','corpo',2,'p_corpo','myparser.py',270),
  ('corpo -> empty','corpo',1,'p_corpo','myparser.py',271),
  ('acao -> expressao','acao',1,'p_acao','myparser.py',289),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','myparser.py',290),
  ('acao -> se','acao',1,'p_acao','myparser.py',291),
  ('acao -> repita','acao',1,'p_acao','myparser.py',292),
  ('acao -> leia','acao',1,'p_acao','myparser.py',293),
  ('acao -> escreva','acao',1,'p_acao','myparser.py',294),
  ('acao -> retorna','acao',1,'p_acao','myparser.py',295),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','myparser.py',303),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','myparser.py',304),
  ('se -> SE expressao error corpo FIM','se',5,'p_se_error','myparser.py',319),
  ('se -> error SENAO corpo FIM','se',4,'p_se_error','myparser.py',320),
  ('se -> SE expressao SENAO corpo error','se',5,'p_se_error','myparser.py',321),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','myparser.py',332),
  ('repita -> REPITA corpo error','repita',3,'p_repita_error','myparser.py',338),
  ('leia -> LEIA LPAR expressao RPAR','leia',4,'p_leia','myparser.py',342),
  ('escreva -> ESCREVA LPAR expressao RPAR','escreva',4,'p_escreva','myparser.py',347),
  ('retorna -> RETORNA LPAR expressao RPAR','retorna',4,'p_retorna','myparser.py',352),
  ('retorna -> RETORNA LPAR error RPAR','retorna',4,'p_retorna_error','myparser.py',357),
  ('var -> ID','var',1,'p_var','myparser.py',366),
  ('var -> ID indice','var',2,'p_var','myparser.py',367),
  ('var -> ID lista_dimensions','var',2,'p_var','myparser.py',368),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','myparser.py',379),
  ('expressao -> atribuicao','expressao',1,'p_expressao','myparser.py',380),
  ('lista_parametros -> lista_parametros COM parametro','lista_parametros',3,'p_lista_parametros','myparser.py',388),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','myparser.py',389),
  ('lista_parametros -> empty','lista_parametros',1,'p_lista_parametros','myparser.py',390),
  ('indice -> indice LBR expressao RBR','indice',4,'p_indice','myparser.py',405),
  ('indice -> LBR expressao RBR','indice',3,'p_indice','myparser.py',406),
  ('indice -> indice LBR error RBR','indice',4,'p_indice_error','myparser.py',419),
  ('indice -> LBR error RBR','indice',3,'p_indice_error','myparser.py',420),
  ('indice -> error RBR','indice',2,'p_indice_error','myparser.py',421),
  ('indice -> LBR error','indice',2,'p_indice_error','myparser.py',422),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','myparser.py',432),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','myparser.py',433),
  ('parametro -> tipo COLON var','parametro',3,'p_parametro','myparser.py',447),
  ('parametro -> parametro','parametro',1,'p_parametro','myparser.py',448),
  ('lista_dimensions -> dimension','lista_dimensions',1,'p_lista_dimensions','myparser.py',460),
  ('lista_dimensions -> lista_dimensions dimension','lista_dimensions',2,'p_lista_dimensions','myparser.py',461),
  ('dimension -> LBR RBR','dimension',2,'p_dimension','myparser.py',472),
  ('operador_relacional -> LET','operador_relacional',1,'p_operador_relacional','myparser.py',478),
  ('operador_relacional -> GRT','operador_relacional',1,'p_operador_relacional','myparser.py',479),
  ('operador_relacional -> EQU','operador_relacional',1,'p_operador_relacional','myparser.py',480),
  ('operador_relacional -> NEQ','operador_relacional',1,'p_operador_relacional','myparser.py',481),
  ('operador_relacional -> LEQ','operador_relacional',1,'p_operador_relacional','myparser.py',482),
  ('operador_relacional -> GEQ','operador_relacional',1,'p_operador_relacional','myparser.py',483),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','myparser.py',490),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','myparser.py',491),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','myparser.py',505),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','myparser.py',506),
  ('operador_soma -> ADD','operador_soma',1,'p_operador_soma','myparser.py',520),
  ('operador_soma -> SUB','operador_soma',1,'p_operador_soma','myparser.py',521),
  ('operador_multiplicacao -> TIMES','operador_multiplicacao',1,'p_operador_multiplicacao','myparser.py',528),
  ('operador_multiplicacao -> DIV','operador_multiplicacao',1,'p_operador_multiplicacao','myparser.py',529),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','myparser.py',536),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','myparser.py',537),
  ('fator -> LPAR expressao RPAR','fator',3,'p_fator','myparser.py',550),
  ('fator -> var','fator',1,'p_fator','myparser.py',551),
  ('fator -> chamada_funcao','fator',1,'p_fator','myparser.py',552),
  ('fator -> numero','fator',1,'p_fator','myparser.py',553),
  ('numero -> INTEIRO','numero',1,'p_numero','myparser.py',565),
  ('numero -> FLUTUANTE','numero',1,'p_numero','myparser.py',566),
  ('chamada_funcao -> ID LPAR lista_argumentos RPAR','chamada_funcao',4,'p_chamada_funcao','myparser.py',572),
  ('lista_argumentos -> lista_argumentos COM expressao','lista_argumentos',3,'p_lista_argumentos','myparser.py',581),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','myparser.py',582),
  ('lista_argumentos -> empty','lista_argumentos',1,'p_lista_argumentos','myparser.py',583),
  ('empty -> <empty>','empty',0,'p_empty','myparser.py',595),
]
