# 1 - Configuração Inicial: Importa a biblioteca 'random' e define variáveis do jogo
import random  # Importa a biblioteca para gerar números aleatórios
numerosecreto = random.randint(1, 20) 
tentativas = 0  
limitetentativas = 5  

# 2 - Loop de tentativas: Permite ao jogador tentar adivinhar o número até o limite
while tentativas < limitetentativas:  
    palpite = int(input("Escolha um número de 1 a 20: "))  
    tentativas += 1  

    if palpite < numerosecreto:  # Se o palpite for menor que o número secreto
        print("Chute um número maior.")  
    elif palpite > numerosecreto:  # Se o palpite for maior que o número secreto
        print("Chute um número menor.")  
    else:  # Se o palpite for igual ao número secreto
        print(f"Parabéns! Você acertou o número secreto ({numerosecreto}) em {tentativas} tentativas.")  
        break  

# Se o jogador atingir o limite de tentativas sem acertar, exibe uma mensagem final
if tentativas == limitetentativas:  # Verifica se o jogador usou todas as tentativas sem acertar
    print(f"Game over! O número secreto era {numerosecreto}.")
