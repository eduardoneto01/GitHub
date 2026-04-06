# Ler dois numeros, somar e depois mostrar se são (Maior, Menor ou Iguais)

A = int(input("Digite um número inteiro: "))
B = int(input("Digite outro número inteiro: "))

print ("A soma dos números é: ", A + B)
if A > B:
    print ("O número A é maior que o número B.")

elif B > A:
    print ("O número B é maior que o número A.")

else:    print ("Os números A e B são iguais.")