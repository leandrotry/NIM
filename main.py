def computador_escolhe_jogada(n, m):  #FUNÇÃO QUE EXECUTA AS JOGADAS DO COMPUTADOR
    computador_retira = 1

        # N restante == multiplo de (m+1) 
    while computador_retira != m:
        if (n - computador_retira) % (m + 1) == 0:
            return computador_retira
        else:
            computador_retira += 1
    return computador_retira


def jogador_escolhe_jogada(n, m):
    while True:
        jogador_remove_peca = int(input('Quantas peças você vai retirar?'))
        if jogador_remove_peca > m or jogador_remove_peca < 1:

            print("jogada inválida")
        else:
            break
    return jogador_remove_peca


def campeonato():
    rodada = 1
    while rodada <= 3:
        print(f'Rodada: {rodada}')
        rodada +=1
    



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
    if n % (m + 1) == 0:
        print('Jogador Inicia')
        computador_escolhe_jogada(n,m)
    else:
        print('Computador inicia')



partida()
