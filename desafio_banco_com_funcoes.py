

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

# Não adicionei verificação de números por enquanto.
def verifica_cpf(cpf, usuarios):
    if len(cpf) == 14:
        cpf_len = [3,3,3,2]
        veri_cpf = cpf.split("-").split(".")
        if len(veri_cpf) == 4:
            for index, value in enumerate(veri_cpf):
                if len(value) == cpf_len[index]:
                    continue
                else:
                    return False
            if cpf not in usuarios:
                return True
            else:
                print("CPF existente.")
                return False
    elif len(cpf) == 11:
        if cpf not in usuarios:
            return True
        else:
            print("CPF existente.")
            return False
    else:
        return False

# exemplo
# usuarios = {"565656":{"nome":"joao","data_de_nascimento":"13/06/06","endereco":"logradouro, nro - bairro - cidade/sigla estado"}}
def cadastro_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")

    if verifica_cpf(cpf, usuarios):


    print()

# exemplo
# contas = {"1":{"agencia":0001,"numero_conta":"1","usuario":"565656"}}
def cadastro_conta(usuarios,contas):
    print()

MENSAGEM = """\n\n####### Bem vindo ao Banco sem nome! #######

Digite para:
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

opção: """

saldo = 0
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
    