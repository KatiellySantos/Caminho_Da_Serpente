# Define o arquivo onde as tarefas serão armazenadas
arquivo = "tarefas.txt"
tarefas = []  

# Carrega tarefas existentes do arquivo, caso haja alguma salva
with open(arquivo, "a+") as file:  
    file.seek(0)
    tarefas = [t.strip() for t in file.readlines()]

# Loop principal do programa
while True:
    print("Bloco de Tarefas 🚀")  # Exibe o título do programa
    menu = int(input("\n1. Inserir\n2. Remover\n3. Listar\n4. Sair\nEscolha: "))  # Menu de opções

    # Opção para adicionar uma nova tarefa
    if menu == 1:
        tarefa = input("Nova tarefa: ")  
        tarefas.append(tarefa)  
        with open(arquivo, "a") as file: 
            file.write(tarefa + "\n")  

    # Opção para remover uma tarefa existente
    elif menu == 2:
        if not tarefas:  # Verifica se há tarefas antes de tentar remover
            print("Sem itens para remover.")
        else:
            for indice, tarefa in enumerate(tarefas, 1):
                print(f"{indice}. {tarefa}")
            indice = int(input("Número da tarefa para remover: ")) - 1  # Obtém o número da tarefa

            # Verifica se o número inserido é válido antes de remover
            if 0 <= indice < len(tarefas):
                del tarefas[indice]  # Remove a tarefa da lista
                with open(arquivo, "w") as file:  
                    file.writelines([tarefa + "\n" for tarefa in tarefas])  

    # Opção para listar todas as tarefas armazenadas
    elif menu == 3:
        print("\n".join(tarefas) if tarefas else "Lista sem tarefas.") 

    # Opção para encerrar o programa
    elif menu == 4:
        break  # Finaliza o loop e encerra a execução
