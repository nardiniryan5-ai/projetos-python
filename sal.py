#---Simulador De Investimentos-----

invest_inicio = float(input("Quanto deseja investir? "))
meses = int(input("Por quantos Meses? "))

cdb = 1.09 / 100 
final = 0  # Começa com zero para o primeiro mês não duplicar

for i in range(1, meses + 1):
    # 1. Primeiro coloca o dinheiro do mês (R$ 100)
    final = final + invest_inicio
    
    # 2. Depois calcula o rendimento do CDB sobre esse valor
    final = final * (1 + cdb)
    
    print(f"mes {i}: R$ {final:.2f}")

print(f"O valor do Retorno Sera de : {final:.2f}")

#-----Ryan Nardini Pereira----