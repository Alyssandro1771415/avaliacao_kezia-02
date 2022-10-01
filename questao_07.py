"""7. Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N. Faça um programa para gerar e
mostrar o número H. O número N será fornecido como entrada."""

numero = input("Digite o n´mero de valores a somar: ")
resultado = 0
contador = 1

while numero.isalpha():
    numero = input("Valor inválido, digite o número de valores a somar: ")
numero = int(numero)

for i in range(numero, 0, -1):
    resultado = resultado + (1/contador)
    contador += 1

print("Resultado: {:.3f}".format(resultado))
