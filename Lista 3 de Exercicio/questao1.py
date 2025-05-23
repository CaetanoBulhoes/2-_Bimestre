#1. Escreva um algoritmo que diga se o número é par ou ímpar

num = int(input("Escreva um número: "))

if num % 2 == 0:
    print(f"O número {num} é par.")

else:
    print(f"O número {num} é ímpar.")