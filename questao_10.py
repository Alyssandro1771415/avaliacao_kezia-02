"""10. Faça um programa que mostre os n termos da Série a seguir:
 S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série. """

n_termos = input("Número de termos: ")
while n_termos.isalpha():
    n_termos = input("Valor inválido, número de termos: ")
n_termos = int(n_termos)

valor_n = 1
valor_m = 1

for i in range(n_termos, 0, -1):
    print(f"{valor_n}/{valor_m}")
    valor_n += 1
    valor_m += 2
