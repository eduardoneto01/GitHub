# Ler um valor e identificar se ele está entre 0 e 10, se for exibir a frase de dentro do intervalo, se não, apresentar a frase de fora do intervalo.

A = int(input("Digite um número inteiro: "))
if 0 <= A <= 10:
    print("Dentro do intervalo")
else:   print("Fora do intervalo.")