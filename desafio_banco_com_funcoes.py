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


def saque(*,saldo,limite,extrato,numero_saques,LIMITE_SAQUE):
    
    saque = float(input("Quantia desejada para saque: "))

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
        
        retorno = f"R$ {saque} foram sacados!"
        extrato.append(retorno)
        
        print(retorno)

        return saldo, numero_saques
    else:
        print("Digite um valor valido")
        return saldo, numero_saques
def deposito():
    print()

def exibir_extrato():
    print()

def cadastro_usuario():
    print()

def cadastro_conta():
    print()
while numero_de_saques < 3:
    saldo, numero_de_saques = saque(saldo=saldo,limite=limite,extrato=extrato,numero_saques=numero_de_saques,LIMITE_SAQUE=LIMITE_DE_SAQUES)

print()

print(extrato)