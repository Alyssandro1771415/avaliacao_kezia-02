"""9. Fazer um programa que calcule e escreva a soma dos 50 primeiros termos da
seguinte série"""

valor = 1000
soma = 0

for i in range(1, 51):
    soma += valor/i
    valor -= 3

print(soma)