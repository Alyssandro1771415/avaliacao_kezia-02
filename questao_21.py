"""21. O cardápio de uma lanchonete é o seguinte: 

Faça um programa que leia o código dos itens pedidos e as quantidades 
desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e 
o total geral do pedido. Considere que o cliente deve informar quando o pedido 
deve ser encerrado."""

print("\033[36;4mESPECIFICAÇÃO", "CÓDIGO", "PREÇO", sep='\t\t')
print("C. Quente", "100", "R$1,20", sep='\t\t')
print("Bauru simples", "101", "R$1,30", sep='\t\t')
print("Bauru com ovo", "102", "R$1,50", sep='\t\t')
print("Hambúrguer", "103", "R$1,20", sep='\t\t')
print("Cheesebúrguer", "104", "R$1,30", sep='\t\t')
print("Refrigerante", "105", "R$1,00\033[m", sep='\t\t')

total = 0
quantidade = 1
resposta = "S"

while resposta == "S":

    produto = input("Digite o código do produto: ")
    while produto.isalpha() or int(produto) > 105 or int(produto) < 100:
        produto = input("Código inválido, digite o código do produto: ")
    produto = int(produto)

    quantidade = input("Quantidade: ")
    while quantidade.isalpha():
        quantidade = input("Digite o código do produto: ")
    quantidade = int(quantidade)

    if produto == 100:
        print(f"Valor: R${1.20 * quantidade}")
        total = total + 1.20 * quantidade
    elif produto == 101:
        print(f"Valor: R${1.30 * quantidade}")
        total = total + 1.30 * quantidade
    elif produto == 102:
        print(f"Valor: R${1.50 * quantidade}")
        total = total + 1.50 * quantidade
    elif produto == 103:
        print(f"Valor: R${1.20 * quantidade}")
        total = total + 1.20 * quantidade
    elif produto == 104:
        print(f"Valor: R${1.30 * quantidade}")
        total = total + 1.30 * quantidade
    elif produto == 105:
        print(f"Valor: R${1.00 * quantidade}")
        total = total + 1.00 * quantidade

    resposta = input("Deseja pedir algo mais[S/N]: ").upper()
    while resposta not in "SN":
        resposta = input("Deseja pedir[S/N]: ").upper()

print(f"Valor total da compra: R${total}")
