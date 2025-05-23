# 18.Uma rainha requisitou os serviços de um monge e disse-lhe que pagaria qualquer preço. O monge, necessitando de alimentos, perguntou à rainha se o pagamento poderia ser feito com grãos de trigo dispostos em um tabuleiro de xadrez, de tal forma que o primeiro quadro contivesse apenas um grão e os quadros subsequentes, o dobro do quadro anterior. A rainha considerou o pagamento barato e pediu que o serviço fosse executado, sem se dar conta de que seria impossível efetuar o pagamento. Escreva um algoritmo que calcule o número de grãos que o monge esperava receber.

graos = 0


for i in range(64):
    
    graos += 2 ** i

print(graos)