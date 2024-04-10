import datetime
import textwrap

# funcao MENU


def menu():
    # Exibe as opções para escolha
    menu = """    
    O que deseja fazer?
    
    [d]\tDeposito
    [s]\tSaque
    [e]\tExtrato
    [n]\tNova Conta
    [l]\tListar Contas
    [u]\tNovo Usuario
    [q]\tSair
    
    -> Digite uma opção: """

    return input(textwrap.dedent(menu))

#extrato
def exibir_extrato(saldo, /, *, extrato):
    agora = datetime.datetime.now()
    emissao = agora.strftime("%d/%m/%Y, %H:%M:%S")
    print("\n================ EXTRATO ================")
    print(f"\nEmitido em: {emissao}")
    print("Não foram realizadas movimentações." if not extrato else extrato)

    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print(f"\nEmitido em: {emissao}")
    print("==========================================")


# funcao saque


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    agora = datetime.datetime.now()
    data_reg = agora.strftime("%d/%m/%Y, %H:%M:%S")

    if excedeu_saldo:
        print("Estais liso saldo insuficiente")

    elif excedeu_limite:
        print("Valor de saque maior que 500!")

    elif excedeu_saques:
        print("Ja fez tres saques hoje")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"\n(-) Saque:\t\tR$ {valor:.2f}\n{data_reg}\n"
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato


# A funçõa recebe argumentos por posiçõa por isso temos o caracter '/'


def deposito(saldo, valor_deposito, extrato, /):
    # print("Deposito")
    agora = datetime.datetime.now()
    data_reg = agora.strftime("%d/%m/%Y, %H:%M:%S")
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"\n(+) Deposito:\t\tR$ {valor_deposito:,.2f}\n{data_reg}\n"
        print(
            f"Deposito no valor de R$ {valor_deposito:,.2f} foi realizado com sucesso!"
        )
        # Adicionar o Valor Digitado ao Saldo

        # Grava a operaçõa na vaiável Extrato

    else:
        print(
            f"Valor digitado ('R$ {valor_deposito:,.2f}')Menor ou Igual a Zero.Por favor, tente novamente!"
        )

    return saldo, extrato

#Novo usuario
def criar_usuario(usuarios):
    cpf = input('Digite o cpf (apenas numeros): ')
    usuario = filtrar_usuario (cpf, usuarios)
    
    if usuario:
        print(' Usuario ja cadastrado')
        return
    
    nome = input('Seu nome Completo é: ')
    
    
    

def main():
    # Variaveis
    # Limite de saques dia
    LIMITE_SAQUES = 3
    # AGENCIA
    AGENCIA = "0001"

    # Saldo incial zero
    saldo = 0
    # Limite de valor por saque
    limite_por_saque = 500
    # Texto Extrato
    extrato = ""
    # Contador Saque Diário
    numero_saques = 0
    # Usuarios
    usuarios = []
    # Contas
    contas = []

    # Cria o Loop While com True
    while True:
        opcao = menu()

        if opcao == "d":
            valor_depositado = float(
                input("Digite o Valor a ser depositado: "))

            saldo, extrato = deposito(saldo, valor_depositado, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite_por_saque,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Sair")
            break
        else:
            print(f"===ATENÇÃO===\nVocê digitou {opcao}")
            print("\nPor favor, digite um Opção válida!\n")


main()
