def partida():
    while True:
        try:        
            n = int(input('Digite a quantidade de peças'))
            m = int(input('Limite de peças por jogada'))
        except ValueError:
            print('selecionado tipo inválido')
        if n > m:
            break
        else:
            continue
    escolhe_primeiro_jogador(n, m)

def escolhe_primeiro_jogador(n, m):
    if (n % (m + 1)) == 0:
        print('Jogador Inicia')
    else:
        print('Computador inicia')



partida()
