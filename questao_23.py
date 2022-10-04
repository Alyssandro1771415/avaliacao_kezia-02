"""23. Faça um programa que receba um número e verifique se ele é ou não triangular. 
 OBS: um número é triangular quando é resultado do produto de 3 números 
consecutivos. Exemplo: o número 24 é triangular, pois, 24 = 2 * 3 * 4"""



numero = input("Valor: ")
while numero.isalpha() or int(numero) < 0:
    numero = input("Inválido, digite um valor numérico e positivo: ")
numero = int(numero)

contador = 1

while contador * (contador+1) * (contador+2) < numero:
    contador += 1

if contador * (contador+1) * (contador+2) == numero:
    print(f"{numero} = {contador}x{contador+1}x{contador+2}")
else:
    print(f"O valor {numero} não é triangular!")