# 5. Escreva um algoritmo que mostre na tela a soma dos 200 primeiros ímpares.
soma = 0
num = 1
quantidade = 0

while quantidade < 200:

    soma += num
    num += 2
    quantidade += 1
print(f"A soma dos primeiros 200 números impares é {soma}!")

