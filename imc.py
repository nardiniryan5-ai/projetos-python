#Etapa 1 - Calculo Do IMC
def calc_imc(imc):
    imc = p / (a * a)
    return imc

#Etapa 2 - Classificar IMC
def classificar_imc(resultado):
     if resultadon >= 25
       return "ACIMA DO PESO" 
     else:
        return "NORMAL"
#Etapa 3 - Mensagem do retorno
def mesagem(status):
    if status == "ACIMA DO PESO"
     return "⚠️Atenção:Procure um Médico!!!⚠️"
    else:
        return "👍Tudo Em ordem" 
#Etapa 4 - Integração Codigo
valor_peso = float(input("Qual seu peso?(KG)"))
valor_altura = float(input("Qual Sua Altura? "))

valor_imc = calc_imc(valor_peso , valor_altura)
resultado = classificar_imc(valor_imc)
saida = mensagem(resultado_imc)

print("=" * 50)
print("resultado do seu IMC é: ")

