def contador (frase):
    frase = frase.lower().replace(",", "").replace(".", "")  # Normaliza a string
    palavras = frase.split()
    return len(palavras)

resultado = input ("Digite a frase:\n")

print(f"A Frase contém {contador(resultado)} palavras.")