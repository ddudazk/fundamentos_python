#autor: Eduarda michele

usuario = input("Digite o nome do usuário: ")
senha = input("Digite sua senha: ")

if usuario == "admin" and senha == "1234": 
    print("Acesso permitido!")
else:
    print("Acesso negado!")