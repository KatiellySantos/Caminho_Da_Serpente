# 1 - Configuração Inicial: Importa a biblioteca 'random' e define variáveis do jogo
import random  # Importa a biblioteca para gerar números aleatórios
numerosecreto = random.randint(1, 20)  # Escolhe um número aleatório entre 1 e 20
tentativas = 0  # Inicializa o contador de tentativas
limitetentativas = 5  # Define o número máximo de tentativas permitidas

# 2 - Loop de tentativas: Permite ao jogador tentar adivinhar o número até o limite
while tentativas < limitetentativas:  # O loop continua enquanto o número de tentativas for menor que o limite
    palpite = int(input("Escolha um número de 1 a 20: "))  # Solicita um número ao usuário e converte para inteiro
    tentativas += 1  # Incrementa o número de tentativas a cada rodada

    if palpite < numerosecreto:  # Se o palpite for menor que o número secreto
        print("Chute um número maior.")  # Indica que o número secreto é maior
    elif palpite > numerosecreto:  # Se o palpite for maior que o número secreto
        print("Chute um número menor.")  # Indica que o número secreto é menor
    else:  # Se o palpite for igual ao número secreto
        print(f"Parabéns! Você acertou o número secreto ({numerosecreto}) em {tentativas} tentativas.")  
        break  # Finaliza o jogo ao acertar

# Se o jogador atingir o limite de tentativas sem acertar, exibe uma mensagem final
if tentativas == limitetentativas:  # Verifica se o jogador usou todas as tentativas sem acertar
    print(f"Game over! O número secreto era {numerosecreto}.")
