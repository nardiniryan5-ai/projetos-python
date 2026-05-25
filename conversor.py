def converte(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("Conversor Dolar x Real")
preco = float(input("Digite o valor do produto em Dolar:"))
resultado = converte(preco)
print(f"O valor em reais é:{resultado: .2f}")