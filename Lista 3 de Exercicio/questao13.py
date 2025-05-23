# 13.Faça um algoritmo/programa que calcule e imprima o salário reajustado de um funcionário de acordo com a seguinte regra:
# • salários até 1200, reajuste de 50%
# • salários maiores que 1200, reajuste de 30%

salario = float(input("Digite seu salário: "))

if salario <=1200:
    ajuste = salario * 0.5

    salario_final = salario + ajuste

    print(f"O ajuste Salarial foi de R${ajuste}, ficando agora R${salario_final}")

else:
    ajuste = salario * 0.3

    salario_final = salario + ajuste

    print(f"O ajuste salarial foi de R${ajuste}, ficando agora R${salario_final}")