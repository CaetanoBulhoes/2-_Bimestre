# 11. Escreva um algoritmo que receba dados sobre 10 pessoas: nome, sexo (M ou F) e altura.

altura_f = []
altura_m = []
quantidade_m = 0
nome_mulher = 0

for i in range(10):
    nome = input("\nQual seu nome?\nDigite:")
    genero = input("\nQual seu genero? F(Feminino) ou M(Masculino)\nDigite:")
    altura = float(input("\nQual sua altura?\nDigite:"))

    if genero.upper() == "F":

        altura_f.append(altura)
        altura_f.sort()

        if altura <=  altura_f[0]:

            nome_mulher = nome
        
    elif genero.upper() == "M": 

        altura_m.append(altura)
        altura_m.sort()
        quantidade_m += 1

maior_altura_m = max(altura_m)
maior_altura_f = max(altura_f)
menor_altura_m = min(altura_m)
menor_altura_f = min(altura_f)
soma = sum(altura_f)
media = soma / len(altura_f)

print(f"\nMaiores alturas:\nMasculino: {maior_altura_m:.2f} e Feminino: {maior_altura_f:.2f}\nMenores alturas:\nMasculino: {menor_altura_m:.2f} e Feminino: {menor_altura_f:.2f}")
print(f"\nA média das alturas das mulheres é: {media:.2f}")
print(f"\nA quantidade de homens é: {quantidade_m}")
print(f"\nA {nome_mulher} possui {menor_altura_f:.2f} m, tendo assim a menor altura.\n")