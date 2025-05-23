# 3. Escreva um algoritmo que apresente na tela as tabuadas de 1 até 10.

num = int(input("Digite um número:"))

for cont in range (1,10 + 1):
    multi = num * cont
    print(f"{num} * {cont} = {multi}")