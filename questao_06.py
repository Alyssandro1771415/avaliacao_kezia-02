"""6. Faça um programa para calcular um valor A elevado a um expoente B. Os
valores A e B deverão ser lidos. Não usar A** B e sim uma estrutura de
repetição."""

x = 0

numero = input("Valor: ")
while numero.isalpha():
    numero = input("Valor inválido, digite um número: ")
numero = int(numero)

expoente = input("Expoente: ")
while expoente.isalpha():
    expoente = input("Valor inválido, digite um número: ")
expoente = int(expoente)

potenciacao = 1

while x < abs(expoente):
    potenciacao *= int(numero)
    x += 1

if expoente < 0:
    potenciacao = f"1/{potenciacao}"
    print(f"Resultado: {potenciacao}")
elif expoente > 0:
    print(f"Resultado: {potenciacao}")
else:
    print("Resultado: 0")
