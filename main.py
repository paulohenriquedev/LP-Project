def menu_usuario_logado(usuario):  # exibe o menu para o usuário logado
    """
    O parâmetro 'usuario' é um dicionário: {'cpf': ..., 'senha': ..., 'nome': ..., 'saldo': ...}
    """
    while True:
        usuario = obter_dados_usuario(usuario['cpf'])  # Atualiza os dados do usuário a cada iteração
        nome = usuario['nome']

        print(f"\n-------- CONTA DE {nome.upper()} --------")
        print("1. Ver Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair da Conta")
        print("-----------------------------------------")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                ver_saldo(usuario)
            case '2':
                depositar(usuario)
            case '3':
                sacar(usuario)
            case '4':
                print("\nDeslogando... Voltando ao menu principal.")
                break  # Sai do loop do menu do usuário, voltando para a função logar()
            case _:
                print("\nOpção inválida! Tente novamente.")


def obter_dados_usuario(cpf):  # lê os dados do usuário a partir do cpf e retorna uma lista com os dados
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split('|') #Remove quebras de linha e separa por '|'
                if len(dados) == 4:
                    cpf_arquivo = dados[0]
                    if cpf_arquivo == cpf:
                        return {
                            'cpf': dados[0],
                            'senha': dados[1],
                            'nome': dados[2],
                            'saldo': float(dados[3])
                        }
    except FileNotFoundError:
        return None
    return None


def ver_saldo(usuario):
    saldo = usuario['saldo']
    print(f"\nSeu saldo atual é: R${saldo:.2f}.")  # Exibe o saldo atual formatado com 2 casas decimais
    input("Pressione Enter para continuar...")


def depositar(usuario):
    print("\n--- Depósito ---")
    try:
        valor = float(input("Quanto deseja depositar? (Em R$) "))
        if valor > 0:
            novo_saldo = usuario['saldo'] + valor  # Atualiza o saldo com o valor do déposito realizado

            atualizar_dados_usuario(usuario['cpf'], novo_saldo)  # Atualiza o saldo no arquivo
            print(f"Sucesso! R$ {valor:.2f} depositado.")
        else:
            print("O valor do depósito deve ser positivo.")
    except ValueError:
        print("Erro: Digite apenas números (ex: 100.50).")

    input("Pressione Enter para continuar...")


def sacar(usuario):
    print("\n--- Saque ---")
    try:
        valor = float(input("Quanto deseja sacar? (Em R$) "))
        saldo_atual = usuario['saldo']

        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > saldo_atual:
            print(f"Saldo insuficiente! Você tem apenas R${saldo_atual:.2f}.")
        else:
            novo_saldo = saldo_atual - valor  # Atualiza o valor do saldo após realizar as validações

            atualizar_dados_usuario(usuario['cpf'], novo_saldo)  # Escreve o novo saldo no arquivo
            print(f"Sucesso! R$ {valor:.2f} sacado.")
            print(f"Saldo restante: R$ {novo_saldo:.2f}")
    except ValueError:
        print("Erro: Digite apenas números.")

    input("Pressione Enter para continuar...")


def atualizar_dados_usuario(cpf, novo_saldo):
    """Atualiza o saldo de um usuário específico no arquivo."""
    linhas_atualizadas = []
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split('|')
                if len(dados) == 4:
                    cpf_atual = dados[0]
                    senha = dados[1]
                    nome = dados[2]
                    saldo = float(dados[3])

                    if cpf_atual == cpf:
                        saldo = novo_saldo # Se for o usuário alvo, atualiza o saldo na linha

                    # Reconstrói a linha para salvar
                    nova_linha = f"{cpf_atual}|{senha}|{nome}|{saldo}\n"
                    linhas_atualizadas.append(nova_linha)
    except FileNotFoundError:
        return

    # Reescreve o arquivo inteiro com os dados atualizados
    with open("usuarios.txt", "w") as arquivo:
        arquivo.writelines(linhas_atualizadas)


def logar():
    """
    Função para lidar com o login do usuário.
    Verifica CPF e senha no arquivo de usuários.
    """
    print("\n----- Tela de Login -----")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")

    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split('|')
                if len(dados) == 4:
                    cpf_arq = dados[0]
                    senha_arq = dados[1]

                    # Verifica se o CPF e a senha correspondem
                    if cpf_arq == cpf and senha_arq == senha:
                        nome = dados[2]
                        saldo = float(dados[3])
                        usuario = {
                            'cpf': cpf_arq,
                            'senha': senha_arq,
                            'nome': nome,
                            'saldo': saldo
                        }
                        print(f"\nLogin bem-sucedido! Bem-vindo(a), {nome}!")
                        menu_usuario_logado(usuario)  # Chama o menu do usuário
                        return  # Sai da função logar após o sucesso

            # Se terminar o loop e não encontrar
            print("\nCPF ou senha incorretos. Tente novamente.")

    except FileNotFoundError:
        print("\nNenhum usuário cadastrado no sistema.")

    input("Pressione Enter para voltar ao menu...")


def cadastrar():
    """Função para lidar com o cadastro de um novo usuário."""
    print("\n----- Tela de Cadastro -----")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    nome = input("Digite seu nome: ")

    # Verifica se o CPF já existe lendo o arquivo manualmente
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split('|')
                if len(dados) > 0 and dados[0] == cpf:
                    print("\nErro: CPF já cadastrado!")
                    input("Pressione Enter para voltar ao menu...")
                    return
    except FileNotFoundError:
        # Se o arquivo não existe, é o primeiro cadastro, então seguimos em frente
        pass

    # Adiciona o novo usuário (formatado com separadores) ao arquivo
    # Usa 'a' (append) para adicionar ao final sem apagar o resto
    with open("usuarios.txt", "a") as arquivo:
        # Formato: cpf|senha|nome|saldo
        linha_nova = f"{cpf}|{senha}|{nome}|0.0\n"
        arquivo.write(linha_nova)

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

        match opcao:
            case '1':
                logar()
            case '2':
                cadastrar()
            case '3':
                print("Saindo do programa. Até logo!")
                break
            case _:
                print("\nOpção inválida! Por favor, tente novamente.")


if __name__ == "__main__":
    menu_principal()