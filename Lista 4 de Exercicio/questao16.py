# 16. Escreva um algoritmo que receba a idade e o estado civil (C-Casado, S-solteiro, V-viúvo e D-divorciado) de várias pessoas.

quantidade_C = 0
quantidade_V = 0
quantidade_D = 0
quantidade_S = 0
soma_idade = 0
total = 0

for i in range(3):

    idade = int(input("Digite sua idade: "))
    status_civil = input("Estados Civis:\nCasado-C\nSolteiro-S\nViúvo-V\nDivorciado-D\nDigite em qual estado está agora:")

    if status_civil.upper() == "C":

        total += 1
        quantidade_C += 1

    elif status_civil.upper() == "S":

        total += 1
        quantidade_S += 1

    elif status_civil.upper()  == "V":

        total += 1
        quantidade_V += 1
        soma_idade += idade

    elif status_civil.upper() == "D":

        total += 1
        quantidade_D += 1

    else:
        print("Esse Estado Civil não existe, reescreva tudo denovo.")
        
media_viuvas = soma_idade / quantidade_V
porcentagem = ((total - (total - quantidade_D)) / total) * 100
print(f"A quantidade de pessoas casadas é: {quantidade_C} pessoas")
print(f"A quantidade de pessoas solteiras  é: {quantidade_S} pessoas")
print(f"A media da idade das pessoas viuvas é: {media_viuvas} anos")
print(f"A porcentagem de pessoas divorciada é: {porcentagem:.1f}%")



     

