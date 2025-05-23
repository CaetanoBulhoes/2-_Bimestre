# 10. Escreva um algoritmo que receba quatro notas de um aluno, calcule e imprima a média aritmética das notas e a mensagem de aprovado para média superior ou igual a 7.0 ou a mensagem de reprovado para média inferior a 7.0.

total = 0
bimestre = 0 
for i in range(4):

    bimestre += 1
    nota = float(input(f"Digite sua nota do {bimestre}° bimestre: "))

    total += nota

media = float(total/bimestre)

if media >= 7:
    print(f"Aprovado! Sua média foi {media}")

else:
    print(f"Reprovado! Sua média foi {media}")
