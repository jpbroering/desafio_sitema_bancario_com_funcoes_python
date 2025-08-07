

def sacar(*, saque, saldo, limite, extrato, numero_saques, LIMITE_SAQUE):

    excedeu_saldo = saldo < saque
    excedeu_limite = limite < saque
    excedeu_saque = numero_saques >= LIMITE_SAQUE

    if excedeu_saldo:
        print("Não foi possível fazer a transação! O valor inserido ultrapassa o saldo atual.")
        return saldo, numero_saques
    elif excedeu_limite:
        print("Não foi possível fazer a transação! O valor inserido ultrapassa o limite da conta.")
        return saldo, numero_saques
    elif excedeu_saque:
        print("Não foi possível fazer a transação! O limite de saques diários foi alcançado.")
        return saldo, numero_saques
    elif saque > 0:
        numero_saques += 1
        saldo -= saque
        retorno = f"R$ {saque:.2f} foram sacados!\n"
        extrato.append(retorno)
        print(retorno)
        return saldo, numero_saques
    else:
        print("Digite um valor válido")
        return saldo, numero_saques

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        retorno = f"R$ {valor:.2f} foram depositados!\n"
        extrato.append(retorno)
        print(retorno)
        return saldo
    else:
        print("\nDigite um valor válido")
        return 0

def exibir_extrato(saldo,/,*,extrato):
    print("\n")
    print(" EXTRATO ".center(40,"#"))
    if len(extrato) != 0:
        print()
        for transacao in extrato:
            print(transacao)
        print(f"Saldo atual da conta: {saldo}\n")
    else:
        print("\nNenhuma transação feita até o momento.\n")
    print("".center(40,"#"))

def verifica_cpf(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastro_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")

    if verifica_cpf(cpf, usuarios):
        print("Operação falhou! CPF em uso.")
        return

    nome = input("Digite o nome de usuário [i.e: Nome Sobrenome]: ")
    data_de_nascimento = input("Digite o nome de usuário [i.e: dd/mm/aaaa]: ")
    endereco = input("Digite o nome de usuário [i.e: logradouto, N - bairro - cidade/sigla do estado]: ")
    usuario = {
        "CPF": cpf,
        "nome":nome,
        "data de nascimento":data_de_nascimento,
        "endereço":endereco
        }

    print(f"Usuário {nome} criado com sucesso!")
    usuarios.append(usuario)




def cadastro_conta(usuarios,contas):
    cpf = input("Digite o CPF do ususário ao qual a conta será cadastrada: ")

    contador = len(contas)+1

    if verifica_cpf(cpf,usuarios) == None:
        print("Operação falhou! Não foi possível encontrar o usuário.")
        return contador
    
    contas.append({
        "conta": contador,
        "usuario": cpf,
        "agencia": "0001",
    })
    print("Conta cadastrada com sucesso!")

def exibir_conta(contas):
    corpo = ""
    for conta in contas:
        for chave,valor in conta.items():
            corpo += f"{chave}: {valor}\n"
        corpo += "\n "

    print(" LISTAR ".center(40,"#"))
    print("\n",corpo,end="")
    print("".center(40,"#"))

def main():

    LIMITE_DE_SAQUES = 3
    MENSAGEM = """\n\n####### Bem vindo ao Banco sem nome! #######

    Digite para:
    [d] Deposito
    [s] Saque
    [e] Extrato
    [rs] Registrar usuário
    [rc] Registra conta
    [ec] Exibir contas
    [q] Sair

    opção: """

    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    extrato = []
    usuarios = []
    contas = []


    while True:
        opcao = input(MENSAGEM)

        if opcao == "d":
            valor = float(input("Quantia desejada para deposito: "))
            saldo += depositar(saldo,valor,extrato)

        elif opcao == "s": 
            saque = float(input("Quantia desejada para saque: "))
            saldo, numero_de_saques = sacar(saque=saque, saldo=saldo, limite=limite, extrato=extrato, numero_saques=numero_de_saques, LIMITE_SAQUE=LIMITE_DE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "rs":
            cadastro_usuario(usuarios)

        elif opcao == "rc":
            cadastro_conta(usuarios,contas)

        elif opcao == "ec":
            exibir_conta(contas)

        elif opcao == "q":
            print("\nObrigado por usar nossos serviços!")
            return
        else:
            print("\nDigite uma opção válida!")
        # Para dar tempo para o usuário ler:
        input("Digite qualquer digito para continuar.")

main()