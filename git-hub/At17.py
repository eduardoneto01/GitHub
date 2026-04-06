# ler a idade e classicar sua faixa etária, se for menor de idade, adulto ou idoso.

A = int(input("Digite sua idade: "))
if A <= 18:
    print("Você é menor de idade.")
elif A >= 18 and A <= 59:
    print("Você é adulto.")
else:
    print("Você é idoso.")