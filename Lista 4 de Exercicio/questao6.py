# 6. Escreva um algoritmo que receba n números e tire a média entre eles.
quantidade = int(input("Digite quantos números você vai somar: "))
soma = 0

for i in range(quantidade):

    num = float(input("Digite um número: "))

    soma += num

media = soma / quantidade

print(f"A media dos {quantidade} números é {media:.2f}")