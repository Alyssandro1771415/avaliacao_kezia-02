"""19. A câmara municipal de uma cidade fez uma pesquisa entre seus habitantes, coletando
dados sobre o salário e número de filhos. A prefeitura deseja saber:
a) Média do salário da população;
b) Média do número de filhos;
c) Maior salário;
d) Percentual de pessoas com salário até R$250,00.
Desenvolver um programa para calcular e escrever o que foi pedido nos itens
a, b, c e d. O final da leitura de dados se dará com a entrada de um salário
negativo."""

contador = 0
total_filhos = total_salario = 0
maior_salario = 0
percentual_250 = 0
salario = 0

while salario >= 0:

    salario = input("Salário: ")

    while salario.isalpha():
        salario = input("Inválido, salário: ")
    salario = float(salario)

    if salario >= 0:
        numeroFilhos = input("Quantidade de filhos: ")

        while numeroFilhos.isalpha() or int(numeroFilhos) < 0:
            numeroFilhos = input("Número de filhos inválido, digite novamente: ")
        numeroFilhos = int(numeroFilhos)

        contador = contador + 1

        total_salario += salario
        total_filhos += numeroFilhos

        if contador == 1:
            maior_salario = salario

        if salario > maior_salario:
            maior_salario = salario

        if salario <= 250:
            percentual_250 = percentual_250 + 1
    
    elif contador == 0:
        print("Finalizado!")

    else:

        mediaSalarial = float(total_salario / contador)
        mediaFilhos = float(total_filhos / contador)

        print(f"Média salarial: {mediaSalarial}")
        print(f"Média de filhos: {mediaFilhos}")
        print(f"Maior salario: {maior_salario}")
        print(f"Percentual de pessoas com salario até R$250: {percentual_250*100/contador}%")
