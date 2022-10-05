"""18. Uma grande firma deseja saber qual é o empregado mais recente e qual é o 
mais antigo. Desenvolver um programa para ler um número indeterminado de 
informações contendo o número do empregado e o número de meses de 
trabalho deste empregado e imprimir o mais recente e o mais antigo. Obs.: A 
última informação contém os dois números iguais a zero. Não existem dois 
empregados admitidos no mesmo mês"""



contador = 0
resposta = "S"
maisAntigo = maisNovo = 0
meses = []

while resposta == "S":

    resposta = input("Deseja adicionar um empregado[S/N]: ").upper()
    
    while resposta not in "SN":
        resposta = input("Deseja adicionar um empregado[S/N]: ").upper()
    
    contador = contador + 1

    if resposta == "S":
        numero_empregado = input("Número do empregado: ")
        while numero_empregado.isalpha() or float(numero_empregado) < 0:
            numero_empregado = input("Número do empregado: ")
            
        numero_meses = input("Número de meses na empresa: ")
        while numero_meses in meses:
            numero_meses = input("Inválido, nesse mês já houve contratação, tente novamente: ")

        meses.append(numero_meses)

        if contador == 1:
            maisAntigo = maisNovo = numero_empregado

        if numero_meses > maisAntigo:
            maisAntigo = numero_empregado

        if numero_meses < maisNovo:
            maisNovo = numero_empregado

    elif resposta == "N":
        print(f"\033[4;36;40mFuncionário mais antigo: {maisAntigo}\033[m")
        print(f"\033[4;36;40mFuncionário mais novo: {maisNovo}\033[m")

print("Funcionário mais antigo: 0")
print("Funcionário mais novo: 0")