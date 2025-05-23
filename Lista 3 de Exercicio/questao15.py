# 15. Escreva um algoritmo que possa entrar com nome do produto e valor da compra e imprimir o nome do produto e valor de venda.

produto = input("Escreva o nome do produto: ")
valor = float(input("Escreva o valor do produto: "))

if valor < 10:
    print(f"O produto {produto} tem valor de venda de 70%!")

elif valor <= 30:
    print(f"O produto {produto} tem valor de venda de 50%!")

elif valor <= 50:
    print(f"O produto {produto} tem valor de venda de 40%!")
    
elif valor > 50:
    print(f"O produto {produto} tem valor de venda de 30%!")