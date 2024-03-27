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
        t = 0
        while True:
            msg = input('Digite o Valor a ser depositado: ')
            valor = float(msg)

            if valor <= 0:
                t = t + 1
                print('Valor digitado Menor ou Igual a Zero.Por favor, tente novamente!')
                print(msg)

                print(f'Numero de Tentaivas:{t=}')

                if t == 3:
                    print(
                        '\nVocê digitou 3 Vezes seguidas um valor Zero ou Negativo!\nPor favor tente novamente!')
                    break

            else:
                print('Valor Ok')
                break

    elif opcao == "s":
        print("Saque")
    elif opcao == "e":
        print("Extrato")
    elif opcao == "q":
        print("Sair")
        break
    else:
        print(f"===ATENÇÃO===\nVocê digitou {opcao}")
        print("\nPor favor, digite um Opção válida!\n")
