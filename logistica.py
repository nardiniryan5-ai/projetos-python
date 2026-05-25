def calcular_frete(peso):
    if peso <= 20:
        valorporkm = 10
    else:
        valorporkm = 15
    valor_frete = valorporkm * peso
    return valor_frete
peso_item = float(input("Digite o Peso do Item em kg: "))
frete = calcular_frete(peso_item)
print(f"O valor do frete é: R${frete:.2f}")
    