# 8.Escreva um algoritmo que receba cinco números e diga a quantidade de números negativos.

total = 0

for i in range(5):

    num = int(input("Digite um número: "))

    if num < 0:
       total += 1

print(f"O quantidade de números negativos é {total}")