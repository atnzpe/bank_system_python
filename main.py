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
        while True:
            msg = input('Digite o Valor do deposito: ')
            valor = float(msg)

            if valor <= 0:
                print('Valor digitado Menor ou Igual a Zero')
                print(msg)
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
