"""10. Faça um programa que mostre os n termos da Série a seguir:
 S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série. """

resultado = 0

n_termos = input("Número de termos: ")
while n_termos.isalpha() or int(n_termos) < 0:
    n_termos = input("Valor inválido, número de termos: ")
n_termos = int(n_termos)

valor_n = 1
valor_m = 1

for i in range(n_termos, 0, -1):
    divisao = valor_n/valor_m
    valor_n = valor_n + 1
    valor_m = valor_m + 2
    resultado = resultado + divisao

print(f"Soma total dos termos: {resultado:.3f}")