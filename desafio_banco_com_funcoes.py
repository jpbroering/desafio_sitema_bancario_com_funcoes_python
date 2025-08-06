

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
def verifica_cpf(cpf, usuarios,/,*,procura):
    if len(cpf) == 14:
        cpf_len = [3,3,3,2]
        veri_cpf = cpf.split("-").split(".")
        if len(veri_cpf) == 4:
            for index, value in enumerate(veri_cpf):
                if len(value) == cpf_len[index]:
                    continue
                else:
                    return False
            if cpf not in usuarios and procura == False:
                return True
            elif cpf in usuarios and procura:
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

def verifica_data(data_de_nascimento):
    if len(data_de_nascimento.split("/")) == 3:
            padrao = [31,12,2050]
            for index,data in enumerate(data_de_nascimento.split("/")):
                if int(data) > 0 and data <= padrao[index]:
                    continue
                else:
                    return False
            return True

# exemplo usuário
# usuarios = {
# "56565656565":{
#   "nome":"joao",
#   "data_de_nascimento":"13/06/2006",
#   "endereco":"logradouro, nro - bairro - cidade/sigla estado"
#   }
# }
def cadastro_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")

    if verifica_cpf(cpf, usuarios, procura=False):
        nome = input("Digite o nome de usuário [Nome Sobrenome]: ")

        data_de_nascimento = input("Digite o nome de usuário [i.e: 10/04/2000]: ")

        if verifica_data(data_de_nascimento):
            endereco = input("Digite o nome de usuário [i.e: Rua exemplo, 09 - vila das torres - SC]: ")

            usuario = {
                "nome":nome,
                "data de nascimento":data_de_nascimento,
                "endereço":endereco
                }

            print(f"Usuário {nome} criado com sucesso!")
            usuarios[cpf] = usuario
        else:
            print("Operação falhou! Digite uma data de nascimento válida.")
    else:
        print("Operação falhou! Digite um CPF válido.")

# exemplo conta
# contas = {
# 1:{
#   "agencia":"0001",
#   "usuario":"565656",
#   "dados":{
#       "saldo":0,
#       "limite":500,
#       "extrato":"",
#       "quantidade_saques":0,
#       "LIMITE_SAQUES":3,
#       }
#   }
# }
def cadastro_conta(usuarios,contas,contador):
    cpf = input("Digite o CPF do ususário ao qual a conta será cadastrada: ")

    if verifica_cpf(cpf,usuarios,procura=True):
        contas[contador] = {
            "usuario": cpf,
            "agencia": "0001",
            "dados": {
                "saldo": 0,
                "limite": 500,
                "extrato": "",
                "quantidade_saques": 0,
                "LIMITE_SAQUES": 3
            }
        }
        print("Conta cadastrada com sucesso")
        return contador+1
    else:
        print("Operação falhou! Não foi possível encontrar o usuário.")

# retorna o sistema bancário se a conta existir
def logar(contas,usuarios):
    numero = input("Dgite o número da conta a qual deseja logar: ")

    if numero in contas:
        print("Conta encontrada!")
        cpf = input(f"Para confirmar a conta digite o CPF da conta {numero}: ")

        if verifica_cpf(cpf,usuarios,procura=True):
            if cpf in contas[numero].values():
                return init_sistema_bancario(contas,(numero,contas[numero],))
            
            else:
                print("Operação inválida! CPF não condiz com o da conta.")

        else:
            print("Operação inválida! CPF formatado incorretamente. (I.E: 123.123.123-32 ou 12312312332)")

    else:
        print("Operação inválida! Número não encontrado.")

MENSAGEM_USUARIO = """\n\n####### Bem vindo ao Banco sem nome! #######

Digite para:
[s] Casdastrar usuário
[c] Cadastrar conta
[e] Entrar
[q] Sair
"""

MENSAGEM_CONTA = """\n\n

Digite para:
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair da conta

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
count_contas = 1

opcao = ""

def init_tela_inicial():
    while True:
        opcao = input(MENSAGEM_USUARIO)

        if opcao == "s":
            cadastro_usuario(usuarios)

        elif opcao == "c":
            count_contas = cadastro_conta(usuarios,contas,count_contas)

        elif opcao == "e":
            logar(contas,usuarios)

        elif opcao == "q":
            print("Obrigado por usar nosso sistema!")
            return
        
        else:
            print("Digite uma opção válida!")

def init_sistema_bancario(contas,conta):
    while True:
        opcao = input(MENSAGEM_CONTA)

        if opcao == "d":
            valor = float(input("Quantia desejada para deposito: "))
            saldo += depositar(saldo,valor,extrato)

        elif opcao == "s": 
            saque = float(input("Quantia desejada para saque: "))
            # Talvez tenha mudanças por causa da criação de conta, talvez condensar as informações em um dict na conta pra não precisar de tanto parâmetro
            saldo, numero_de_saques = sacar(saque=saque, *conta)

        elif opcao == "e":
            exibir_extrato(saldo,extrato=extrato)

        elif opcao == "q":
            print("\nObrigado por usar nossos serviços!")
            return
        else:
            print("\nDigite uma opção válida!")
