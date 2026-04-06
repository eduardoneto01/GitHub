# Ler dois números inteiros e mostrar uma mensagem caso eles sejam iguais, caso contrário, mostrar outra mensagem.

A = int(input("Digite um número inteiro: "))
B = int(input("Digite um número inteiro: "))
if A != B:
    print("Os números são diferentes, a diferença entre eles é {A - B}.")
  
else:
    print("Os números são iguais.")
