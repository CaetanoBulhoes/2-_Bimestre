# 19.Um marciano chegou a uma floresta e se escondeu atrás de uma das 100 árvores quando viu um caçador. O caçador só tinha cinco balas em sua espingarda. Cada vez que ele atirava, e não acertava, é claro, o marciano dizia: estou mais à direita ou estou mais à esquerda. Se o caçador não conseguir acertar o marciano, ele será levado para Marte. Escreva um algoritmo para este jogo, com dois jogadores, onde um escolhe a árvore em que o marciano irá se esconder, e o outro tenta acertar.

print(f"{"*" * 50}\nVamos jogar um jogo em que uma pessoa é o Alien tentando \nse esconder, enquanto o outro é um caçador tentando acertar o Alien.\n\nRegras:\nO primeiro jogador irá escolhar um número entre 1 a 100 que representam as respectivas\narvóres que o Alien irá se esconder.\nEm seguida, o outro jogador terá 5 tentativas para acertar a arvóre que está o Alien\ncaso erre todas, será abduzido pelo Alien, assim perdendo o jogo, caso o contrário, o Alien perde.\n")

chances = 6

for i in range(10):
    arvore = int(input("Escolha uma árvore de 1 a 100\nEscolha:"))
    if arvore < 0 or arvore > 100:
        print("Essa arvóre não existe, se esconda em outra")

    else:
        
        break

for i in range(10):
    chances -= 1
    tiro = int(input(f"\nEscolha uma arvóre\n<-Esquerda 1 ... 100 Direita->\nVocê tem {chances} chances\nEscolha:"))

    if tiro > arvore:
        print("Mais para a esquerda!")
        
    elif tiro < arvore:
        print("Mais para a direita!")

    else:
        print("Você conseguiu capturar o Alien. Vitória do Caçador!")
        break
    for r in range(1):

        if tiro < 0 or tiro > 100:
            print("Você atirou no nada, perdeu uma chance!")

chances -= 1
if chances == 0:
    print("Suas balas acabaram e você foi abduzido. Vitória do Alien!")
 
