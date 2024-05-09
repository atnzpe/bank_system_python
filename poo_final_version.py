# Importa a biblioteca date time
import datetime


class Banco:
    """
    Classe que representa um banco com suas contas e usuários.
    """

    def __init__(self):
        # Inclui os atributos conta e usuario
        self.contas = []
        self.usuarios = []

    def criar_usuario(self, nome, cpf, data_nascimento, endereco):
        """
        Cria o usuario.

        Args:
            nome (str): Nome do usuário.
            Cpf (int): CPf do usuario.
            data_nascimento (str): Data que a pessoa nasceu.

        Returns:
            usuario: usuario criado.
        """
        if self.obter_usuario_por_cpf(cpf):
            raise ValueError("Usuário já cadastrado com esse CPF.")
        usuario = PessoaFisica(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(usuario)
        return usuario

    def criar_conta(self, numero, agencia, titular):
        """
        Cria uma nova conta no banco.

        Args:
            numero (int): O número da conta.
            agencia (str): A agência da conta.
            titular (PessoaFisica): O titular da conta.

        Returns:
            Conta: A conta criada.
        """
        conta = Conta(numero, agencia, titular)

        self.contas.append(conta)

        return conta

    def listar_contas(self):
        for conta in self.contas:
            print(
                f"Número: {conta.numero}, Agência: {conta.agencia}, Titular: {conta.titular.nome}"
            )

    def obter_conta_por_cpf(self, cpf):
        for conta in self.contas:
            if conta.titular.cpf == cpf:
                return conta
        return None

    def obter_usuario_por_cpf(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None


class Conta:
    def __init__(self, numero, agencia, titular, saldo=0):
        self.numero = numero
        self.agencia = agencia
        self.titular = titular
        self._saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        """
        Efetua transação deposito

        Args:
            valor (float): Valor da transação (positivo para depósitos).

        Returns:
            None.
        """
        self._saldo += valor
        transacao = Transacao(valor, "(+) Deposito", self._saldo)
        self.extrato.append(transacao)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        """
        Efetua transação de saque

        Args:
            valor (float): Valor da transação (negativo para saque).

        Returns:
            None.
        """
        self._saldo -= valor
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        if (
            len(
                [
                    t
                    for t in self.extrato
                    if t.tipo == "(-) Saque" and t.data.date() == datetime.date.today()
                ]
            )
            >= 3
        ):
            raise ValueError("Limite de saques diários atingido.")
        transacao = Transacao(valor, "(-) Saque", self._saldo)
        self.extrato.append(transacao)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        """
        Cria a exibição o extrato com as transaçoes do usuario

        Args:
            Não tem.

        Returns:
            usuario: usuario criado.
        """
        data = datetime.datetime.now()
        dt_extrato = data.strftime("%d/%m/%Y, %H:%M:%S")
        e = " EXTRATO "
        text_registro_transacao = " MOVIMENTAÇÕES "

        text = f"""                
Data da Emissão: {dt_extrato}
Agência: {self.agencia}
Conta:   {self.numero}
Cliente: {self.titular.nome}
CPF Cliente: {self.titular.cpf}"""

        print(e.center(30, "="))
        print("-" * 30)
        print("DADOS DA CONTA")
        print("-" * 30)
        print(text)
        print("-" * 30)
        print(text_registro_transacao.center(30, "="))
        print("-" * 30)

        # Verifica se o extrato esta vazio
        if not self.extrato:
            print("Não foram realizadas movimentações.")

        else:
            for transacao in self.extrato:
                print(
                    f"{transacao.data} - {transacao.tipo}: R$ {transacao.valor:.2f} - Saldo: R$ {self._saldo:.2f}"
                )
        print("-" * 30)
        print(f"Saldo Final: R$ {self._saldo:.2f}")
        print("-" * 30)


class PessoaFisica:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class Transacao:
    """
    Classe que os dados sobre as transações realizadas.
    """

    def __init__(self, valor, tipo, saldo):
        """
        Inicializa um objeto Transacao com informações sobre a transação realizada.

        Args:
        valor (float): Valor da transação (positivo para depósitos, negativo para saques).
        tipo (str): Tipo da transação ("deposito" ou "saque").
        saldo (float): Saldo da conta após a transação.

        Returns:
        None
        """
        dt_extrato = datetime.datetime.now()
        self.valor = valor
        self.tipo = tipo
        self.data = dt_extrato.strftime("%d/%m/%Y, %H:%M:%S")
        self.saldo = saldo


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
    -> """
    return input(menu)


# Menu auxiliar para escolha de sim ou não


def menu_yes_or_no():
    menu_yes_or_no = """
    Escolha Sim ou Não?
    [1] SIM
    [0] NÂO
    ->  """
    return input(menu_yes_or_no)


# Função principal do programa. Gerencia as operações bancárias.


def main():
    # Cria um objeto da classe Banco, que representa o sistema bancário com suas funcionalidades.
    banco = Banco()

    # Inciar um Laço True esperando o usuario interagir com o menu
    while True:
        # Cria a Veriável opção para que recebe uma escolha do usuario nas opções dispostas pela função Menu()
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do usuário: ")
            conta = banco.obter_conta_por_cpf(cpf)

            if conta:
                try:
                    valor_deposito = float(input("Digite o valor do depósito: "))
                    conta.depositar(valor_deposito)
                except ValueError as e:
                    print(e)
            else:
                print(
                    "Conta não encontrada.Deseja cadastra um Novo Usuário e uma nova conta?"
                )

                menu_aux = menu_yes_or_no()

                # Se escolher SIM crie um e uma nova conta
                if menu_aux == "1":
                    print("=== Iniciando a criação do usuário ===")
                    nome = input("Digite o nome do usuário: ")
                    cpf = cpf
                    data_nascimento = input(
                        "Digite a data de nascimento (dd/mm/aaaa): "
                    )
                    endereco = input("Digite o endereço: ")
                    try:
                        banco.criar_usuario(nome, cpf, data_nascimento, endereco)
                        print("Usuário criado com sucesso!")
                    except ValueError as e:
                        print(e)

                    # Incia o cadastro da conta
                    usuario = banco.obter_usuario_por_cpf(cpf)
                    if usuario:
                        numero_conta = len(banco.contas) + 1
                        conta = banco.criar_conta(numero_conta, "0001", usuario)
                        print(
                            f"Seja bem vindo {nome} Conta criada com sucesso! Número: {numero_conta}"
                        )

            conta = banco.obter_conta_por_cpf(cpf)

        elif opcao == "s":
            cpf = input("Informe o CPF do usuário: ")
            conta = banco.obter_conta_por_cpf(cpf)

            if conta:
                try:
                    valor_saque = float(input("Digite o valor do saque: "))
                    conta.sacar(valor_saque)
                except ValueError as e:
                    print(e)
            else:
                print(
                    "Conta não encontrada.Deseja cadastra um Novo Usuário e uma nova conta?"
                )

                menu_aux = menu_yes_or_no()

                # Se escolher SIM crie um e uma nova conta
                if menu_aux == "1":
                    print("=== Iniciando a criação do usuário ===")
                    nome = input("Digite o nome do usuário: ")
                    cpf = cpf
                    data_nascimento = input(
                        "Digite a data de nascimento (dd/mm/aaaa): "
                    )
                    endereco = input("Digite o endereço: ")
                    try:
                        banco.criar_usuario(nome, cpf, data_nascimento, endereco)
                        print("Usuário criado com sucesso!")
                    except ValueError as e:
                        print(e)

                    # Incia o cadastro da conta
                    usuario = banco.obter_usuario_por_cpf(cpf)
                    if usuario:
                        numero_conta = len(banco.contas) + 1
                        conta = banco.criar_conta(numero_conta, "0001", usuario)
                        print(
                            f"Seja bem vindo {nome} Conta criada com sucesso! Número: {numero_conta}"
                        )

            conta = banco.obter_conta_por_cpf(cpf)

        elif opcao == "e":
            cpf = input("Informe o CPF do usuário: ")
            conta = banco.obter_conta_por_cpf(cpf)

            if conta:
                conta.exibir_extrato()
            else:
                print(
                    "Conta não encontrada.Deseja cadastra um Novo Usuário e uma nova conta?"
                )

                menu_aux = menu_yes_or_no()

                # Se escolher SIM crie um e uma nova conta
                if menu_aux == "1":
                    print("=== Iniciando a criação do usuário ===")
                    nome = input("Digite o nome do usuário: ")
                    cpf = cpf
                    data_nascimento = input(
                        "Digite a data de nascimento (dd/mm/aaaa): "
                    )
                    endereco = input("Digite o endereço: ")
                    try:
                        banco.criar_usuario(nome, cpf, data_nascimento, endereco)
                        print("Usuário criado com sucesso!")
                    except ValueError as e:
                        print(e)

                    # Incia o cadastro da conta
                    usuario = banco.obter_usuario_por_cpf(cpf)
                    if usuario:
                        numero_conta = len(banco.contas) + 1
                        conta = banco.criar_conta(numero_conta, "0001", usuario)
                        print(
                            f"Seja bem vindo {nome} Conta criada com sucesso! Número: {numero_conta}"
                        )

            conta = banco.obter_conta_por_cpf(cpf)

        elif opcao == "u":
            nome = input("Digite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            endereco = input("Digite o endereço: ")
            try:
                banco.criar_usuario(nome, cpf, data_nascimento, endereco)
                print("Usuário criado com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "n":
            cpf = input("Informe o CPF do titular da conta: ")
            usuario = banco.obter_usuario_por_cpf(cpf)

            if usuario:
                numero_conta = len(banco.contas) + 1
                conta = banco.criar_conta(numero_conta, "0001", usuario)
                print(f"Conta criada com sucesso! Número: {conta.numero}")
            else:
                print(
                    "Conta não encontrada.Deseja cadastra um Novo Usuário e uma nova conta?"
                )

                menu_aux = menu_yes_or_no()

                # Se escolher SIM crie um e uma nova conta
                if menu_aux == "1":
                    print("=== Iniciando a criação do usuário ===")
                    nome = input("Digite o nome do usuário: ")
                    cpf = cpf
                    data_nascimento = input(
                        "Digite a data de nascimento (dd/mm/aaaa): "
                    )
                    endereco = input("Digite o endereço: ")
                    try:
                        banco.criar_usuario(nome, cpf, data_nascimento, endereco)
                        print("Usuário criado com sucesso!")
                    except ValueError as e:
                        print(e)

                    # Incia o cadastro da conta
                    usuario = banco.obter_usuario_por_cpf(cpf)
                    if usuario:
                        numero_conta = len(banco.contas) + 1
                        conta = banco.criar_conta(numero_conta, "0001", usuario)
                        print(
                            f"Seja bem vindo {nome} Conta criada com sucesso! Número: {numero_conta}"
                        )

            conta = banco.obter_conta_por_cpf(cpf)

        elif opcao == "l":
            banco.listar_contas()

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
