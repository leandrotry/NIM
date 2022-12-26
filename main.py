def computador_escolhe_jogada(n, m):  #FUNÇÃO QUE EXECUTA AS JOGADAS DO COMPUTADOR
    computador_retira = 1

        # N restante == multiplo de (m+1) 
    while computador_retira != m:
        if (n - computador_retira) % (m + 1) == 0:
            return computador_retira
        else:
            computador_retira += 1
    return computador_retira


#----------------------------------------------------------------------------------#


def usuario_escolhe_jogada(n, m):
    while True:
        jogador_remove_peca = int(input('Quantas peças você vai retirar?'))
        if jogador_remove_peca > m or jogador_remove_peca < 1:

            print("jogada inválida")
        else:
            break
    return jogador_remove_peca


#----------------------------------------------------------------------------------#


def campeonato():
    rodada = 1
    while rodada <= 3:
        print(f'Rodada: {rodada}')
        partida()
        rodada +=1
        
    print("Placar: Você 0 X 3 Computador")


#----------------------------------------------------------------------------------#

def partida(): 
    vez_do_pc = False
    while True:
        try:        
            n = int(input('Digite a quantidade de peças'))
            m = int(input('Limite de peças por jogada'))
        except ValueError:
            print('selecionado tipo inválido')
        if n >= m:
            break
        elif n < m:
            print('ERRO!')
            print('Quantidade de peças inválidas. A quantidade de peças não pode ser menor que o limite de peças por jogada.')
            continue

    if n == (n % m+1 == 0):
        print('Jogador Inicia')
    else:
        print('Computador inicia') 
        vez_do_pc = True


    while n > 0:
        if vez_do_pc:
            pc_remove = computador_escolhe_jogada(n, m)
            n = n - pc_remove
            
            if pc_remove == 1:
                print('O computador retirou uma peça')
                print()
            else:
                print(f'O computador retirou {pc_remove}')
            vez_do_pc = False
        
        else:
            jogador_remove = usuario_escolhe_jogada(n, m) 
            n = n - jogador_remove
            if jogador_remove == 1:
                print('Você tirou 1 peça')
            else:
                print(f'Você tirou {jogador_remove}')
            vez_do_pc = True
        
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')

tipoDePartida = int(input('2 - para jogar um campeonato '))

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
elif tipoDePartida == 1:
    print()
    partida()
#----------------------------------------------------------------------------------#
