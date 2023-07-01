# Jogo do Galo

import tkinter as tk
from tkinter import messagebox

# Criar a janela
janela = tk.Tk()
janela.title("Jogo do Galo")
janela.geometry("300x320")

# Criar tabuleiro, inicializar jogador

tabuleiro = [["" for _ in range(3)] for _ in range(3)]
# A variável é "_" porque em Python é costume usar-se este nome para variáveis de vida muito curta, dispensáveis
# print(tabuleiro) >> Para ver o resultado, que é um tabuleiro 3x3, sem nada em cada posição

# Indico que o primeiro jogador é o X
jogador = "X"

#Inicializo o valor dos botões
botoes = []

#Inicializo a contagem das jogadas
jogada_n = 1

def verificar_vitoria():
    """ # Serve para documentar a função
        ## Formatando a documentação
        ### Em vários níveis
        #### Experimentem passar por cima do nome da função sem clicar"""
        
    # Crio uma função para verificar se já houve vitória ou não. Poderia estar no meio do código principal, mas assim fica mais limpo.
    
    # Verifico se alguma das linhas ou alguma das colunas têm já 3 elementos iguais diferentes de "" (o símbolo != quer dizer "diferente de" e é para imitar o sinal de desigualdade matemática, com um traço a riscar o igual)
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != "":
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != "":
            return True
    
    # Verifico se as diagonais têm já 3 elementos iguais diferentes de ""
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
        return True
    
    # Se não se verificar nenhuma das condições, devolve falso e o jogo continua
    return False

# jogada

# Esta função é especial porque vai estar associada a cada botão

def jogada(ln, col, jogador):
    
    """ # Serve para documentar a função
        ## Formatando a documentação
        ### Em vários níveis
        #### Experimentem passar por cima do nome da função sem clicar"""
            
    # Usei esta variável, mas como é criada dentro da função e a quero usar fora, tive de a declarar como "global"
    global jogada_n
    
    # Verifico se a jogada é par ou ímpar, para decidir de quem é a vez de jogar (X, ímpar, O, par)
    if jogada_n%2 == 0:
        print(jogada_n)
        jogador = "O"
    else:
        print(jogada_n)
        jogador = "X"
    
    # Conforme a jogada tem determinadas coordenadas, vou definir que aí escrevo o símbolo do jogador atual    
    botoes[ln][col].config(text=jogador)
    # Insiro esse valor no tabuleiro virtual, para verificar a vitória
    tabuleiro[ln][col]= jogador
    # Aumento a jogada (se estava na jogada 2, passa a 3)
    jogada_n += 1
    
    #Chamo a função de verificação de vitória
    if verificar_vitoria():
        # Se ganhou, digo que ganhou.
        messagebox.showinfo("Resultado", "Ganhou!")
        # Se acabou, fecho a janela (um nome é um pouco dramático...)
        janela.destroy()
    elif jogada_n == 10:
        # Se já se jogou tudo (a 10ª jogada não pode ser possível) e ninguém ganhou, então houve empate.
        messagebox.showinfo("Resultado", "Empataram. É o resultado esperado de dois jogadores inteligentes. Parabéns aos dois!")
        # Se acabou, fecho a janela (um nome é um pouco dramático...)
        janela.destroy()

    return

# Criação dos botões do tabuleiro

# Aqui crio um duplo loop linha e coluna para criar o tabuleiro

for linha in range(3):
    # Aqui crio uma lista para a linha que vou construir 
    botao_linha = []
    
    # Vou correr as colunas para a linha que criei    
    for coluna in range(3):
        
        # Esta é a chave do jogo, em que, para cada botão, vou definir o sítio, a "janela", o texto, neste caso vazio, a largura e a altura
        # Mas também crio uma função que eu defino como tendo dois parâmetros, ln e col, associando a eles os valores de linha e coluna, que depois vão estar associados aos botões através da grid.
        # Esta função é invocada pelo clique do botão, faz parte do widget
        botao = tk.Button(janela, text="", width=10, height=5,command=lambda ln=linha,col=coluna: jogada(ln, col,jogador))
        
        # Esta grid permite-me posicionar widgets, neste caso os botões, numa determinada ordem (row/column), com determinado espaçamento (padx, pady).
        botao.grid(row=linha, column=coluna, ipadx= 5, ipady=5, padx=5, pady=5)
        
        # Preencho a lista com os botões criados, 3 de cada vez, correspondendo às colunas
        botao_linha.append(botao)
    
    # Preencho a lista de botões com as linhas, à medida que as for criando, no total 3 linhas, cada uma com 3 botões, só vai servir para desenhar "X" e "O" nos botões, a partir das coordenadas.   
    botoes.append(botao_linha)

# Antes de fazer o código, pensámos um pouco na lógica, para não irmos à toa.

# Criar um loop while de 9 jogadas
    # criar um data_frame 3*3
    # Jogada par-impar
        # Mudar o botão para X quando é ímp
    # confirmação das linhas feitas (alto, largo, diagonal)
    # condição que pare o jogo quando é ganho e dê uma mensagem de parabéns, caso contrário continua
# Se ninguém ganhar, dá uma mensagem a dizer que há empate
# Pode perguntar se quer jogar outra vez

# Isto inicializa a janela e mostra-a no écran. É aquilo que o "destroy" termina.
janela.mainloop()