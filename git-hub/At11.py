# Ler um número e: Se for par e positivo print “Par positivo”; Se for par e negativo print “Par e negativo”; caso contrário print “Ímpar”. 

A = int(input("Digite um número inteiro: "))
if A % 2 == 0 and A > 0:
    print("O número é par e positivo.")
elif A % 2 == 0 and A < 0:
    print("O número é par e negativo.")
else:   print("O número é ímpar.")