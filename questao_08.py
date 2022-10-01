"""8. Faça um programa para:
a) Ler um valor x qualquer
b) Calcular Y = (x+1)+(x+2)+(x+3)+(x+4)+(x+5)+…(x+100)"""

resultado = 0

valor = input("Valor: ")
while valor.isalpha():
    valor = input("Valor inválido, digite um valor numérico: ")
valor = float(valor)

for i in range(1, 101):
    resultado = resultado + (valor + i)

print(f"Resultado: {resultado}")
