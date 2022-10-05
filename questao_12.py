"""12. Faça um programa que receba dois números inteiros e gere os números
inteiros que estão no intervalo compreendido por eles."""

ordem_progresso = 1

valor_1 = input("Inicio da contagem: ")
while valor_1.isalpha():
    valor_1 = input("Inválido, inicio da contagem: ")
valor_1 = int(valor_1)

valor_2 = input("Fim da contagem: ")
while valor_2.isalpha():
    valor_2 = input("Inválido, fim da contagem: ")
valor_2 = int(valor_2)

if valor_1 > valor_2:
    ordem_progresso = -1


for i in range(valor_1 + ordem_progresso, valor_2, ordem_progresso):
    print(i)
