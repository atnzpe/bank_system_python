import datetime

# Imprime Mensagem de Boas Vindas

# Imprime perguntando o que o cliente deseja fazer

# Exibe as opções para escolha
menu = "O que deseja fazer?\n[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\nDigite uma opção: "

# Variaveis
# Saldo incial zero
saldo = 0

# Limite de valor por saque
limite_por_saque = 500
# Texto Extrato
extrato = ""
# Contador Saque Diário
numero_saques = 0
# Limite de saques dia
LIMITE_SAQUES = 3

# Cria o Loop While com True
while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        n_tentativas_erradas = 0

        while True:
            msg_deposito = input('Digite o Valor a ser depositado: ')
            valor_digitado_deposito = float(msg_deposito)

            if valor_digitado_deposito <= 0:
                n_tentativas_erradas += 1
                print('Valor digitado Menor ou Igual a Zero.Por favor, tente novamente!')
                print(msg_deposito)

                print(f'Você errou {n_tentativas_erradas} vez!')

                if n_tentativas_erradas == 3:
                    print(
                        f'\nVocê digitou {n_tentativas_erradas} Vezes seguidas um valor Zero ou Negativo!\nPor favor tente novamente!')
                    break

            else:
                print(
                    f'Deposito no valor de R$ {valor_digitado_deposito:,.2f} foi realizado com sucesso!')
                # Adicionar o Valor Digitado ao Saldo
                saldo += valor_digitado_deposito
                # Grava a operaçõa na vaiável Extrato
                extrato += (f'\n(+) Depósito R$ {valor_digitado_deposito:,.2f}\n')
                break

    elif opcao == "s":
        print("Saque")
        
        if numero_saques >= LIMITE_SAQUES:
            print(f'Você já efetuou {numero_saques} saques hoje!')
            break
            
        while True:
            
            if saldo <= 0:
                print(f'Seu saldo atual é R$ {saldo}!\n')
                break
        
            msg_saque = input('Digite o Valor a ser sacado: ')
            valor_digitado_saque = float(msg_saque)
        
            if saldo <= 0 and numero_saques >= LIMITE_SAQUES:
                print(f'Seu saldo atual é R$ {saldo}!')
                print(f'Você já efetuou {numero_saques} saques hoje!')
                break
        
            elif saldo <= 0:
                print(f'Seu saldo atual é R$ {saldo}!\n')
                break
        
            elif numero_saques >= LIMITE_SAQUES:
                print(f'Você já efetuou {numero_saques} saques hoje!')
                break
            
            else:          
                if valor_digitado_saque > 500:
                    print(f'Valor digitado para saque maior que R$ 500,00 {valor_digitado_saque=}')
                    break
                
                else:
                    if valor_digitado_saque > saldo:
                        print('Saldo insuficiente!')
                        break
                    else:
                        print(
                        f'Saque no valor de R$ {valor_digitado_saque:,.2f} foi realizado com sucesso!')
                        # Adicionar o Valor Digitado ao Saldo
                        saldo -= valor_digitado_saque
                        # Grava a operaçõa na vaiável Extrato
                        extrato += (f'\n(-) Saque R$ {valor_digitado_saque:,.2f}\n')
                        numero_saques +=1
                        break
                
            
            
            
            
            

    elif opcao == "e":
        print("=== Extrato ===")
        agora = datetime.datetime.now()
        agora_string = agora.strftime("%A %d %B %y %I:%M")
        print(agora_string)
        print('==========')
        if extrato == "":
            print('----------')
            print('Não foram realizadas movimentações.')
            print('----------')
        else:
            print('--------------------')
            print(extrato, f'\nSaldo Atual: R$ {saldo:,.2f}')
            print('--------------------')

    elif opcao == "q":
        print("Sair")
        break
    else:
        print(f"===ATENÇÃO===\nVocê digitou {opcao}")
        print("\nPor favor, digite um Opção válida!\n")

