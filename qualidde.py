def cabecalho():
    print("=" * 30)
    print("Sistema de Qualidade")
def  verificar_status(peso):
    if peso >= 50 and peso <= 100:
     return"Aprovado"
    else:
       return "Reprovado"
cabecalho()
peso_item = float(input("Digite o Peso do Item em gramas: "))
status = verificar_status(peso_item)
print(f"resultado da inpeçao:{status}")
print("=" * 30)

arquivo = open(codigos)