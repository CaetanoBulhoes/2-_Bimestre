# 10. Escreva um algoritmo que mostre todos os possíveis lançamentos de três dados.

dado1 = [1,2,3,4,5,6]
dado2 = [1,2,3,4,5,6]
dado3 = [1,2,3,4,5,6]

for i in dado1:
    for p in dado2:
        for t in dado3:
            print(f"{i},{p},{t}")