"""19. A câmara municipal de uma cidade fez uma pesquisa entre seus habitantes, coletando
dados sobre o salário e número de filhos. A prefeitura deseja saber:
a) Média do salário da população;
b) Média do número de filhos;
c) Maior salário;
d) Percentual de pessoas com salário até R$250,00.
Desenvolver um programa para calcular e escrever o que foi pedido nos itens
a, b, c e d. O final da leitura de dados se dará com a entrada de um salário
negativo."""

resposta = "S"
contador = 0
total_filhos = total_salario = 0
maior_salario = 0
percentual_250 = 0

while resposta == "S":
    resposta = input("Deseja adinionar dados[S/N]: ").upper()

    while resposta not in "SN":
        resposta = input("Deseja adinionar dados[S/N]: ").upper()

    if resposta == "S":

        salario = input("Salário: ")

        while salario.isalpha() or float(salario) < 0:
            salario = input("Inválido, salário: ")
        salario = float(salario)

        numeroFilhos = input("Quantidade de filhos: ")

        while numeroFilhos.isalpha() or int(numeroFilhos) < 0:
            numeroFilhos = input("Inválido, salário: ")
        numeroFilhos = int(numeroFilhos)

        contador += 1

        total_salario += salario
        total_filhos += numeroFilhos

        if contador == 1:
            maior_salario = salario

        if salario > maior_salario:
            maior_salario = salario

        if salario <= 250:
            percentual_250 = ((percentual_250 + 1) / contador) * 100

    else:
        mediaSalarial = float(total_salario / contador)
        mediaFilhos = float(total_filhos / contador)

        print(f"Média salarial: {mediaSalarial}")
        print(f"Média de filhos: {mediaFilhos}")
        print(f"Maior salario: {maior_salario}")
        print(f"Percentual de salario até R$250: {percentual_250}%")
