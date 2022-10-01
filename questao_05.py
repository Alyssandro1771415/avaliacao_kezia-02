"""5. Faça um programa para calcular a área de N quadriláteros. Fórmula: Área =
Lado * Lado."""

resposta = "S"

while resposta == "S":

    resposta = input("Deseja calcular a área de um quadrilátero S/N? ").upper()

    if resposta == "S":
        lado_1 = input("Digite o valor do primeiro lado: ")
        while lado_1.isalpha() or float(lado_1) < 0:
            lado_1 = input("\033[31;40mValor inválido, digite um valor numérico e positivo: \033[m")

        lado_2 = input("Digite o valor do primeiro lado: ")
        while lado_2.isalpha() or float(lado_2) < 0:
            lado_2 = input("\033[31;40mValor inválido, digite um valor numérico e positivo: \033[m")

        print(f"\033[36;40mA área do quadrilátero informado é: {float(lado_1)*float(lado_2)}m²\033[m")

    elif resposta == "N":
        print("Programa encerrado!")

    else:
        print("Resposta inválida!")
