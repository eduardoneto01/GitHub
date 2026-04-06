# Ler um valor e verificar se ele o um número inteiro está entre 0 e 100, caso contrário, mostrar o valor lido.

A = int(input("Digite um número inteiro: "))
if not (0 < A < 100):
    print(A)