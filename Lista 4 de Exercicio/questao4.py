#4. Escreva um algoritmo que receba dois números e mostre o somatório dos números entre eles.

comeco = int(input("Digite o primeiro número: "))
fim = int(input("Digite o ultimo número: "))

soma = 0
num = 0
for i in range(comeco,fim + 1):

    num = i
    soma += num

print(soma)