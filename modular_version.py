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


# funcao saque


def saque(numero_saques, limite_saques, saldo, extrato):
    print("Saque")

    if numero_saques >= limite_saques:
        print(f"Você já efetuou {numero_saques} saques hoje!")
        # break

    while True:

        if saldo <= 0:
            print(f"Seu saldo atual é R$ {saldo}!\n")
            break

        msg_saque = input("Digite o Valor a ser sacado: ")
        valor_digitado_saque = float(msg_saque)

        if saldo <= 0 and numero_saques >= limite_saques:
            print(f"Seu saldo atual é R$ {saldo}!")
            print(f"Você já efetuou {numero_saques} saques hoje!")
            break

        elif saldo <= 0:
            print(f"Seu saldo atual é R$ {saldo}!\n")
            break

        elif numero_saques >= limite_saques:
            print(f"Você já efetuou {numero_saques} saques hoje!")
            break

        else:
            if valor_digitado_saque > 500:
                print(
                    f"Valor digitado para saque maior que R$ 500,00 {valor_digitado_saque=}"
                )
                break

            else:
                if valor_digitado_saque > saldo:
                    print("Saldo insuficiente!")
                    break
                else:
                    print(
                        f"Saque no valor de R$ {valor_digitado_saque:,.2f} foi realizado com sucesso!"
                    )
                    # Adicionar o Valor Digitado ao Saldo
                    saldo -= valor_digitado_saque
                    # Grava a operaçõa na vaiável Extrato
                    extrato += f"\n(-) Saque R$ {valor_digitado_saque:,.2f}\n"
                    numero_saques += 1
                    break

# A funçõa recebe argumentos por posiçõa por isso temos o caracter '/'
def deposito(saldo, valor_deposito, extrato, /):
    #print("Deposito")
    '''
    n_tentativas_erradas = 0


    if valor_deposito <= 0:
        n_tentativas_erradas += 1
        print("Valor digitado Menor ou Igual a Zero.Por favor, tente novamente!")
        print(valor_deposito)

        print(f"Você errou {n_tentativas_erradas} vez!")
            
        if n_tentativas_erradas == 3:
            print(
                f"\nVocê digitou {n_tentativas_erradas} Vezes seguidas um valor Zero ou Negativo!\nPor favor tente novamente!"
                )
    
'''
    if valor_deposito > 0:
        print(f"Deposito no valor de R$ {valor_deposito:,.2f} foi realizado com sucesso!")
        # Adicionar o Valor Digitado ao Saldo
        saldo += valor_deposito
        # Grava a operaçõa na vaiável Extrato
        extrato += f"\n(+) Depósito R$ {valor_deposito:,.2f}\n"
    else:
        print(f"Valor digitado ('R$ {valor_deposito:,.2f}')Menor ou Igual a Zero.Por favor, tente novamente!")
        
    

    return saldo, extrato            

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
            valor_depositado = float(input("Digite o Valor a ser depositado: "))
            
            deposito(saldo,valor_depositado,extrato)
            '''
            print("Deposito")
            n_tentativas_erradas = 0

          
                
                
                

                if valor_deposito <= 0:
                    n_tentativas_erradas += 1
                    print(
                        "Valor digitado Menor ou Igual a Zero.Por favor, tente novamente!"
                    )
                    print(valor_deposito)

                    print(f"Você errou {n_tentativas_erradas} vez!")

                if n_tentativas_erradas == 3:
                    print(
                        f"\nVocê digitou {n_tentativas_erradas} Vezes seguidas um valor Zero ou Negativo!\nPor favor tente novamente!"
                    )
                    break

                else:
                    print(
                        f"Deposito no valor de R$ {valor_deposito:,.2f} foi realizado com sucesso!"
                    )
                    # Adicionar o Valor Digitado ao Saldo
                    saldo += valor_deposito
                    # Grava a operaçõa na vaiável Extrato
                    extrato += f"\n(+) Depósito R$ {valor_deposito:,.2f}\n"
                    break
'''
        elif opcao == "s":
            saque(numero_saques, LIMITE_SAQUES, saldo, extrato=extrato)

        elif opcao == "e":
            print("=== Extrato ===")
            agora = datetime.datetime.now()
            agora_string = agora.strftime("%A %d %B %y %I:%M")
            print(agora_string)
            print("==========")
            if extrato == "":
                print("----------")
                print("Não foram realizadas movimentações.")
                print("----------")
            else:
                print("--------------------")
                print(extrato, f"\nSaldo Atual: R$ {saldo:,.2f}")
                print("--------------------")

        elif opcao == "q":
            print("Sair")
            break
        else:
            print(f"===ATENÇÃO===\nVocê digitou {opcao}")
            print("\nPor favor, digite um Opção válida!\n")


main()
