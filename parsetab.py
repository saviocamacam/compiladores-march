
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASS COLON LPAR RPAR ADD SUB TIMES DIV LEQ GEQ EQU NEQ LET GRT LBR RBR COM ID NOT AND OR SE ENTAO SENAO FIM REPITA FLUTUANTE RETORNA ATE LEIA ESCREVE INTEIROprograma : lista_declaracoes\n        lista_declaracoes : lista_declaracoes declaracao\n            | declaracao\n            | error\n        \n        declaracao : declaracao_variaveis\n            | inicializacao_variaveis\n            | declaracao_funcao\n            | error\n        declaracao_variaveis : tipo COLON lista_variaveisdeclaracao_variaveis : tipo COLON errorinicializacao_variaveis : atribuicao\n        declaracao_funcao : tipo cabecalho\n            | cabecalho\n        \n        declaracao_funcao : tipo cabecalho error\n            | cabecalho error\n        tipo : INTEIRO \n            | FLUTUANTE\n        lista_variaveis : lista_variaveis COM var\n            | var\n        lista_variaveis : lista_variaveis COM error\n        atribuicao : var simbolo_atribuicao expressao\n            | condicional\n            | NOT condicional\n        \n        condicional : expressao_simples operador_relacional expressao_aditiva\n            | LPAR condicional RPAR\n            | condicional simbolo_condicional condicional\n            | condicional simbolo_condicional error\n            | LPAR error RPAR\n            | error simbolo_condicional condicional\n        \n        simbolo_condicional : OR\n            | AND\n        simbolo_atribuicao : ASSatribuicao : var simbolo_atribuicao errorcabecalho : ID LPAR lista_parametros RPAR corpo FIMcabecalho : ID LPAR lista_parametros RPAR corpo error\n        corpo : corpo acao\n            | empty\n        \n        acao : expressao\n            | declaracao_variaveis\n            | se\n            | repita\n            | leia\n            | escreve\n            | retorna\n        \n        se : SE expressao ENTAO corpo FIM\n            | SE expressao ENTAO corpo SENAO corpo FIM\n        \n        se : SE expressao error corpo FIM\n            | error SENAO corpo FIM\n        repita : REPITA corpo ATE expressaorepita : REPITA corpo errorleia : LEIA LPAR ID RPARescreve : ESCREVE LPAR expressao RPARretorna :  RETORNA LPAR expressao RPAR\n        var : ID\n            | ID indice\n        \n        expressao : expressao_simples\n            | atribuicao\n        \n        lista_parametros : lista_parametros COM parametro\n            | parametro\n            | empty\n        \n        indice : indice LBR expressao RBR\n            | LBR expressao RBR\n        \n        indice : indice LBR error RBR\n            | LBR error RBR\n            | error RBR\n            | LBR error\n        \n        expressao_simples : expressao_aditiva\n            | expressao_simples operador_relacional expressao_aditiva\n        \n        parametro : tipo COLON ID\n            | parametro dimension\n        dimension : LBR RBR\n        operador_relacional : LET\n            | GRT\n            | EQU\n            | NEQ\n            | LEQ\n            | GEQ\n        \n        expressao_aditiva : expressao_multiplicativa\n            | expressao_aditiva operador_soma expressao_multiplicativa\n        \n        expressao_multiplicativa : expressao_unaria\n            | expressao_multiplicativa operador_multiplicacao expressao_unaria\n        \n        operador_soma : ADD\n            | SUB\n        \n        operador_multiplicacao : TIMES\n            | DIV\n        \n        expressao_unaria : fator\n            | operador_soma fator\n        \n        fator : LPAR expressao RPAR\n            | var\n            | chamada_funcao\n            | numero\n        \n        numero : INTEIRO\n            | FLUTUANTE\n        chamada_funcao : ID LPAR lista_argumentos RPAR\n        lista_argumentos : lista_argumentos COM expressao\n            | expressao\n            | empty\n        empty :'
    
