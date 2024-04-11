import datetime
import textwrap

# funcao MENU


def menu():
    # Exibe as opções para escolha
    menu = """
    O que deseja fazer?
    [d] Depósito
    [s] Saque
    [e] Extrato
    [n] Nova Conta
    [l] Listar Contas
    [u] Novo Usuário
    [q] Sair
    -> """  # Removido o texto "Digite uma opção:"
    return input(menu)

# Funçõa extrato


def exibir_extrato(saldo, /, *, extrato, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        for conta in contas:
            linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

        agora = datetime.datetime.now()
        emissao = agora.strftime("%d/%m/%Y, %H:%M:%S")
        print("\n================ EXTRATO ================")
        print(linha)
        # listar_contas()
        print(f"\nEmitido em: {emissao}")
        print("Não foram realizadas movimentações." if not extrato else extrato)

        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
        print(f"\nEmitido em: {emissao}")
        print("==========================================")

    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


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
    agora = datetime.datetime.now()
    data_reg = agora.strftime("%d/%m/%Y, %H:%M:%S")

    # for conta in contas:
    # print("Deposito")
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

# Novo usuario


def criar_usuario(usuarios):
    cpf = input('Digite o cpf (apenas numeros): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(' Usuario ja cadastrado')
        return

    nome = input('Seu nome Completo é: ')
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def titular_extrato(usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        for conta in contas:
            linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


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
    # linha
    linha = ""

    # Cria o Loop While com True
    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                valor_depositado = float(
                    input("Digite o Valor a ser depositado: "))

                saldo, extrato = deposito(saldo, valor_depositado, extrato)
            else:
                while True:
                    print('Deseja cadastrar um novo usuário?')
                    print('\n1-SIM\n2-NAO\n')
                    escolha = input('Digite sua escolha: ')

                    if escolha == "1":

                        criar_usuario(usuarios)
                        numero_conta = len(contas) + 1
                        conta = criar_conta(AGENCIA, numero_conta, usuarios)

                        if conta:
                            contas.append(conta)
                            break

                    elif escolha == "2":
                        print('Até a proxima!')
                        break

                    else:
                        print('Digite uma opção válida!')
                        continue

        elif opcao == "s":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                valor = float(input("Informe o valor do saque: "))

                saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite_por_saque,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
                )

            else:
                while True:
                    print('Deseja cadastrar um novo usuário?')
                    print('\n1-SIM\n2-NAO\n')
                    escolha = input('Digite sua escolha: ')

                    if escolha == "1":

                        criar_usuario(usuarios)
                        numero_conta = len(contas) + 1
                        conta = criar_conta(AGENCIA, numero_conta, usuarios)

                        if conta:
                            contas.append(conta)
                            break

                    elif escolha == "2":
                        print('Até a proxima!')
                        break

                    else:
                        print('Digite uma opção válida!')
                        continue

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato,
                           usuarios=usuarios, contas=contas)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                listar_contas(contas)
                
            else:
                while True:
                    print('=== CONTA NÃO ENCONTRADA ===')
                    print('Deseja cadastrar um novo usuário e conta?')
                    print('\n1-SIM\n2-NAO\n')
                    escolha = input('Digite sua escolha: ')

                    if escolha == "1":

                        criar_usuario(usuarios)
                        numero_conta = len(contas) + 1
                        conta = criar_conta(AGENCIA, numero_conta, usuarios)

                        if conta:
                            contas.append(conta)
                            break

                    elif escolha == "2":
                        print('Até a proxima!')
                        break

                    else:
                        print('Digite uma opção válida!')
                        continue

        elif opcao == "q":
            print("Sair")
            break
        else:
            print(f"===ATENÇÃO===\nVocê digitou {opcao}")
            print("\nPor favor, digite um Opção válida!\n")


main()
