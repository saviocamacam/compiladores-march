; ModuleID = "geracao/gencode-005.tpp"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"escrevaInteiro"(i32 %".1") 

declare void @"escrevaFlutuante"(float %".1") 

declare i32 @"leiaInteiro"() 

declare float @"leiaFlutuante"() 

define i32 @"soma"(i32* %"a", i32* %"b") 
{
entry-soma:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  %"left_side" = load i32, i32* %"a"
  %"right_side" = load i32, i32* %"b"
  %"temp+" = add i32 %"left_side", %"right_side"
  store i32 %"temp+", i32* %"retorno"
  br label %"exit-soma"
exit-soma:
  %"retFin" = load i32, i32* %"retorno"
  ret i32 %"retFin"
}

define i32 @"main"() 
{
entry-principal:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  %"a" = alloca i32, align 4
  %"b" = alloca i32, align 4
  %"c" = alloca i32, align 4
  %"readIa" = call i32 @"leiaInteiro"()
  store i32 %"readIa", i32* %"a"
  %"readIb" = call i32 @"leiaInteiro"()
  store i32 %"readIb", i32* %"b"
  %"retorno-soma" = call i32 @"soma"(i32* %"a", i32* %"b")
  store i32 %"retorno-soma", i32* %"c"
  %"writec" = load i32, i32* %"c"
  call void @"escrevaInteiro"(i32 %"writec")
  store i32 0, i32* %"retorno"
  br label %"exit-principal"
exit-principal:
  %"retFin" = load i32, i32* %"retorno"
  ret i32 %"retFin"
}
