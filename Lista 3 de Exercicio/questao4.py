# 4. Escreva um algoritmo que, para uma conta bancária, leio o seu número, o saldo, o tipo de operação a ser realizada (depósito ou retirada) e o valor da operação. Após, determine e mostre o novo saldo.

saldo = float(input("Digite o seu Saldo: "))
print(f"{"*" * 20}Conta Bancaria{"*" * 20}")

print(f"Você tem R${saldo:.2f} na sua conta")

resposta = input("Você deseja Sacar ou Depositar? \nResposta: ")

if resposta.upper() == "SACAR":
    saque = float(input("Digite o quanto deseja sacar(-): "))
    print(f"Você retirou R${saque:.2f} \nSua conta possui agora: R${saldo - saque:.2f}!")

else:
    deposito = float(input("Digite quanto deseja depositar(+): "))
    print(f"Você adicionou R${deposito:.2f} \nSua conta possui agora: R${saldo + deposito:.2f}!")

    
