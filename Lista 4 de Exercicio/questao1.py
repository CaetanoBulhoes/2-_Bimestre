
print("\nVocê quer que mostra uma lista de 100 a 1 ou de 1 a 100?\n100 a 1: 1 \n1 a 100: 0\n")

escolha = int(input("Escolha:"))

if escolha == 1:

    for i in range(100, 0, -1):
        print(f"{i}")

elif escolha == 0:

    for i in range(1,100 + 1 ):
        print(f"{i}")
    
else:
    print("Essa opção não existe")