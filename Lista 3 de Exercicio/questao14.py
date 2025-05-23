# 14. Faça um algoritmo/programa que receba a idade de uma pessoa e classifique-a

idade = int(input("Digite sua idade: "))

if idade <= -1:
    print("Não é  possivel ter uma idade negativa.")

elif idade <= 2:
    print("Você é um recém-nascido!")

elif idade <= 11:
    print("Você é uma criança!")

elif idade <= 19:
    print("Você é um adolescente!")

elif idade <= 55:
    print("Você é um adulto!")

elif idade > 55:
    print("Você é um idoso!")

