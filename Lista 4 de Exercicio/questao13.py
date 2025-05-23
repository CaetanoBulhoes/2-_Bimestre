#13. Escreva um algoritmo que receba a idade, a altura e o peso de 12 pessoas.

pessoas_acima_50 = 0
soma_altura = 0
total = 0
peso_menor_40 = 0
total = 0
pessoas_entre_10_20 = 0
peso_menor_40 = 0

for i in range(12):
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    total += 1

    for i in range(1):

        if idade > 50:
            pessoas_acima_50 += 1

        elif idade >= 10 and idade <= 20:
            
            soma_altura += altura
            pessoas_entre_10_20 += 1
        

    if peso < 40:
        peso_menor_40 += 1



num = total - (total - peso_menor_40) 
porcentagem = (num / total) * 100


print(f"A quantidade de pessoas acima de 50 é: {pessoas_acima_50}!")

if soma_altura == 0 or pessoas_entre_10_20 == 0:

    print("Não há pessoas entre 10 a 20 anos!")

else:

    media = soma_altura / pessoas_entre_10_20
    print(f"A média da altura das pessoas entre 10 e 20 é: {media}!")

print(f"A porcentagem de pessoas com o peso inferior a 40 Kg é: {porcentagem:.1f}% ")