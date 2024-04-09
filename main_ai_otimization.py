import datetime

# Imprime mensagem de boas-vindas, pergunta o que o cliente deseja fazer e exibe as opções
menu = """
O que deseja fazer?
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
Digite uma opção: """
print(menu)

# Variáveis
saldo = 0
limite_saque = 500
extrato = ""
saques_hoje = 0
limite_saques = 3

# Loop principal
while True:
    opcao = input(menu)

    if opcao == "d":
        while True:
            try:
                valor_deposito = float(input("Digite o valor a ser depositado: "))
                if valor_deposito <= 0:
                    print("Valor inválido. Tente novamente.")
                else:
                    saldo += valor_deposito
                    extrato += f"\n(+) Depósito: R$ {valor_deposito:.2f}"
                    print(f"Depósito no valor de R$ {valor_deposito:.2f} realizado com sucesso!")
                    break
            except ValueError:
                print("Valor inválido. Tente novamente.")

    elif opcao == "s":
        if saques_hoje >= limite_saques:
            print(f"Você já efetuou {saques_hoje} saques hoje.")
        elif saldo <= 0:
            print("Saldo insuficiente.")
        else:
            while True:
                try:
                    valor_saque = float(input("Digite o valor a ser sacado: "))
                    if valor_saque > limite_saque:
                        print("Valor de saque maior que o limite de R$ 500,00.")
                    elif valor_saque > saldo:
                        print("Saldo insuficiente.")
                    else:
                        saldo -= valor_saque
                        extrato += f"\n(-) Saque: R$ {valor_saque:.2f}"
                        saques_hoje += 1
                        print(f"Saque no valor de R$ {valor_saque:.2f} realizado com sucesso!")
                        break
                except ValueError:
                    print("Valor inválido. Tente novamente.")

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
            print(extrato, f"\nSaldo Atual: R$ {saldo:.2f}")
            print("--------------------")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print(f"Opção inválida: {opcao}")