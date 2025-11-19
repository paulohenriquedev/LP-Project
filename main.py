import os
import json

def menu_usuario_logado(usuario): # exibe o menu para o usuário logado
    """
    O parâmetro 'usuario' é um dicionário: {'cpf': ..., 'senha': ..., 'nome': ..., 'saldo': ...}
    """
    while True:        
        usuario = obter_dados_usuario(usuario['cpf']) # Atualiza os dados do usuário a cada iteração
        nome = usuario['nome']
        
        print(f"\n-------- CONTA DE {nome.upper()} --------")
        print("1. Ver Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair da Conta")
        print("-----------------------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            ver_saldo(usuario)
        elif opcao == '2':
            depositar(usuario)
        elif opcao == '3':
            sacar(usuario)
        elif opcao == '4':
            print("\nDeslogando... Voltando ao menu principal.")
            break  # Sai do loop do menu do usuário, voltando para a função logar()
        else:
            print("\nOpção inválida! Tente novamente.")

def obter_dados_usuario(cpf):  #lê os dados do usuário a partir do cpf e retorna uma lista com os dados
    try:
        with open("usuarios/usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
            for usuario in usuarios:
                if usuario['cpf'] == cpf:
                    return usuario # Retorna o dicionário do usuário
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return None

"""
def ver_saldo(usuario):
   

def depositar(usuario):
    

def sacar(usuario):
"""

def atualizar_dados_usuario(cpf, novo_saldo):
    """Atualiza o saldo de um usuário específico no arquivo."""
    usuarios = []
    try:
        with open("usuarios/usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existe ou está vazio, não há o que atualizar.
        return

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario['saldo'] = novo_saldo
            break

    # Reescreve o arquivo inteiro com os dados atualizados
    with open("usuarios/usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=2)

def logar():
    """
    Função para lidar com o login do usuário.
    Verifica CPF e senha no arquivo de usuários.
    """
    print("\n----- Tela de Login -----")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")

    try:
        with open("usuarios/usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
            for usuario in usuarios:
                # Verifica se o CPF e a senha correspondem
                if usuario['cpf'] == cpf and usuario['senha'] == senha:
                    print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario['nome']}!")
                    menu_usuario_logado(usuario) # Chama o menu do usuário
                    return  # Sai da função logar após o sucesso
    except (FileNotFoundError, json.JSONDecodeError):
        print("\nNenhum usuário cadastrado no sistema.")

    print("\nCPF ou senha incorretos. Tente novamente.")
    input("Pressione Enter para voltar ao menu...")


def cadastrar():
    """Função para lidar com o cadastro de um novo usuário."""
    print("\n----- Tela de Cadastro -----")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    nome = input("Digite seu nome: ")
    
    usuarios = []
    try:
        # Tenta carregar os usuários existentes
        with open("usuarios/usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existe ou está vazio, a lista de usuários fica vazia
        pass

    # Verifica se o CPF já existe
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("\nErro: CPF já cadastrado!")
            input("Pressione Enter para voltar ao menu...")
            return

    # Adiciona o novo usuário (como um dicionário) à lista
    usuarios.append({
        "cpf": cpf,
        "senha": senha,
        "nome": nome,
        "saldo": 0.0
    })

    # Salva a lista inteira de volta no arquivo JSON
    with open("usuarios/usuarios.json", "w") as arquivo:
        # indent=2 formata o arquivo para ser mais legível
        json.dump(usuarios, arquivo, indent=2)

    print("\nUsuário cadastrado com sucesso!")
    input("Pressione Enter para voltar ao menu...")


def menu_principal():
   
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1. Logar")
        print("2. Cadastrar")
        print("3. Sair")
        print("============================")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            logar()
        elif opcao == '2':
            cadastrar()
        elif opcao == '3':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("\nOpção inválida! Por favor, tente novamente.")


if __name__ == "__main__":
    # Garante que o diretório 'usuarios' exista ao iniciar
    if not os.path.exists("usuarios"):
        os.makedirs("usuarios")
    menu_principal()