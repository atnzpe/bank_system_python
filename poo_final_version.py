"""
Biblioteca 
"""

import datetime


class Banco:
    """
    Representa um banco, gerenciando contas e usuários.

    Atributos:
        contas (list): Uma lista de objetos Conta associados ao banco.
        usuarios (list): Uma lista de objetos PessoaFisica representando
                         os usuários do banco.
    """

    def __init__(self):
        """Inicializa um novo objeto Banco com listas vazias de contas e usuários."""
        self.contas = []
        self.usuarios = []

    def criar_usuario(self, nome, cpf, data_nascimento, endereco):
        """ "
        Cria um novo usuário e o adiciona à lista de usuários do banco.

        Args:
            nome (str): Nome do usuário.
            cpf (str): CPF do usuário.
            data_nascimento (str): Data de nascimento do usuário no formato "dd/mm/aaaa".
            endereco (str): Endereço do usuário.

        Returns:
            PessoaFisica: O objeto PessoaFisica representando o usuário criado.

        Raises:
            ValueError: Se já existir um usuário com o mesmo CPF.
        """
        if self.obter_usuario_por_cpf(cpf):
            raise ValueError("Usuário já cadastrado com esse CPF.")
        usuario = PessoaFisica(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(usuario)
        return usuario

    def criar_conta(self, numero, agencia, titular):
        """
        Cria uma nova conta e a adiciona à lista de contas do banco.

        Args:
            numero (int): Número da conta.
            agencia (str): Agência da conta.
            titular (PessoaFisica): O titular da conta (objeto PessoaFisica).

        Returns:
            Conta: O objeto Conta representando a conta criada.
        """
        conta = Conta(numero, agencia, titular)

        self.contas.append(conta)

        return conta

    def listar_contas(self):
        """Imprime na tela a lista de contas do banco com seus números, agências e titulares."""
        for conta in self.contas:
            print(
                f"Número: {conta.numero}, Agência: {conta.agencia}, Titular: {conta.titular.nome}"
            )

    def obter_conta_por_cpf(self, cpf):
        """
        Busca uma conta pelo CPF do titular.

        Args:
            cpf (str): CPF do titular da conta.

        Returns:
            Conta: O objeto Conta se encontrado, None caso contrário.
        """
        for conta in self.contas:
            if conta.titular.cpf == cpf:
                return conta
        return None

    def obter_usuario_por_cpf(self, cpf):
        """
        Busca um usuário pelo CPF.

        Args:
            cpf (str): O CPF do usuário.

        Returns:
            PessoaFisica: O objeto PessoaFisica se encontrado, None caso contrário.
        """
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_usuario_e_conta_se_necessario(banco, cpf):
        """
        Cria um novo usuário e uma nova conta se não existir uma conta com o CPF informado.

        Args:
            cpf (str): O CPF do usuário.

        Returns:
            Conta: A conta criada ou None se o usuário optar por não criar uma conta.
        """
        print(
            "Conta não encontrada. Deseja cadastrar um novo usuário e uma nova conta?"
        )
        menu_aux = menu_yes_or_no()
        if menu_aux == "1":
            print("=== Iniciando a criação do usuário ===")
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            endereco = input("Digite o endereço: ")
            try:
                banco.criar_usuario(nome, cpf, data_nascimento, endereco)
                print("Usuário criado com sucesso!")
                usuario = banco.obter_usuario_por_cpf(cpf)
                if usuario:
                    numero_conta = len(banco.contas) + 1
                    conta = banco.criar_conta(numero_conta, "0001", usuario)
                    print(
                        f"Seja bem-vindo {nome}! Conta criada com sucesso! Número: {numero_conta}"
                    )
                    return conta
            except ValueError as e:
                print(e)
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

    def entrada_por_transferencia(self, valor):
        """
        Efetua ENTRADA por transferencia

        Args:
            valor (float): Valor da transação (ENTRADA por transferencia).

        Returns:
            None.
        """
        self._saldo += valor
        transacao = Transacao(valor, f"(+) ENTRADA por transferencia", self._saldo)
        self.extrato.append(transacao)
        print(f"ENTRADA por transferencia  R$ {valor:.2f} realizado com sucesso!")

    def saida_por_transferencia(self, valor):
        """
        Efetua transação de Retirada de Valor por Transferencia

        Args:
            valor (float): É o valor que será retirado da conta de origem.

        Returns:
            None.
        """
        self._saldo -= valor
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        """if (
            len(
                [
                    t
                    for t in self.extrato
                    if t.tipo == "(-) Saída por Transferência" and t.data.date() == datetime.date.today()
                ]
            )
            >= 3
        ):
            raise ValueError("Limite de saques diários atingido.")"""
        transacao = Transacao(valor, f"(-) Saída por Transferência ", self._saldo)
        self.extrato.append(transacao)
        # print(f"Transferencia para  e de R$ {valor:.2f} realizado com sucesso!")

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

    def transferir(self, valor, conta_destino):
        """
        Transfere um valor para outra conta.

        Args:
            valor (float): Valor da transferência.
            conta_destino (Conta): A conta de destino.

        Raises:
            ValueError: Se o saldo for insuficiente.
        """
        # Verifica se o saldo é maior do que a variável privada self._saldo
        if valor > self._saldo:
            # Se o suario não tiver saldo o Raisen  vai retornar um raise informando que o saldo é insuficiente.
            raise ValueError("Saldo insuficiente para transferência.")
        self.saida_por_transferencia(
            valor
        )  # Usa o método saida_por_transferencia existente para debitar o valor
        conta_destino.entrada_por_transferencia(
            valor
        )  # Usa o método entrada_por_transferencia existente para creditar o valor
        print(
            f"Parabéns {self.titular.nome}Transferência de R$ {valor:.2f} {self.numero} para a conta {conta_destino.numero} realizada com sucesso!"
        )

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
    """
    Representa uma pessoa física com seus dados pessoais.

    Atributos:
        nome (str): Nome da pessoa.
        cpf (str): CPF da pessoa.
        data_nascimento (str): Data de nascimento da pessoa no formato "dd/mm/aaaa".
        endereco (str): Endereço da pessoa.
    """
    def __init__(self, nome, cpf, data_nascimento, endereco):
        """
        Inicializa um novo objeto PessoaFisica.

        Args:
            nome (str): Nome da pessoa.
            cpf (str): CPF da pessoa.
            data_nascimento (str): Data de nascimento da pessoa no formato "dd/mm/aaaa".
            endereco (str): Endereço da pessoa.
        """
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
        valor (float): Valor da transação (positivo para depósitos e recebimento de transferecia, negativo para saques e saida por transferencia, ).
        tipo (str): Tipo da transação ("deposito", "saque", "(-) Saída por Transferência).
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
    [t] Transferência Entre Contas
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

            if not conta:
                conta = banco.criar_usuario_e_conta_se_necessario(cpf)

            if conta:
                try:
                    valor_deposito = float(input("Digite o valor do depósito: "))
                    conta.depositar(valor_deposito)
                except ValueError as e:
                    print(e)

        elif opcao == "s":
            cpf = input("Informe o CPF do usuário: ")
            conta = banco.obter_conta_por_cpf(cpf)

            if not conta:
                conta = banco.criar_usuario_e_conta_se_necessario(cpf)

            if conta:
                try:
                    valor_saque = float(input("Digite o valor do saque: "))
                    conta.sacar(valor_saque)
                except ValueError as e:
                    print(e)

        elif opcao == "t":
            # Solicita o cpf de origem
            cpf_origem = input("Informe o CPF de Origem: ")
            # Obtem a conta de origem
            conta_origem = banco.obter_conta_por_cpf(cpf_origem)
            nome = banco.obter_usuario_por_cpf(cpf_origem)
            # se não houver a conta criada será solicitado a criacao
            if not conta_origem:
                conta = banco.criar_usuario_e_conta_se_necessario(cpf_origem)
                continue

            valor_deposito = input("Digite o valor a ser depositado: ")  #

            cpf_destino = input("Informe o CPF Destino: ")
            conta_destino = banco.obter_conta_por_cpf(cpf_destino)

            if not conta_destino:
                print("Conta de destino não encontrada.")
                continue

            try:
                valor_transferencia = float(valor_deposito)
                conta_origem.transferir(
                    valor_transferencia, conta_destino, conta_origem, nome
                )
            except ValueError as e:
                print(e)

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
