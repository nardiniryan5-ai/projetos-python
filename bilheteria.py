def formatar(nome):
    return nome.upper()
def verificador(idade):
    if idade >= 18:
     return "Aprovado"
    else:
       return "Negado"
def gerar_mensagem(status):
   if status == "Autorizado":
    return "Tenha uma otima Sessão"
   else:
      return"Sinto Muito, Idade Negada"
nome_filme = input("Digite o nome do filme: ")
idade_filme = int(input("Digite sua Idade:"))

filme = formatar(nome)
status_filme = verificador(idade)
mensagem = gerar_mensagem(status)