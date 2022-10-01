"""4. Faça um programa para somar os números pares positivos < 1000 e ao final
escrever o resultado."""

resultado = 0

for i in range(0, 1000, 2):
    resultado += i
print(f"\033[36;40mO resultado da soma de todos os valores pares menores que 1000 é: {resultado}\033[m")
