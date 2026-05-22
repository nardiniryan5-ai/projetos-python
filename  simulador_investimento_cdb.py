#---Simulador De Investimentos-----

invest_inicio = float(input("Quanto deseja investir? "))
meses = int(input("Por quantos Meses? "))

cdb = 1.09 / 100 
final = invest_inicio

for i in range(1, meses + 1):
 final = final * (1 + cdb)
 print(f"mes {i}:R$ {final: .2f}")

print(f"O valor do Retorno Sera de : {final:.2f}")

#-----Ryan Nardini Pereira----
