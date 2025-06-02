import random  # Importa o módulo 'random' para gerar números aleatórios

while True:  # Loop infinito até que o jogador decida parar
    input("Pressione ENTER para rolar o dado...")  # Aguarda o jogador pressionar ENTER para continuar
    
    dado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6, simulando a rolagem de um dado
    print(f"Você rolou: {dado}")  # Exibe o resultado da rolagem do dado

    continuar = input("Deseja rolar novamente? (s/n): ").lower()  # Pergunta se o jogador quer continuar e converte resposta para minúsculas
    if continuar != "s":  # Se a resposta for diferente de 's', o jogo termina
        print("Fim do jogo! Obrigado por jogar. 🎲")  # Mensagem final ao encerrar o jogo
        break  # Interrompe o loop e finaliza a execução
    