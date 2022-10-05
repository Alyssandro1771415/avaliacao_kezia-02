"""11. Cada espectador de um cinema respondeu a um questionário no qual constava
sua idade e a sua opinião em relação ao filme: ótimo - 3, bom - 2, regular - 1.
Faça um programa que receba a idade e a opinião de 15 espectadores, calcule
e imprima:
a) A média das idades das pessoas que responderam ótimo;
b) A quantidade de pessoas que responderam regular;
c) A porcentagem de pessoas que responderam bom entre todos os
espectadores analisados."""


soma_idade_otimo = 0
avaliacao_regular = 0
soma_bom = 0

for i in range(0, 15):
    idade = input("Idade: ")
    while idade.isalpha() or int(idade) < 0:
        idade = input("Inválido, digite sua idade: ")
    idade = int(idade)

    opiniao = input("Conceito(3-ótimo, 2-bom, 1-regular): ")
    while opiniao.isalpha() or int(opiniao) > 3 or int(opiniao) < 1:
        opiniao = input("Conceito(3-ótimo, 2-bom, 1-regular): ")
    opiniao = int(opiniao)


    if opiniao == 3:
        soma_idade_otimo = soma_idade_otimo + idade
    if opiniao == 1:
        avaliacao_regular = avaliacao_regular + 1
    if opiniao == 2:
        soma_bom = soma_bom + 1


print(f"Média de idade das pessoas que opinaram o filme como ótimo: {soma_idade_otimo/15}")
print(f"Total de avaliações regulares: {avaliacao_regular}")
print(f"Porcentagem de avaliações boas: {soma_bom*100/15}%")
