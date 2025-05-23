# 3. Escreva um algoritmo que diga o conceito de um aluno baseado em uma nota.

nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Você é um otimo aluno.")

elif nota >= 4:
    print("Tua situação tá complicada")

else:
    print(f"Irmão, tu tá passando bem?")