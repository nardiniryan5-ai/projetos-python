def calcular_imc(p, a):
  imc = p / (a ** 2)
  return imc
def classificar(imc):
  if imc >25:
    print("normal")
  else:
    print("Acima do peso")
def gerar_aviso(status):
  if imc <25:
   print("Exercícios regulares:")
  else:
    print("Acompanhamento Especializado \n Índice de Massa Corporal (IMC) é apenas uma medida geral e não avalia a sua composição corporal (porcentagem de gordura vs. massa muscular)")
p = float(input("Qual o Seu Peso atual? "))
a = float(input("Qual sua altura atual? "))
 
imc = calcular_imc(p, a)
print(f"Seu IMC é: {imc:.2f}")
classificar(imc)
gerar_aviso(imc) 