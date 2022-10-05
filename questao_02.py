"""2. Escreva um programa que leia 10 números e informe o maior e o menor
número."""
maior = menor = 0
contador = 0

for i in range(0, 10):

    numero = input("Digite um valor: ")
    while numero.isalpha():
        numero = input("\033[31;40mValor inválido, digite um valor numérico: \033[m")
    numero = float(numero)

    contador += 1

    if contador == 1:
        maior = menor = numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f"Maior: {maior}")
print(f"Menor: {menor}")
