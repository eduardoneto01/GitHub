altura = int(input("Digite a altura em centímetros: "))
peso = int(input("Digite o peso em kg: "))

altura2 = altura / 100

imc = peso / (altura2 ** 2)
print(imc)