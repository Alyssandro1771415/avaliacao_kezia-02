"""14. Faça um programa que peça para n pessoas a sua idade, ao final o programa
devera verificar se a média de idade da turma varia entre 0 e 25, 26 e 60 e
maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
média calculada."""

resposta = "S"
soma = 0
contador = 0

while resposta == "S":
    resposta = input("Deseja inserar uma idade[S/N]: ").upper()

    if resposta == "S":
        idade = input("Idade: ")
        soma += idade
        contador += 1
    elif resposta == "N":
        media = soma/contador
        if media <= 25:
            conceito = "Jovem"
        elif media > 26 and media < 60:
            conceito = "Adulto"
        else:
            conceito = "Idosa"
        print(f"A média de idade dos usuários é {}")

