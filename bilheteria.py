def formatar(nome):
    return nome.upper()

def verificador(idade):
    if idade >= 18:
        return "Aprovado"
    else:
        return "Negado"

def gerar_mensagem(status):
    if status == "Aprovado":
        return "Tenha uma ótima sessão"
    else:
        return "Sinto muito, idade negada"

nome_filme = input("Digite o nome do filme: ")
idade_filme = int(input("Digite sua idade: "))

filme = formatar(nome_filme)
status_filme = verificador(idade_filme)
mensagem = gerar_mensagem(status_filme)

print(f"Filme: {filme}")
print(f"Status: {status_filme}")
print(f"Aviso: {mensagem}")