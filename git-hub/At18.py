# Ler um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro.

A = int(input("Digite um número inteiro: "))
if A % 2 == 0 and A > 0:
    print("O número é par e positivo.")
elif A % 2 == 0 and A < 0:
    print("O número é par e negativo.")
elif A % 2 != 0 and A > 0:
    print("O número é ímpar e positivo.")
elif A % 2 != 0 and A < 0:
    print("O número é ímpar e negativo ou neutro.")