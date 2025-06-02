import random  # Importa o módulo 'random' para gerar números aleatórios

while True:  # Loop infinito até que o jogador decida parar
    input("Pressione ENTER para rolar o dado...")  
    
    dado = random.randint(1, 6)  
    print(f"Você rolou: {dado}")  

    continuar = input("Deseja rolar novamente? (s/n): ").lower()  
    if continuar != "s":  
        print("Fim do jogo! Obrigado por jogar. 🎲")  
        break  
    
