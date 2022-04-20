# Printa o tabuleiro
def visualiza_tabuleiro(tabuleiro):
    str = '\n'
    for indice, linha in enumerate(tabuleiro):
        str += f'{linha[0]}|{linha[1]}|{linha[2]}\n'
        if indice < len(tabuleiro) - 1:
            str += '-----\n'
    return str


# Recebe o movimento do player, verifica seus parametros e retorna a posicao do movimento.
def jogada_do_player(tabuleiro):
    escolha_permitida = False
    
    while escolha_permitida == False:
        escolha = input('Faça sua jogada: ')

        # Escolha deve estar entre 1~9 e ser um número inteiro.
        if escolha.isdigit():
            if (1<= int(escolha) <= 9):
                escolha = int(escolha)
                
                # Verifica se a posicao do movimento é válida.
                if verifica_posicao(escolha, tabuleiro):
                    print('Posicao ocupada.')
                else:
                    return escolha

            else:
                print('Escolha inválida. Deve ser um número entre 1~9.')
        else:
            print('Escolha inválida. Deve ser um número inteiro.')


# verifica se a posicao do movimento é válida.
def verifica_posicao(escolha, tabuleiro):
    linha = (escolha - 1) // 3
    coluna = (escolha - 1) % 3
    
    if (tabuleiro[linha][coluna] == 'X') or (tabuleiro[linha][coluna] == 'O'):
        return True
    else:
        return False


# Realiza o movimento.
def realiza_movimento(escolha, tabuleiro, peca):
    linha = (escolha - 1) // 3
    coluna = (escolha - 1) % 3

    tabuleiro[linha][coluna] = peca


# Verifica se houve vitoria ou deu velha.
def verifica_vitoria(tabuleiro, peca):
    # Velha
    casas = list(range(9))
    for linha in tabuleiro:
        for i in range(3):
            if (linha[i] == 'X' or linha[i] == 'O'):
                casas.pop()
    if len(casas) == 0:
        print(f'Fim de jogo. Deu velha.')
        return True
    # Vitoria na horizontal
    for linha in tabuleiro:
        if ((linha[0] == linha[1]) and (linha[1] == linha [2]) and (linha[0] == peca)):
            print(f'Fim de jogo. O jogador de "{peca}" ganhou. vitoria horizontal.')
            return True
    # Vitoria na vertical
    for coluna in range(len(tabuleiro)):
        if ((tabuleiro[0][coluna] == tabuleiro[1][coluna]) and (tabuleiro[1][coluna] == tabuleiro[2][coluna]) and (tabuleiro[0][coluna] == peca)):
            print(f'Fim de jogo. O jogador "{peca}" ganhou. vitoria vertical')
            return True
    # Vitoria na diagonal
    peca_meio = tabuleiro[1][1]
    diag1 = True
    diag2 = True
    if peca_meio in ['X','O']:
        peca_meio = set(tabuleiro[1][1])
        coluna = len(tabuleiro) - 1

        for i in range(len(tabuleiro)):
            tab_peca = tabuleiro[i][i]
            peca_meio.add(tab_peca)
            if len(peca_meio) > 1:
                peca_meio.pop()
                diag1 = False
                break
        for i in range(len(tabuleiro)):
            tab_peca = tabuleiro[i][coluna]
            peca_meio.add(tab_peca)
            if len(peca_meio) > 1:
                peca_meio.pop()
                diag2 = False
                break
            coluna -= 1
        if len(peca_meio) == 1 and diag1 == True or diag2 == True:
            print(f'Fim de jogo. O jogador "{peca}" ganhou. vitoria diagonal.')
            return True
    
    return False


# Inicializa o jogo
def jogo_da_velha():
    keep_playing = True
    game_over = False
    turno = 'player1'
    while keep_playing == True:
        row1 = [' ',' ',' ']
        row2 = [' ',' ',' ']
        row3 = [' ',' ',' ']

        tabuleiro = [row1,row2,row3]
        print(visualiza_tabuleiro(tabuleiro))
        while game_over == False:
            
            if turno == 'player1':
                peca = 'X'
                turno = 'player2'
            else:
                peca = 'O'
                turno = 'player1'
            
            escolha = jogada_do_player(tabuleiro)
            realiza_movimento(escolha, tabuleiro, peca)
            print(visualiza_tabuleiro(tabuleiro))
            resultado = verifica_vitoria(tabuleiro, peca)
            if resultado:
                game_over = True
        while True:
            jogar = input('Quer continuar jogando? [Y/N] ').upper()
            if jogar == 'Y':
                game_over = False
                break
            elif jogar == 'N':
                keep_playing = False
                break
            else:
                print('opcao invalida.')

jogo_da_velha()