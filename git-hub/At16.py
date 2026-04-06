# Ler um valor e exibir o tipo do valor, se for inteiro exibir o valor elevado ao quadrado.

A = input("Digite um valor: ")
tipo = type(A)
print(tipo)
if tipo == int:
    print(tipo ** 2)