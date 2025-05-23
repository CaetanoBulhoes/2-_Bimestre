#9.Escreva um algoritmo que mostre todas as possibilidades de que no lançamento de dois dados tenhamos o valor 7 como resultado da soma dos valores de cada dado.

dado1 = [1,2,3,4,5,6]
dado2 = [1,2,3,4,5,6]

for i in dado1:
    for p in dado2:
        if i + p == 7:
            print(f"{i} + {p} = 7")