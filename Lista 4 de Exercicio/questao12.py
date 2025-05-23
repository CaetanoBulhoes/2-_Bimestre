# 12. Escreva um algoritmo que receba os dados sobre 15 pessoas: peso e idade

maior_idade = 0 
quantidade = 0
soma = 0


for i in range(4):
    peso = float(input("Digite seu peso: "))
    idade = int(input("Digite sua idade: "))

    if idade > 12: 
        quantidade += 1
        soma += peso
        
        if idade > maior_idade:
            maior_idade = idade

media = soma / quantidade

print(f"A média dos pesos é:{media:.2f} Kg.")
print(f"A maior idade entre todos é {maior_idade} anos.")

