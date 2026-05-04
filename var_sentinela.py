#Exemplo de Uso da Variavel Sentinela
while True:
    comando = input("Digite um comando: ")
    if comando == "sair":
        break
    print(f"Executado {comando}")