{Aviso: Variável 'b' declarada e não utilizada}
{Aviso: Atribuição de tipos distintos 'b' inteiro e 'c' flutuante}
{Aviso: Atribuição de tipos distintos 'a' flutuante e 'func' retorna inteiro}
{Erro: Função principal deveria retornar inteiro, mas retorna vazio}

inteiro func(inteiro: x, inteiro: y)
	retorna (x + y)
fim

inteiro principal()
	flutuante: a, d
	flutuante: c
	inteiro: b

	d := c

	a := func(10,5)
fim
