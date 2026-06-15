# Etapa 1 - Calculo Do IMC
def calc_imc(p, a):
    imc = p / (a * a)
    return imc

# Etapa 2 - Classificar IMC
def classificar_imc(resultado):
    if resultado >= 25:
        return "ACIMA DO PESO"
    else:
        return "NORMAL"

# Etapa 3 - Mensagem do retorno
def mensagem(status):
    if status == "ACIMA DO PESO":
        return "⚠️ Atenção: procure um médico!!! ⚠️"
    else:
        return "👍 Tudo em ordem"

# Etapa 4 - Integração Codigo
valor_peso = float(input("Qual seu peso? (KG): "))
valor_altura = float(input("Qual sua altura? (m): "))

valor_imc = calc_imc(valor_peso, valor_altura)
resultado = classificar_imc(valor_imc)
saida = mensagem(resultado)

print("=" * 50)
print(f"\nResultado do seu IMC é: {valor_imc:.2f}")
print(f"\nClassificação: {resultado}")
print(saida)

