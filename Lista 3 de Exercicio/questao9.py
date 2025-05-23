# 9.Escreva um algoritmo que recebe o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor, e caso não haja vencedor deverá ser mostrar a palavra EMPATE.

time1 = []
time2 = []

time1.append(input("Digite o nome do time 1: "))
time2.append(input("Digite o nome do time 2: "))

time1.append(int(input(f"Digite o número de gols do time {time1[0]}: ")))
time2.append(int(input(f"Digite o número de gols do time {time2[0]}: ")))

if time1[1] > time2[1]:
    print(f"O time {time1[0]} ganhou com {time1[1]} Gols!")
elif time2[1] > time1[1]:
    print(f"O time {time2[0]} ganhou com {time2[1]} Gols!")

else:
    print(f"Os dois times ficaram empatados, ficando {time1[1]} x {time2[1]}")