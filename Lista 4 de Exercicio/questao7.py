# 7. Escreva um algoritmo que receba um número e mostre a média da soma de todos os números até ele.

num = int(input("Digite um número: "))
soma = 0

for i in range(num + 1):

    soma += i

media = soma / num 

print(media)