def palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")  # Normaliza a string
    return texto == texto[::-1]  # Compara com a versão invertida

frase = input("Favor insira a palavra ou texto:\n")

if palindromo(frase):
    print("É um palíndromo! (Lido da mesma forma de trás para frente)")
else:
    print("Não é um palíndromo.")
