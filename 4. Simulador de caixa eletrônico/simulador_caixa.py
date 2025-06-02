cedulas = [200, 100, 50, 20, 10, 5, 2]  # Lista com os valores das cédulas disponíveis

# Tratamento de erros para entrada do usuário
while True:
    try:
        valor = int(input("Digite o valor do saque: "))  # Solicita o valor do saque e converte para inteiro
        if valor <= 0:  
            print("Erro: O valor deve ser positivo.")  # Garante que o valor inserido seja maior que zero
        else:
            break  # Sai do loop quando um valor válido é inserido
    except ValueError:  
        print("Erro: Digite um número válido.")  # Captura erro se o usuário digitar algo que não seja um número inteiro

# Percorre cada cédula disponível para calcular quantas serão usadas no saque
for nota in cedulas:
    quantidade, valor = divmod(valor, nota)  # Divide o valor total pelas cédulas (divmod retorna quociente e resto)
    if quantidade > 0:  
        print(f"{quantidade} nota(s) de {nota}")  # Exibe quantas notas de cada valor serão utilizadas
