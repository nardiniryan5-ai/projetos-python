#Contador de Carácteres - Achando a maior palavra
def maior_palavra(texto):
    for p in ", ! ? . ; : ":
        texto = texto.replace(p, "")
    palavra = texto.split()
    if not palavra:
        return " "
    tamanho = ""
    for frase in palavra:
        if len(frase) >= len(tamanho):
            tamanho = frase
    return tamanho

print(maior_palavra("texto reflexão"))