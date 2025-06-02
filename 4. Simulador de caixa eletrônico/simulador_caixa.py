cedulas = [200, 100, 50, 20, 10, 5, 2]  # Lista com os valores das cédulas disponíveis

# Tratamento de erros para entrada do usuário
while True:
    try:
        valor = int(input("Digite o valor do saque: ")) 
        if valor <= 0:  
            print("Erro: O valor deve ser positivo.") 
        else:
            break  
    except ValueError:  
        print("Erro: Digite um número válido.")  

# Percorre cada cédula disponível para calcular quantas serão usadas no saque
for nota in cedulas:
    quantidade, valor = divmod(valor, nota)  
    if quantidade > 0:  
        print(f"{quantidade} nota(s) de {nota}")  
