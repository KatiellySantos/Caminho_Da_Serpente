# Define o arquivo onde as tarefas serão armazenadas
arquivo = "tarefas.txt"
tarefas = []  # Lista para armazenar tarefas

# Carrega tarefas existentes do arquivo, caso haja alguma salva
with open(arquivo, "a+") as file:  # Abre o arquivo em modo adicionar e leitura
    file.seek(0)  # Move o cursor para o início do arquivo
    tarefas = [t.strip() for t in file.readlines()]  # Lê as tarefas e remove espaços extras

# Loop principal do programa
while True:
    print("Bloco de Tarefas 🚀")  # Exibe o título do programa
    menu = int(input("\n1. Inserir\n2. Remover\n3. Listar\n4. Sair\nEscolha: "))  # Menu de opções

    # Opção para adicionar uma nova tarefa
    if menu == 1:
        tarefa = input("Nova tarefa: ")  # Solicita a nova tarefa ao usuário
        tarefas.append(tarefa)  # Adiciona à lista
        with open(arquivo, "a") as file:  # Abre o arquivo em modo de escrita
            file.write(tarefa + "\n")  # Salva a nova tarefa no arquivo

    # Opção para remover uma tarefa existente
    elif menu == 2:
        if not tarefas:  # Verifica se há tarefas antes de tentar remover
            print("Sem itens para remover.")
        else:
            # Lista todas as tarefas com números para facilitar a escolha
            for indice, tarefa in enumerate(tarefas, 1):
                print(f"{indice}. {tarefa}")
            indice = int(input("Número da tarefa para remover: ")) - 1  # Obtém o número da tarefa

            # Verifica se o número inserido é válido antes de remover
            if 0 <= indice < len(tarefas):
                del tarefas[indice]  # Remove a tarefa da lista
                with open(arquivo, "w") as file:  # Abre o arquivo e sobrescreve as tarefas restantes
                    file.writelines([tarefa + "\n" for tarefa in tarefas])  # Atualiza o arquivo

    # Opção para listar todas as tarefas armazenadas
    elif menu == 3:
        print("\n".join(tarefas) if tarefas else "Lista sem tarefas.")  # Exibe as tarefas ou informa que está vazia

    # Opção para encerrar o programa
    elif menu == 4:
        break  # Finaliza o loop e encerra a execução
