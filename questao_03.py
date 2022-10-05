"""3. Escreva um programa que calcula o fatorial de um dado número N"""

valor = input("Digite um valor positivo: ")

while valor.isalpha() or int(valor) < 0:
    valor = input("\033[31;40mValor inválido, digite um valor numérico e positivo: \033[m")
valor = int(valor)

resultado = valor

for i in range(valor-1, 0, -1):
    resultado = resultado * i

print(f"\033[4;36;40mResultado: {resultado}\033[m")
