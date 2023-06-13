# Forca - v1.0

# Importar a biblioteca para geração de números aleatórios

import random

# Definir uma função para criar o boneco

def Forca(erros):
    Body_parts = ["  |","  O"," \|/","  |"," / \\"]
    for i in range(erros+1):
        print(Body_parts[i])

# Definir função para tratar correção do input

def Input_correto(carater):
    if carater.isalpha() and len(carater)==1:
        return True
    else:
        return False

# Inicializar variáveis

palavras = ["Fado", "Alfama", "Colombo", "Tejo", "Terramotos", "Docas"]
escolha = palavras[random.randint(0,len(palavras)-1)]
palavra_secreta = escolha.lower()

letras_acertadas = ["_"] * len(palavra_secreta)
tentativa = 0
max_tentativas = 5
letras_erradas = []

# Jogo com 5 tentativas (<6)

while tentativa <max_tentativas+1:
    
    if tentativa == max_tentativas-1:
        Print("É agora ou nunca, tem de acertar!")
    else:
        print("Ainda tem "+str(max_tentativas-1-tentativa)+" oportunidades de falhar.")

    # Mecanismo de tentativas

    print("\n")
    print("\nPalavra: " + " ".join(letras_acertadas))
    print("\n")
    print("Letras que não estão na palavra: " + ", ".join(letras_erradas))
    print("\n")
    letra = input("Digite uma letra: ").lower()

    # Verifico se está ou não ok o input

    if Input_correto(letra):
        
        # Se for repetido, certo ou errado, avisa, mas nada altera.

        if letra in letras_erradas or letra in letras_acertadas:
            print("Você já tentou essa letra. Tente novamente.")
        # Se não for repetido, verifica se a letra existe na palavra secreta - se existir, insere na lista das que se mostra
        elif letra in palavra_secreta:
             for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_acertadas[i] = letra

        # Se não for repetida e não estiver na palavra secreta, então é um erro

        else:
            # Sendo um erro, vai para a lista das erradas
            letras_erradas.append(letra)
            # Desenha a forca
            Forca(tentativa)
            # Gasta mais uma tentativa
            tentativa += 1
        
        # Caso já não haja "_" dentro das letras_acertadas, então já descobrimos a palavra e vencemos o jogo

        if "_" not in letras_acertadas:
            print("\n")
            print("Parabéns! Você venceu com " + str(len(letras_erradas))+" erros. A palavra era: " + escolha)
            break
        elif tentativa == max_tentativas:
            print("\nGame over! Você perdeu. A palavra era: " + escolha)
            break

    # Caso o input não esteja correto, avisa.

    else:
        print("Entrada inválida. Digite apenas letras e apenas uma.")