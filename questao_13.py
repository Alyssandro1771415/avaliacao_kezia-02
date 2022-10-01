"""13. Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo. Um número primo é aquele que é divisível somente por ele
mesmo e por 1."""

numero = input("Digite um valor para saber se é primo: ")
resultado = 0

while numero.isalpha():
    numero = input("Dgito inválido ou 0, digite um valor para saber se é primo: ")
numero = int(numero)

for i in range(1, abs(numero)+1):
    if abs(numero) % i == 0:
        resultado += 1

if resultado == 2:
    print(f"\033[4;36;40mO Número {numero} é primo!\033[m")

else:
    print(f"\033[4;36;40mO Valor {numero} não é primo!\033[m")