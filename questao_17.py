"""17. Faça um programa que receba o valor de uma dívida e mostre uma tabela com 
os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e 
valor da parcela. 
Os juros e a quantidade de parcelas seguem a tabela abaixo: 
Quantidade de Parcelas e % de Juros sobre o valor inicial da dívida
1 0
3 10
6 15
Exemplo de saída do programa: 
Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
R$ 1.000,00 0 1 R$ 1.000,00
R$ 1.100,00 10 3 R$ 366,00
R$ 1.150,00 15 6 R$ 191,67"""

valor_divida = input("Valor da dívida: ")

while valor_divida.isalpha() or float(valor_divida) < 0:
    valor_divida = input("Inválido, valor da dívida: ")

valor_divida = float(valor_divida)

print("valor da dívida", "valor juros", "quantidade parcelas", "valor parcelas", sep='\t\t')

for i in range(3):
    if i == 0:
        valor_juros = 0
        quantidade_parcelas = 1

    elif i == 1:
        valor_juros = 0.1
        quantidade_parcelas = 3

    else:
        valor_juros = 0.15
        quantidade_parcelas = 6

    acrescimo_juros = valor_divida * valor_juros
    valor_total = valor_divida + acrescimo_juros
    valor_parcelas = float((valor_divida + (valor_divida*valor_juros)) / quantidade_parcelas )
    
    print(f"\033[4;36mR$ {valor_total}", f"{valor_juros * 100}%", quantidade_parcelas, f"R${valor_parcelas:.2f}\033[m", sep='\t\t\t')
