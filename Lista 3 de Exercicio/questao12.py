# 12. Escreva um algoritmo que implemente uma calculadora simples com 4 operações. Considere divisão por zero.

while True:
     
        print(f"\nEscolha uma das opções:\nSoma:0\nSubtração:1\nMultiplicação:2\nDivisão:3\n")

        opcao = int(input("Escolha: "))
        resultado = 0
        if opcao == 0:

            quantidade = int(input("Digite quantos números deseja somar: "))

            for i in range(quantidade):

                soma = float(input(f"Digite o {i + 1}° número: "))
                resultado += soma

            print(f"\nA soma dos {quantidade} números é {resultado}")
            

        elif opcao == 1:
            sub1 = float(input("Digite o primeiro número: "))
            sub2 = float(input("Digite o segundo número: "))
            
            print(f"\nA subtração entre os dois números é {sub1 - sub2}")
            

        elif opcao == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            print(f"\nA multiplicação entre os dois números é {num1 * num2}")
            

        elif opcao == 3:
            div1 = float(input("Digite o primeiro número: "))
            div2 = float(input("Digite o segundo número: "))
            
            if div1 != 0 and div2 != 0:
                 print(f"\nA divisão entre esses dois números é{div1 / div2}")
            
            else:
                print("\nA divisão entre esses dois números é 0 ")
            

        else:
            print("Essa opção não existe!")

        print("\nDeseja repetir?")
        escolha = int(input("Sim: 1\nNão:0\nEscolha:"))
        if escolha == 0:
             break
        