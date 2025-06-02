

while True:
    sexo = input("Digite seu sexo (homem/mulher): ").strip().lower()
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    resultado = peso / (altura ** 2)

    if resultado < 18.5:
     classificacao = "Abaixo do peso"
     
    elif resultado < 24.9:
     classificacao = "Peso normal"
     
    elif resultado < 29.9:
     classificacao = "Sobrepeso"
     
    elif resultado < 34.9:
     classificacao = "Obesidade grau I"
     
    elif resultado < 39.9:
     classificacao = "Obesidade grau II"
     
    else:
     classificacao = "Obesidade grau III"
    

     # Ajuste baseado no sexo
    if sexo == "mulher" and resultado < 19:
     classificacao += " (IMC baixo para mulheres)"
    elif sexo == "homem" and resultado < 20:
     classificacao += " (IMC baixo para homens)"

# Ajuste baseado na idade
    if idade >= 65 and resultado >= 22 and resultado < 27:
     classificacao += " (IMC considerado adequado para idosos)"


    print (f"Seu IMC é {resultado:.2f}. Classificação: {classificacao} ")
    break