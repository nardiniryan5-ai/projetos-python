#Módulo 1: Lógica Matemática
#Responsável: Pedro Henryke da Costa Gomes
def calcular_imc(p, a):
    imc = p / (a ** a)
    return imc

#Módulo 2: Classificação de Dados
#Responsável: Rafael Henrique Trajano
def classificar(valor_imc):
    if valor_imc <25:
        return "Saudável ✅"
    else:
        return "Acima do peso 🚫"
#Módulo 3: Especialista em Conteúdo
#Responsável: Brayan De Santana Da Silva
def gerar_aviso(status):
    if status == "Saudável ✅":
        return "Dica: Continue mantendo hábitos saudáveis, como uma dieta equilibrada e exercícios regulares!"
    else:
        return "Dica: Inclua caminhadas na sua rotina e foque em alimentos ricos em fibras. Pequenas mudanças fazem grande diferença!"

#Módulo 4:Engenheiro de Integração
#Responsável: Ryan Nardini Pereira
p = float(input("Qual o Seu Peso atual?(Kg) "))
a = float(input("Qual sua altura atual? "))
 
imc = calcular_imc(p, a)
print(f"Seu IMC é: {imc:.2f}")
classificar(imc)
gerar_aviso(imc)