_lr_action_items = {'error':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,22,23,24,25,28,29,30,31,32,33,34,36,37,38,39,40,42,43,44,45,46,48,49,54,66,67,68,69,70,71,72,73,75,76,77,78,79,80,87,88,90,91,92,93,94,95,96,97,103,105,106,112,113,114,115,116,117,118,123,124,125,126,127,128,129,130,131,132,133,134,136,137,141,142,143,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164,165,166,167,],[4,29,-3,-4,-5,-6,-7,-11,36,-92,-93,-89,-22,41,47,51,-67,-78,-80,-86,-90,-91,-2,-8,41,-30,-31,70,73,-15,76,-32,79,-23,-89,47,-92,-93,41,-55,90,-57,-87,41,-29,-9,-10,-19,47,-14,-21,-33,-56,-26,-27,41,-65,111,-66,-25,-28,-88,-24,-79,-81,115,-98,-94,41,-62,-64,-18,-20,-24,126,-37,-61,-63,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,41,-98,-98,149,151,41,41,155,-98,-98,41,-50,-48,155,155,-49,-51,-52,-53,-45,-98,-47,155,-46,]),'INTEIRO':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,36,37,38,39,40,42,43,44,45,46,48,49,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,88,90,91,92,93,94,95,96,101,103,104,105,106,112,113,114,115,116,117,118,123,124,125,126,127,128,129,130,131,132,133,134,136,137,141,143,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164,165,166,167,],[11,11,-3,-4,-5,-6,-7,-11,-13,-92,-93,-89,-22,44,44,-67,-78,44,-80,-86,-90,-91,-82,-83,-2,-8,44,-30,-31,-12,-15,44,-32,44,-23,-89,-54,-92,-93,11,-55,44,-57,44,-72,-73,-74,-75,-76,-77,44,44,-84,-85,-87,44,-29,-9,-10,-19,-54,-14,99,-21,-33,-56,-26,-27,44,-65,44,-66,-25,-28,-88,-24,-79,-81,44,-98,99,-94,44,-62,-64,-18,-20,-24,11,-37,-61,-63,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,44,-98,-98,11,44,44,11,-98,-98,44,-50,-48,11,11,-49,-51,-52,-53,-45,-98,-47,11,-46,]),'FLUTUANTE':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,36,37,38,39,40,42,43,44,45,46,48,49,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,87,88,90,91,92,93,94,95,96,101,103,104,105,106,112,113,114,115,116,117,118,123,124,125,126,127,128,129,130,131,132,133,134,136,137,141,143,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164,165,166,167,],[12,12,-3,-4,-5,-6,-7,-11,-13,-92,-93,-89,-22,45,45,-67,-78,45,-80,-86,-90,-91,-82,-83,-2,-8,45,-30,-31,-12,-15,45,-32,45,-23,-89,-54,-92,-93,12,-55,45,-57,45,-72,-73,-74,-75,-76,-77,45,45,-84,-85,-87,45,-29,-9,-10,-19,-54,-14,100,-21,-33,-56,-26,-27,45,-65,45,-66,-25,-28,-88,-24,-79,-81,45,-98,100,-94,45,-62,-64,-18,-20,-24,12,-37,-61,-63,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,45,-98,-98,12,45,45,12,-98,-98,45,-50,-48,12,12,-49,-51,-52,-53,-45,-98,-47,12,-46,]),'NOT':([0,2,3,4,5,6,7,9,10,11,12,13,14,17,19,20,22,23,24,25,28,29,34,36,37,38,40,42,43,44,45,46,48,49,54,66,67,68,69,70,71,72,73,75,76,77,78,79,80,87,88,90,91,92,93,94,95,96,103,105,106,112,113,114,115,116,117,118,123,124,125,126,127,128,129,130,131,132,133,134,136,137,141,143,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164,165,166,167,],[15,15,-3,-4,-5,-6,-7,-11,-13,-92,-93,-89,-22,15,-67,-78,-80,-86,-90,-91,-2,-8,-12,-15,15,-32,-23,-89,-54,-92,-93,15,-55,15,-57,-87,15,-29,-9,-10,-19,-54,-14,-21,-33,-56,-26,-27,15,-65,15,-66,-25,-28,-88,-24,-79,-81,-98,-94,15,-62,-64,-18,-20,-24,15,-37,-61,-63,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,15,-98,-98,15,15,15,15,-98,-98,15,-50,-48,15,15,-49,-51,-52,-53,-45,-98,-47,15,-46,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,42,43,44,45,46,48,49,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,79,80,87,88,90,91,92,93,94,95,96,97,101,103,105,106,109,112,113,114,115,116,117,118,123,124,125,126,127,128,129,130,131,132,133,134,136,137,141,143,144,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164,165,166,167,],[16,16,-3,-4,-5,-6,-7,35,-11,-13,-16,-17,-89,-22,43,43,-67,-78,43,-80,-86,-90,-91,-82,-83,-2,-8,43,-30,-31,72,-12,-15,43,-32,43,-23,-89,-54,-92,-93,43,-55,43,-57,43,-72,-73,-74,-75,-76,-77,43,43,-84,-85,-87,43,-29,-9,-10,-19,-54,-14,-21,-33,-56,-26,-27,43,-65,43,-66,-25,-28,-88,-24,-79,-81,72,43,-98,-94,43,122,-62,-64,-18,-20,-24,43,-37,-61,-63,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,43,-98,-98,43,152,43,43,43,-98,-98,43,-50,-48,43,43,-49,-51,-52,-53,-45,-98,-47,43,-46,]),'LPAR':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,38,39,40,42,43,44,45,46,48,49,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,79,80,87,88,90,91,92,93,94,95,96,101,103,105,106,112,113,114,115,116,117,118,123,124,125,126,127,128,129,130,131,132,133,134,136,137,138,139,140,141,143,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164,165,166,167,],[17,17,-3,-4,-5,-6,-7,-11,-13,-92,-93,-89,-22,17,46,17,-67,-78,67,-80,-86,-90,-91,-82,-83,-2,-8,17,-30,-31,-12,74,-15,17,-32,17,-23,-89,80,-92,-93,17,-55,17,-57,67,-72,-73,-74,-75,-76,-77,67,67,-84,-85,-87,17,-29,-9,-10,-19,-54,-14,-21,-33,-56,-26,-27,17,-65,17,-66,-25,-28,-88,-24,-79,-81,67,-98,-94,17,-62,-64,-18,-20,-24,17,-37,-61,-63,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,17,-98,144,145,146,-98,17,17,17,17,-98,-98,17,-50,-48,17,17,-49,-51,-52,-53,-45,-98,-47,17,-46,]),'ADD':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,22,23,24,25,26,27,28,29,30,31,32,34,36,37,38,39,40,42,43,44,45,46,48,49,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,79,80,87,88,90,91,92,93,94,95,96,101,103,105,106,112,113,114,115,116,117,118,123,124,125,126,127,128,129,130,131,132,133,134,136,137,141,143,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164,165,166,167,],[26,26,-3,-4,-5,-6,-7,-11,-13,-92,-93,-89,-22,26,-54,26,26,-78,-80,-86,-90,-91,-82,-83,-2,-8,26,-30,-31,-12,-15,26,-32,26,-23,-89,-54,-92,-93,26,-55,26,-57,26,-72,-73,-74,-75,-76,-77,26,26,-84,-85,-87,26,-29,-9,-10,-19,-54,-14,-21,-33,-56,-26,-27,26,-65,26,-66,-25,-28,-88,26,-79,-81,26,-98,-94,26,-62,-64,-18,-20,26,26,-37,-61,-63,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,26,-98,-98,26,26,26,26,-98,-98,26,-50,-48,26,26,-49,-51,-52,-53,-45,-98,-47,26,-46,]),'SUB':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,19,20,22,23,24,25,26,27,28,29,30,31,32,34,36,37,38,39,40,42,43,44,45,46,48,49,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,79,80,87,88,90,91,92,93,94,95,96,101,103,105,106,112,113,114,115,116,117,118,123,124,125,126,127,128,129,130,131,132,133,134,136,137,141,143,145,146,147,148,149,150,151,156,157,158,159,160,161,162,163,164,165,166,167,],[27,27,-3,-4,-5,-6,-7,-11,-13,-92,-93,-89,-22,27,-54,27,27,-78,-80,-86,-90,-91,-82,-83,-2,-8,27,-30,-31,-12,-15,27,-32,27,-23,-89,-54,-92,-93,27,-55,27,-57,27,-72,-73,-74,-75,-76,-77,27,27,-84,-85,-87,27,-29,-9,-10,-19,-54,-14,-21,-33,-56,-26,-27,27,-65,27,-66,-25,-28,-88,27,-79,-81,27,-98,-94,27,-62,-64,-18,-20,27,27,-37,-61,-63,-34,-35,-36,-38,-39,-40,-41,-42,-43,-44,27,-98,-98,27,27,27,27,-98,-98,27,-50,-48,27,27,-49,-51,-52,-53,-45,-98,-47,27,-46,]),'$end':([1,2,3,4,5,6,7,9,10,13,14,19,20,22,23,24,25,28,29,34,36,40,42,43,44,45,48,54,66,68,69,70,71,72,73,75,76,77,78,79,87,90,91,92,93,94,95,96,105,112,113,114,115,116,123,124,125,126,],[0,-1,-3,-4,-5,-6,-7,-11,-13,-89,-22,-67,-78,-80,-86,-90,-91,-2,-8,-12,-15,-23,-89,-54,-92,-93,-55,-57,-87,-29,-9,-10,-19,-54,-14,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-94,-62,-64,-18,-20,-24,-61,-63,-34,-35,]),'OR':([4,14,20,22,23,24,25,29,40,41,42,43,44,45,48,50,51,66,68,76,78,79,87,90,91,92,93,94,95,96,105,111,112,113,116,123,124,126,151,155,],[31,31,-78,-80,-86,-90,-91,31,31,31,-89,-54,-92,-93,-55,31,31,-87,31,31,31,31,-65,31,-25,-28,-88,-24,-79,-81,-94,31,-62,-64,-24,-61,-63,31,31,31,]),'AND':([4,14,20,22,23,24,25,29,40,41,42,43,44,45,48,50,51,66,68,76,78,79,87,90,91,92,93,94,95,96,105,111,112,113,116,123,124,126,151,155,],[32,32,-78,-80,-86,-90,-91,32,32,32,-89,-54,-92,-93,-55,32,32,-87,32,32,32,32,-65,32,-25,-28,-88,-24,-79,-81,-94,32,-62,-64,-24,-61,-63,32,32,32,]),'COLON':([8,11,12,86,99,100,135,],[33,-16,-17,109,-16,-17,33,]),'TIMES':([11,12,13,16,20,22,23,24,25,42,43,44,45,48,66,87,90,93,95,96,105,112,113,123,124,],[-92,-93,-89,-54,64,-80,-86,-90,-91,-89,-54,-92,-93,-55,-87,-65,-66,-88,64,-81,-94,-62,-64,-61,-63,]),'DIV':([11,12,13,16,20,22,23,24,25,42,43,44,45,48,66,87,90,93,95,96,105,112,113,123,124,],[-92,-93,-89,-54,65,-80,-86,-90,-91,-89,-54,-92,-93,-55,-87,-65,-66,-88,65,-81,-94,-62,-64,-61,-63,]),'LET':([11,12,13,16,18,19,20,22,23,24,25,42,43,44,45,48,53,66,77,87,90,93,94,95,96,105,112,113,116,123,124,],[-92,-93,-89,-54,56,-67,-78,-80,-86,-90,-91,-89,-54,-92,-93,-55,56,-87,56,-65,-66,-88,-68,-79,-81,-94,-62,-64,-68,-61,-63,]),'GRT':([11,12,13,16,18,19,20,22,23,24,25,42,43,44,45,48,53,66,77,87,90,93,94,95,96,105,112,113,116,123,124,],[-92,-93,-89,-54,57,-67,-78,-80,-86,-90,-91,-89,-54,-92,-93,-55,57,-87,57,-65,-66,-88,-68,-79,-81,-94,-62,-64,-68,-61,-63,]),'EQU':([11,12,13,16,18,19,20,22,23,24,25,42,43,44,45,48,53,66,77,87,90,93,94,95,96,105,112,113,116,123,124,],[-92,-93,-89,-54,58,-67,-78,-80,-86,-90,-91,-89,-54,-92,-93,-55,58,-87,58,-65,-66,-88,-68,-79,-81,-94,-62,-64,-68,-61,-63,]),'NEQ':([11,12,13,16,18,19,20,22,23,24,25,42,43,44,45,48,53,66,77,87,90,93,94,95,96,105,112,113,116,123,124,],[-92,-93,-89,-54,59,-67,-78,-80,-86,-90,-91,-89,-54,-92,-93,-55,59,-87,59,-65,-66,-88,-68,-79,-81,-94,-62,-64,-68,-61,-63,]),'LEQ':([11,12,13,16,18,19,20,22,23,24,25,42,43,44,45,48,53,66,77,87,90,93,94,95,96,105,112,113,116,123,124,],[-92,-93,-89,-54,60,-67,-78,-80,-86,-90,-91,-89,-54,-92,-93,-55,60,-87,60,-65,-66,-88,-68,-79,-81,-94,-62,-64,-68,-61,-63,]),'GEQ':([11,12,13,16,18,19,20,22,23,24,25,42,43,44,45,48,53,66,77,87,90,93,94,95,96,105,112,113,116,123,124,],[-92,-93,-89,-54,61,-67,-78,-80,-86,-90,-91,-89,-54,-92,-93,-55,61,-87,61,-65,-66,-88,-68,-79,-81,-94,-62,-64,-68,-61,-63,]),'RPAR':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,46,48,50,51,52,53,54,66,68,74,75,76,77,78,79,80,81,82,83,84,85,87,90,91,92,93,94,95,96,98,102,105,107,112,113,116,119,120,121,122,123,124,152,153,154,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-98,-55,91,92,93,-56,-57,-87,-29,-98,-21,-33,-56,-26,-27,-98,103,105,-59,-60,-96,-65,-66,-25,-28,-88,-24,-79,-81,-60,-97,-94,-70,-62,-64,-24,-58,-95,-71,-69,-61,-63,160,161,162,]),'COM':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,46,48,54,66,68,69,71,72,74,75,76,77,78,79,80,81,82,83,84,85,87,90,91,92,93,94,95,96,98,102,105,107,112,113,114,115,116,119,120,121,122,123,124,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-98,-55,-57,-87,-29,97,-19,-54,-98,-21,-33,-56,-26,-27,-98,104,106,-59,-60,-96,-65,-66,-25,-28,-88,-24,-79,-81,-60,-97,-94,-70,-62,-64,-18,-20,-24,-58,-95,-71,-69,-61,-63,]),'FIM':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,48,54,66,68,69,70,71,72,75,76,77,78,79,87,90,91,92,93,94,95,96,103,105,112,113,114,115,116,117,118,123,124,127,128,129,130,131,132,133,134,141,147,148,149,151,156,157,158,159,160,161,162,163,164,165,166,167,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-55,-57,-87,-29,-9,-10,-19,-54,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-98,-94,-62,-64,-18,-20,-24,125,-37,-61,-63,-36,-38,-39,-40,-41,-42,-43,-44,-98,156,-98,-98,-50,-48,163,165,-49,-51,-52,-53,-45,-98,-47,167,-46,]),'SE':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,48,54,66,68,69,70,71,72,75,76,77,78,79,87,90,91,92,93,94,95,96,103,105,112,113,114,115,116,117,118,123,124,127,128,129,130,131,132,133,134,137,141,143,147,148,149,151,156,157,158,159,160,161,162,163,164,165,166,167,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-55,-57,-87,-29,-9,-10,-19,-54,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-98,-94,-62,-64,-18,-20,-24,136,-37,-61,-63,-36,-38,-39,-40,-41,-42,-43,-44,-98,-98,136,136,-98,-98,-50,-48,136,136,-49,-51,-52,-53,-45,-98,-47,136,-46,]),'REPITA':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,48,54,66,68,69,70,71,72,75,76,77,78,79,87,90,91,92,93,94,95,96,103,105,112,113,114,115,116,117,118,123,124,127,128,129,130,131,132,133,134,137,141,143,147,148,149,151,156,157,158,159,160,161,162,163,164,165,166,167,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-55,-57,-87,-29,-9,-10,-19,-54,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-98,-94,-62,-64,-18,-20,-24,137,-37,-61,-63,-36,-38,-39,-40,-41,-42,-43,-44,-98,-98,137,137,-98,-98,-50,-48,137,137,-49,-51,-52,-53,-45,-98,-47,137,-46,]),'LEIA':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,48,54,66,68,69,70,71,72,75,76,77,78,79,87,90,91,92,93,94,95,96,103,105,112,113,114,115,116,117,118,123,124,127,128,129,130,131,132,133,134,137,141,143,147,148,149,151,156,157,158,159,160,161,162,163,164,165,166,167,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-55,-57,-87,-29,-9,-10,-19,-54,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-98,-94,-62,-64,-18,-20,-24,138,-37,-61,-63,-36,-38,-39,-40,-41,-42,-43,-44,-98,-98,138,138,-98,-98,-50,-48,138,138,-49,-51,-52,-53,-45,-98,-47,138,-46,]),'ESCREVE':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,48,54,66,68,69,70,71,72,75,76,77,78,79,87,90,91,92,93,94,95,96,103,105,112,113,114,115,116,117,118,123,124,127,128,129,130,131,132,133,134,137,141,143,147,148,149,151,156,157,158,159,160,161,162,163,164,165,166,167,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-55,-57,-87,-29,-9,-10,-19,-54,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-98,-94,-62,-64,-18,-20,-24,139,-37,-61,-63,-36,-38,-39,-40,-41,-42,-43,-44,-98,-98,139,139,-98,-98,-50,-48,139,139,-49,-51,-52,-53,-45,-98,-47,139,-46,]),'RETORNA':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,48,54,66,68,69,70,71,72,75,76,77,78,79,87,90,91,92,93,94,95,96,103,105,112,113,114,115,116,117,118,123,124,127,128,129,130,131,132,133,134,137,141,143,147,148,149,151,156,157,158,159,160,161,162,163,164,165,166,167,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-55,-57,-87,-29,-9,-10,-19,-54,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-98,-94,-62,-64,-18,-20,-24,140,-37,-61,-63,-36,-38,-39,-40,-41,-42,-43,-44,-98,-98,140,140,-98,-98,-50,-48,140,140,-49,-51,-52,-53,-45,-98,-47,140,-46,]),'ATE':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,48,54,66,68,69,70,71,72,75,76,77,78,79,87,90,91,92,93,94,95,96,105,112,113,114,115,116,118,123,124,127,128,129,130,131,132,133,134,137,143,151,156,159,160,161,162,163,165,167,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-55,-57,-87,-29,-9,-10,-19,-54,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-94,-62,-64,-18,-20,-24,-37,-61,-63,-36,-38,-39,-40,-41,-42,-43,-44,-98,150,-50,-48,-49,-51,-52,-53,-45,-47,-46,]),'SENAO':([11,12,13,14,19,20,22,23,24,25,40,42,43,44,45,48,54,66,68,69,70,71,72,75,76,77,78,79,87,90,91,92,93,94,95,96,105,112,113,114,115,116,118,123,124,126,127,128,129,130,131,132,133,134,148,151,155,156,157,159,160,161,162,163,165,167,],[-92,-93,-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-55,-57,-87,-29,-9,-10,-19,-54,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-94,-62,-64,-18,-20,-24,-37,-61,-63,141,-36,-38,-39,-40,-41,-42,-43,-44,-98,141,141,-48,164,-49,-51,-52,-53,-45,-47,-46,]),'RBR':([13,14,19,20,22,23,24,25,40,42,43,44,45,47,48,54,66,68,75,76,77,78,79,87,89,90,91,92,93,94,95,96,105,108,110,111,112,113,116,123,124,],[-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,87,-55,-57,-87,-29,-21,-33,-56,-26,-27,-65,112,113,-25,-28,-88,-24,-79,-81,-94,121,123,124,-62,-64,-24,-61,-63,]),'ENTAO':([13,14,19,20,22,23,24,25,40,42,43,44,45,48,54,66,68,75,76,77,78,79,87,90,91,92,93,94,95,96,105,112,113,116,123,124,142,],[-89,-22,-67,-78,-80,-86,-90,-91,-23,-89,-54,-92,-93,-55,-57,-87,-29,-21,-33,-56,-26,-27,-65,-66,-25,-28,-88,-24,-79,-81,-94,-62,-64,-24,-61,-63,148,]),'ASS':([13,16,43,48,87,90,112,113,123,124,],[38,-54,-54,-55,-65,-66,-62,-64,-61,-63,]),'LBR':([16,43,48,72,83,87,90,107,112,113,119,121,122,123,124,],[49,49,88,49,108,-65,-66,-70,-62,-64,108,-71,-69,-61,-63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'lista_declaracoes':([0,],[2,]),'declaracao':([0,2,],[3,28,]),'declaracao_variaveis':([0,2,117,143,147,157,158,166,],[5,5,129,129,129,129,129,129,]),'inicializacao_variaveis':([0,2,],[6,6,]),'declaracao_funcao':([0,2,],[7,7,]),'tipo':([0,2,46,74,104,117,143,147,157,158,166,],[8,8,86,86,86,135,135,135,135,135,135,]),'atribuicao':([0,2,17,37,46,49,67,80,88,106,117,136,143,145,146,147,150,157,158,166,],[9,9,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'cabecalho':([0,2,8,],[10,10,34,]),'var':([0,2,15,17,21,30,33,37,39,46,49,55,62,63,67,80,88,97,101,106,117,136,143,145,146,147,150,157,158,166,],[13,13,42,13,42,42,71,13,42,13,13,42,42,42,13,13,13,114,42,13,13,13,13,13,13,13,13,13,13,13,]),'condicional':([0,2,15,17,30,37,39,46,49,67,80,88,106,117,136,143,145,146,147,150,157,158,166,],[14,14,40,50,68,14,78,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'expressao_simples':([0,2,15,17,30,37,39,46,49,67,80,88,106,117,136,143,145,146,147,150,157,158,166,],[18,18,18,53,18,77,18,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'expressao_aditiva':([0,2,15,17,30,37,39,46,49,55,67,80,88,101,106,117,136,143,145,146,147,150,157,158,166,],[19,19,19,19,19,19,19,19,19,94,19,19,19,116,19,19,19,19,19,19,19,19,19,19,19,]),'expressao_multiplicativa':([0,2,15,17,30,37,39,46,49,55,62,67,80,88,101,106,117,136,143,145,146,147,150,157,158,166,],[20,20,20,20,20,20,20,20,20,20,95,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'operador_soma':([0,2,15,17,19,30,37,39,46,49,55,62,63,67,80,88,94,101,106,116,117,136,143,145,146,147,150,157,158,166,],[21,21,21,21,62,21,21,21,21,21,21,21,21,21,21,21,62,21,21,62,21,21,21,21,21,21,21,21,21,21,]),'expressao_unaria':([0,2,15,17,30,37,39,46,49,55,62,63,67,80,88,101,106,117,136,143,145,146,147,150,157,158,166,],[22,22,22,22,22,22,22,22,22,22,22,96,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'fator':([0,2,15,17,21,30,37,39,46,49,55,62,63,67,80,88,101,106,117,136,143,145,146,147,150,157,158,166,],[23,23,23,23,66,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'chamada_funcao':([0,2,15,17,21,30,37,39,46,49,55,62,63,67,80,88,101,106,117,136,143,145,146,147,150,157,158,166,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'numero':([0,2,15,17,21,30,37,39,46,49,55,62,63,67,80,88,101,106,117,136,143,145,146,147,150,157,158,166,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'simbolo_condicional':([4,14,29,40,41,50,51,68,76,78,79,90,111,126,151,155,],[30,39,30,39,30,39,30,39,30,39,30,30,30,30,30,30,]),'simbolo_atribuicao':([13,],[37,]),'indice':([16,43,72,],[48,48,48,]),'expressao':([17,37,46,49,67,80,88,106,117,136,143,145,146,147,150,157,158,166,],[52,75,85,89,52,85,110,120,128,142,128,153,154,128,159,128,128,128,]),'operador_relacional':([18,53,77,],[55,55,101,]),'operador_multiplicacao':([20,95,],[63,63,]),'lista_variaveis':([33,],[69,]),'lista_parametros':([46,74,],[81,81,]),'lista_argumentos':([46,80,],[82,82,]),'parametro':([46,74,104,],[83,83,119,]),'empty':([46,74,80,103,137,141,148,149,164,],[84,98,102,118,118,118,118,118,118,]),'dimension':([83,119,],[107,107,]),'corpo':([103,137,141,148,149,164,],[117,143,147,157,158,166,]),'acao':([117,143,147,157,158,166,],[127,127,127,127,127,127,]),'se':([117,143,147,157,158,166,],[130,130,130,130,130,130,]),'repita':([117,143,147,157,158,166,],[131,131,131,131,131,131,]),'leia':([117,143,147,157,158,166,],[132,132,132,132,132,132,]),'escreve':([117,143,147,157,158,166,],[133,133,133,133,133,133,]),'retorna':([117,143,147,157,158,166,],[134,134,134,134,134,134,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','parser.py',39),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','parser.py',44),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','parser.py',45),
  ('lista_declaracoes -> error','lista_declaracoes',1,'p_lista_declaracoes','parser.py',46),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','parser.py',58),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','parser.py',59),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','parser.py',60),
  ('declaracao -> error','declaracao',1,'p_declaracao','parser.py',61),
  ('declaracao_variaveis -> tipo COLON lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','parser.py',69),
  ('declaracao_variaveis -> tipo COLON error','declaracao_variaveis',3,'p_declaracao_variaveis_error','parser.py',74),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','parser.py',78),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','parser.py',83),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','parser.py',84),
  ('declaracao_funcao -> tipo cabecalho error','declaracao_funcao',3,'p_declaracao_funcao_error','parser.py',93),
  ('declaracao_funcao -> cabecalho error','declaracao_funcao',2,'p_declaracao_funcao_error','parser.py',94),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','parser.py',99),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','parser.py',100),
  ('lista_variaveis -> lista_variaveis COM var','lista_variaveis',3,'p_lista_variaveis','parser.py',105),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','parser.py',106),
  ('lista_variaveis -> lista_variaveis COM error','lista_variaveis',3,'p_lista_variaveis_error','parser.py',114),
  ('atribuicao -> var simbolo_atribuicao expressao','atribuicao',3,'p_atribuicao','parser.py',119),
  ('atribuicao -> condicional','atribuicao',1,'p_atribuicao','parser.py',120),
  ('atribuicao -> NOT condicional','atribuicao',2,'p_atribuicao','parser.py',121),
  ('condicional -> expressao_simples operador_relacional expressao_aditiva','condicional',3,'p_condicional','parser.py',133),
  ('condicional -> LPAR condicional RPAR','condicional',3,'p_condicional','parser.py',134),
  ('condicional -> condicional simbolo_condicional condicional','condicional',3,'p_condicional','parser.py',135),
  ('condicional -> condicional simbolo_condicional error','condicional',3,'p_condicional','parser.py',136),
  ('condicional -> LPAR error RPAR','condicional',3,'p_condicional','parser.py',137),
  ('condicional -> error simbolo_condicional condicional','condicional',3,'p_condicional','parser.py',138),
  ('simbolo_condicional -> OR','simbolo_condicional',1,'p_simbolo_condicional','parser.py',149),
  ('simbolo_condicional -> AND','simbolo_condicional',1,'p_simbolo_condicional','parser.py',150),
  ('simbolo_atribuicao -> ASS','simbolo_atribuicao',1,'p_simbolo_atribuicao','parser.py',155),
  ('atribuicao -> var simbolo_atribuicao error','atribuicao',3,'p_atribuicao_error','parser.py',159),
  ('cabecalho -> ID LPAR lista_parametros RPAR corpo FIM','cabecalho',6,'p_cabecalho','parser.py',163),
  ('cabecalho -> ID LPAR lista_parametros RPAR corpo error','cabecalho',6,'p_cabecalho_error','parser.py',167),
  ('corpo -> corpo acao','corpo',2,'p_corpo','parser.py',172),
  ('corpo -> empty','corpo',1,'p_corpo','parser.py',173),
  ('acao -> expressao','acao',1,'p_acao','parser.py',182),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','parser.py',183),
  ('acao -> se','acao',1,'p_acao','parser.py',184),
  ('acao -> repita','acao',1,'p_acao','parser.py',185),
  ('acao -> leia','acao',1,'p_acao','parser.py',186),
  ('acao -> escreve','acao',1,'p_acao','parser.py',187),
  ('acao -> retorna','acao',1,'p_acao','parser.py',188),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','parser.py',194),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','parser.py',195),
  ('se -> SE expressao error corpo FIM','se',5,'p_se_error','parser.py',205),
  ('se -> error SENAO corpo FIM','se',4,'p_se_error','parser.py',206),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','parser.py',214),
  ('repita -> REPITA corpo error','repita',3,'p_repita_error','parser.py',219),
  ('leia -> LEIA LPAR ID RPAR','leia',4,'p_leia','parser.py',223),
  ('escreve -> ESCREVE LPAR expressao RPAR','escreve',4,'p_escreve','parser.py',228),
  ('retorna -> RETORNA LPAR expressao RPAR','retorna',4,'p_retorna','parser.py',233),
  ('var -> ID','var',1,'p_var','parser.py',239),
  ('var -> ID indice','var',2,'p_var','parser.py',240),
  ('expressao -> expressao_simples','expressao',1,'p_expressao','parser.py',249),
  ('expressao -> atribuicao','expressao',1,'p_expressao','parser.py',250),
  ('lista_parametros -> lista_parametros COM parametro','lista_parametros',3,'p_lista_parametros','parser.py',257),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','parser.py',258),
  ('lista_parametros -> empty','lista_parametros',1,'p_lista_parametros','parser.py',259),
  ('indice -> indice LBR expressao RBR','indice',4,'p_indice','parser.py',268),
  ('indice -> LBR expressao RBR','indice',3,'p_indice','parser.py',269),
  ('indice -> indice LBR error RBR','indice',4,'p_indice_error','parser.py',279),
  ('indice -> LBR error RBR','indice',3,'p_indice_error','parser.py',280),
  ('indice -> error RBR','indice',2,'p_indice_error','parser.py',281),
  ('indice -> LBR error','indice',2,'p_indice_error','parser.py',282),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','parser.py',288),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','parser.py',289),
  ('parametro -> tipo COLON ID','parametro',3,'p_parametro','parser.py',299),
  ('parametro -> parametro dimension','parametro',2,'p_parametro','parser.py',300),
  ('dimension -> LBR RBR','dimension',2,'p_dimension','parser.py',308),
  ('operador_relacional -> LET','operador_relacional',1,'p_operador_relacional','parser.py',314),
  ('operador_relacional -> GRT','operador_relacional',1,'p_operador_relacional','parser.py',315),
  ('operador_relacional -> EQU','operador_relacional',1,'p_operador_relacional','parser.py',316),
  ('operador_relacional -> NEQ','operador_relacional',1,'p_operador_relacional','parser.py',317),
  ('operador_relacional -> LEQ','operador_relacional',1,'p_operador_relacional','parser.py',318),
  ('operador_relacional -> GEQ','operador_relacional',1,'p_operador_relacional','parser.py',319),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','parser.py',326),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','parser.py',327),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','parser.py',337),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','parser.py',338),
  ('operador_soma -> ADD','operador_soma',1,'p_operador_soma','parser.py',348),
  ('operador_soma -> SUB','operador_soma',1,'p_operador_soma','parser.py',349),
  ('operador_multiplicacao -> TIMES','operador_multiplicacao',1,'p_operador_multiplicacao','parser.py',356),
  ('operador_multiplicacao -> DIV','operador_multiplicacao',1,'p_operador_multiplicacao','parser.py',357),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','parser.py',364),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','parser.py',365),
  ('fator -> LPAR expressao RPAR','fator',3,'p_fator','parser.py',375),
  ('fator -> var','fator',1,'p_fator','parser.py',376),
  ('fator -> chamada_funcao','fator',1,'p_fator','parser.py',377),
  ('fator -> numero','fator',1,'p_fator','parser.py',378),
  ('numero -> INTEIRO','numero',1,'p_numero','parser.py',388),
  ('numero -> FLUTUANTE','numero',1,'p_numero','parser.py',389),
  ('chamada_funcao -> ID LPAR lista_argumentos RPAR','chamada_funcao',4,'p_chamada_funcao','parser.py',395),
  ('lista_argumentos -> lista_argumentos COM expressao','lista_argumentos',3,'p_lista_argumentos','parser.py',401),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','parser.py',402),
  ('lista_argumentos -> empty','lista_argumentos',1,'p_lista_argumentos','parser.py',403),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',412),
]
