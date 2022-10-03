"""15. A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos
são fornecidos pelo usuário; a partir daí, os termos são gerados com a soma
ou subtração dos dois termos anteriores, ou seja:
Faça um programa em Python para mostrar os N primeiros termos da série de
FETUCCINE, sabendo-se que para existir esta série serão necessários pelo
menos três termos."""


quant_termos = input("Quantos termos: ")
while quant_termos.isalpha() or int(quant_termos) < 3:
    quant_termos = input("Inválido, digite a quantidade de termos: ")
quant_termos = int(quant_termos)

n1 = n2 = 0
serie = int()

n1 = input("Primeiro termo: ")
while n1.isalpha():
    n1 = input("Inválido, digite o primeiro termo: ")
n1 = int(n1)

n2 = input("Segundo termo: ")
while n2.isalpha():
    n2 = int(input("Inválido, digite o segundo termo: "))
n2 = int(n2)

print(n1)
print(n2)

for i in range (3, quant_termos+1):
    if i % 2 == 0:
        serie = n2 + n1
    else:
        serie = n2 - n1

    n1 = n2
    n2 = serie

    print(serie, end=', ')
