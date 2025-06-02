import time  # Importa a biblioteca time para controlar o tempo e pausas na execução

# Solicita ao usuário o tempo desejado para o cronômetro
segundos = int(input("Defina o tempo do cronômetro (em segundos): "))

# Inicia a contagem regressiva, começando pelo número de segundos informado
for contagem in range(segundos, 0, -1):  
    print(f"⏳ {contagem} segundos restantes...", end="\r")  
    time.sleep(1)  

# Exibe a mensagem final quando o tempo se esgota
print("\n⏰ Tempo esgotado!")
