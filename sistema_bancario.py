# Funções do sistema bancário

def criar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    cpf = input("Informe o CPF do usuário: ")
    usuarios[cpf] = nome
    print(f"Usuário {nome} criado com sucesso!")

def criar_conta_corrente(usuarios, contas):
    cpf = input("Informe o CPF do usuário para vincular a conta: ")
    if cpf in usuarios:
        numero_conta = len(contas) + 1  # Gera um número de conta sequencial
        contas[numero_conta] = {
            "usuario": usuarios[cpf],
            "saldo": 0,
            "extrato": "",
            "numero_saques": 0
        }
        print(f"Conta corrente criada com sucesso para {usuarios[cpf]}! Número da conta: {numero_conta}")
    else:
        print("Usuário não encontrado!")

def depositar(conta):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(conta):
    valor = float(input("Informe o valor do saque: "))
    limite = 500
    LIMITE_SAQUES = 3

    excedeu_saldo = valor > conta["saldo"]
    excedeu_limite = valor > limite
    excedeu_saques = conta["numero_saques"] >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def visualizar_extrato(conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"Saldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

# Inicialização
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta Corrente
[q] Sair

=> """

usuarios = {}
contas = {}

while True:
    opcao = input(menu)

    if opcao == "d":
        cpf = input("Informe o CPF do usuário: ")
        if cpf in usuarios:
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta in contas:
                depositar(contas[numero_conta])
            else:
                print("Conta não encontrada!")
        else:
            print("Usuário não encontrado!")

    elif opcao == "s":
        cpf = input("Informe o CPF do usuário: ")
        if cpf in usuarios:
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta in contas:
                sacar(contas[numero_conta])
            else:
                print("Conta não encontrada!")
        else:
            print("Usuário não encontrado!")

    elif opcao == "e":
        cpf = input("Informe o CPF do usuário: ")
        if cpf in usuarios:
            numero_conta = int(input("Informe o número da conta: "))
            if numero_conta in contas:
                visualizar_extrato(contas[numero_conta])
            else:
                print("Conta não encontrada!")
        else:
            print("Usuário não encontrado!")

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "c":
        criar_conta_corrente(usuarios, contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")