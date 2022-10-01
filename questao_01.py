"""1.Escreva um programa que calcula a média de 30 alunos e informa a situação
(reprovado, aprovado ou recuperação)"""


for i in range(0, 30):

    nota_1 = input("Nota 1: ")
    while nota_1.isalpha() or float(nota_1) > 10 or float(nota_1) < 0:
        nota_1 = input("\033[31m Valor acima ou abaixo do permitido, digite um valor entre 0 e 10: \033[m")

    nota_2 = input("Nota 2: ")
    while nota_2.isalpha() or float(nota_2) > 10 or float(nota_2) < 0:
        nota_2 = input("\033[31mValor acima ou abaixo do permitido, digite um valor entre 0 e 10: \033[m")

    media = (float(nota_1) + float(nota_2)) / 2

    if media >= 7:
        situacao = "Aprovado"
    elif 4 < media <= 6.99:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"\033[4;36;40m O aluno obteve média {media} e sua situação é {situacao}.\033[m")

