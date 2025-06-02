import string  # Importa o módulo 'string' para acessar caracteres alfabéticos e numéricos
import random  # Importa 'random' para gerar valores aleatórios

# Define os conjuntos de caracteres que podem ser usados na senha
letras = string.ascii_letters  
numeros = string.digits  
simbolos = "!@#$%^&*()"  

# Solicita o tamanho da senha ao usuário
senha = int(input("Defina a quantidade de caracteres para a senha: "))

# Verifica se o tamanho inserido é válido
if senha > 0:
    senha_gerada = "".join(random.choices(letras + numeros + simbolos, k=senha))  # Gera a senha aleatória
    print("Senha gerada:", senha_gerada)  
else:
    print("Erro: O tamanho da senha deve ser maior que 0.")  
