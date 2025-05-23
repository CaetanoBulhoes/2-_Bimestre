# 14. Escreva um algoritmo que receba o valor e o código de várias mercadorias vendidas em um determinado dia.

quantidade = 10

# Códigos:
A = []
L = []
H = []

# Totais:
tA = 0
tL = 0
tH = 0
total = 0

for i in range(quantidade):
    codigo = input(f"O que você vai comprar?\nL:Limpeza\nA:Alimentação\nH:Higiene\nEscolha:")

    if codigo.upper() == "A":
        produto = input(f"Qual produto você vai comprar?\nDigite: ")
        A.append(produto)

        preco = float(input("Qual o preço dele?\nDigite:\n"))
        total += preco
        tA += preco

    elif codigo.upper() == "L":
        produto = input(f"Qual produto você vai comprar?\nDigite: ")
        L.append(produto)

        preco = float(input("Qual o preço dele?\nDigite:\n"))
        total += preco
        tL += preco

    elif codigo.upper() == "H":
        produto = input("Qual produto você vai comprar?\nDigite: ")
        H.append(produto)

        preco = float(input("Qual o preço dele?\nDigite:\n"))
        total += preco
        tH += preco

    else:
        print("Essa opção não existe! Escolha denovo.\n")
        quantidade += 1

print("Alimentação:")
for i in A:
    print(i)

print("\nLimpeza:")
for i in L:
    print(i)

print("\nHigiene: ")
for i in H:
    print(f"{i}\n")

print(f"Total: R${total:.2f}")

print(f"O total vendido de alimentação foi: R${tA:.2f}")
print(f"O total vendido de higiene foi: R${tH:.2f}")
print(f"O total vendido de limpeza foi: R${tL:.2f}")