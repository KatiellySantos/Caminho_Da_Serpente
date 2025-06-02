import time  # Importa a biblioteca time para controlar o tempo e pausas na execução

# Solicita ao usuário o tempo desejado para o cronômetro
segundos = int(input("Defina o tempo do cronômetro (em segundos): "))

# Inicia a contagem regressiva, começando pelo número de segundos informado
for contagem in range(segundos, 0, -1):  # Loop que percorre de 'segundos' até 1, diminuindo a cada repetição
    print(f"⏳ {contagem} segundos restantes...", end="\r")  # Exibe a contagem na mesma linha (com \r)
    time.sleep(1)  # Pausa a execução por 1 segundo antes de continuar a contagem

# Exibe a mensagem final quando o tempo se esgota
print("\n⏰ Tempo esgotado!")
