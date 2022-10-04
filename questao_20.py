"""20. Faça um programa que leia uma quantidade não determinada de números 
positivos. Calcule a quantidade de números pares e ímpares, a média de 
valores pares e a média geral dos números lidos. O número que encerrará a 
leitura será zero."""

quantidadePares = quantidadeImpares = somaPares = somaImpares = 0

somaTotal = 0

numero = 1

while numero != 0:

    numero = input("Digite um valor positivo(0 encerra o programa): ")
    while numero.isalpha() or float(numero) < 0:
        numero = input("Digite um valor: ")

    numero = int(numero)

    somaTotal += numero

    if numero % 2 == 0:
        quantidadePares += 1
        somaPares += numero
    else:
        quantidadeImpares += 1
        
quantidadePares -= 1 #Para eliminar o 0
quantidadeTotal = quantidadeImpares + quantidadePares
mediaPares = (quantidadePares / quantidadeTotal) * 100
mediaGeral = somaTotal / quantidadeTotal

print(f"\033[4;36mQuantidade de valores pares: {quantidadePares}\nQuantidade de valores ímpares: {quantidadeImpares}\nMédia de valores pares: {mediaPares}%\nMédia geral dos valores: {mediaGeral}\033[m")
