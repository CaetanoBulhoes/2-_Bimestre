# 15.Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% ao ano, escreva um algoritmo que calcule o tempo necessário para que a população do país A ultrapasse a população do país B.

tempo = 0
populacao_A = 5*(10**6)
populacao_B= 7*(10**6)

while True:
    tempo += 1
    A_porcentagem = populacao_A * 0.03
    populacao_A += A_porcentagem

    B_porcentagem = populacao_B * 0.02
    populacao_B += B_porcentagem

    if populacao_A > populacao_B:
        break

print(f"\nSerá necessário {tempo} anos para que a Cidade A ultrapasse a Cidade B!\n")




