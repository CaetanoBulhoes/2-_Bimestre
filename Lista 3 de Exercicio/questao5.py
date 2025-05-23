# 5.Escreva um algoritmo que receba três números e mostre na tela em ordem crescente
lista = []

for i in range(3):

    num = int(input("Digite um número: "))

    lista.append(num)
    
lista.sort()
print(f"{lista}")   