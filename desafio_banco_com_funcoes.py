

def sacar(*, saque, saldo, limite, extrato, numero_saques, LIMITE_SAQUE):

    excedeu_saldo = saldo < saque

    excedeu_limite = limite < saque

    excedeu_saque = numero_saques > LIMITE_SAQUE

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
    info += [transacao for transacao in extrato]
    print(" EXTRATO ".center("#",20))
    print(info)
    print("".center("#",20))

def cadastro_usuario(usuarios):
    # nome = input("Digite o nome do ")
    print()

def cadastro_conta(usuarios,contas):
    print()

MENSAGEM = """\n\n####### Bem vindo ao Banco sem nome! #######

Digite para:
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

opção: """

saldo = 1000
limite = 500
extrato = ""
numero_de_saques = 0

retorno = "" 

LIMITE_DE_SAQUES = 3

extrato = list()

usuarios = list()
contas = list()

opcao = ""

while True:
    opcao = input(MENSAGEM)

    if opcao == "d":
        valor = float(input("Quantia desejada para deposito: "))
        saldo += depositar(saldo,valor,extrato)

    elif opcao == "s": 
        saque = float(input("Quantia desejada para saque: "))
        # Talvez tenha mudanças por causa da criação de conta, talvez condensar as informações em um dict na conta pra não precisar de tanto parâmetro
        saldo, numero_de_saques = sacar(saque=saque, saldo=saldo, limite=limite, extrato=extrato, numero_saques=numero_de_saques, LIMITE_SAQUE=LIMITE_DE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo,extrato=extrato)
    elif opcao == "u":
        print()
    elif opcao == "c":
        print()
    elif opcao == "q":
        print("\nObrigado por usar nossos serviços!")
        break
    else:
        print("\nDigite uma opção válida!")
    