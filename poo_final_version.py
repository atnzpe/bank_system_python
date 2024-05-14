"""
Módulo que gerencia um sistema bancário simples.
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

    def criar_usuario_se_necessario(self, cpf):
        """Cria um novo usuário se não existir um com o CPF informado."""
        if not self.obter_usuario_por_cpf(cpf):
            print("=== Iniciando a criação do usuário ===")
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            endereco = input("Digite o endereço: ")
            try:
                self.criar_usuario(nome, cpf, data_nascimento, endereco)
                print("Usuário criado com sucesso!")
                return self.obter_usuario_por_cpf(cpf)
            except ValueError as e:
                print(e)
        return None

    def criar_conta_para_usuario(self, usuario):
        """Cria uma nova conta para o usuário informado."""
        numero_conta = len(self.contas) + 1
        conta = self.criar_conta(numero_conta, "0001", usuario)
        print(
            f"Seja bem-vindo {usuario.nome}! Conta criada com sucesso! Número: {numero_conta}"
        )
        return conta


class Conta:
    """
    Representa uma conta bancária com suas informações e operações.

    Atributos:
        numero (int): Número da conta.
        agencia (str): Agência da conta.
        titular (PessoaFisica): O titular da conta (objeto PessoaFisica).
        _saldo (float): Saldo da conta (privado).
        extrato (list): Lista de objetos Transacao representando o histórico de transações da conta.
    """

    def __init__(self, numero, agencia, titular, saldo=0):
        """
        Inicializa um novo objeto Conta.

        Args:
            numero (int): Número da conta.
            agencia (str): Agência da conta.
            titular (PessoaFisica): O titular da conta (objeto PessoaFisica).
            saldo (float, optional): Saldo inicial da conta. Defaults to 0.
        """
        self.numero = numero
        self.agencia = agencia
        self.titular = titular
        self._saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        """
        Realiza um depósito na conta.

        Args:
            valor (float): Valor a ser depositado.

        Returns:
            None
        """
        if valor > 0:
            self._saldo += valor
            transacao = Transacao(valor, "(+) Deposito", self._saldo)
            self.extrato.append(transacao)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            raise ValueError("O valor do depósito deve ser positivo.")

    def entrada_por_transferencia(self, valor):
        """
        Registra uma entrada de valor por transferência.

        Args:
            valor (float): Valor recebido por transferência.

        Returns:
            None
        """
        if valor > 0:
            self._saldo += valor
            transacao = Transacao(valor, f"(+) ENTRADA por transferencia", self._saldo)
            self.extrato.append(transacao)
            print(f"ENTRADA por transferencia  R$ {valor:.2f} realizado com sucesso!")
        else:
            raise ValueError("O valor da transferência deve ser positivo.")

    def saida_por_transferencia(self, valor):
        """
        Realiza uma retirada de valor por transferência.

        Args:
            valor (float): Valor a ser transferido para outra conta.

        Returns:
            None

        Raises:
            ValueError: Se o saldo for insuficiente para a transferência.
        """
        if valor > 0:
            if self._saldo >= valor:
                self._saldo -= valor
                transacao = Transacao(
                    valor, f"(-) Saída por Transferência ", self._saldo
                )
                self.extrato.append(transacao)
            else:
                raise ValueError("Saldo insuficiente.")
        else:
            raise ValueError("O valor da transferência deve ser positivo.")

    def sacar(self, valor):
        """
        Realiza um saque da conta.

        Args:
            valor (float): Valor a ser sacado.

        Returns:
            None

        Raises:
            ValueError: Se o saldo for insuficiente ou se o limite de saques
                        diários for atingido.
        """
        if valor > 0:
            if self._saldo >= valor:
                if (
                    len(
                        [
                            t
                            for t in self.extrato
                            if t.tipo == "(-) Saque"
                            and t.data.date() == datetime.date.today()
                        ]
                    )
                    >= 3
                ):
                    raise ValueError("Limite de saques diários atingido.")
                self._saldo -= valor
                transacao = Transacao(valor, "(-) Saque", self._saldo)
                self.extrato.append(transacao)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                raise ValueError("Saldo insuficiente.")
        else:
            print("O valor do saque deve ser positivo.")

    def transferir(self, valor, conta_destino):
        """
        Transfere um valor para outra conta.

        Args:
            valor (float): Valor a ser transferido.
            conta_destino (Conta): A conta para a qual o valor será transferido.

        Raises:
            ValueError: Se o saldo da conta de origem for insuficiente para
                        realizar a transferência.
        """
        if valor > 0:
            if valor <= self._saldo:
                self.saida_por_transferencia(valor)
                conta_destino.entrada_por_transferencia(valor)
                print(
                    f"Parabéns {self.titular.nome}! Transferência de R$ {valor:.2f} da conta {self.numero} para a conta {conta_destino.numero} realizada com sucesso!"
                )
            else:
                raise ValueError("Saldo insuficiente para transferência.")
        else:
            print("O valor da transferência deve ser positivo.")

    def formatar_extrato(self):
        """Retorna o extrato formatado como uma string."""
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

        resultado =  f"{e.center(30, '=')}\n"
        resultado += "-" * 30 + "\n"
        resultado += "DADOS DA CONTA\n"
        resultado += "-" * 30 + "\n"
        resultado += text + "\n"
        resultado += "-" * 30 + "\n"
        resultado += text_registro_transacao.center(30, "=") + "\n"
        resultado += "-" * 30 + "\n"
        
        if not self.extrato:
            resultado += "Não foram realizadas movimentações.\n"
        else:
            for transacao in self.extrato:
                resultado += f"{transacao.data} - {transacao.tipo}: R$ {transacao.valor:.2f} - Saldo: R$ {transacao.saldo:.2f}\n"
        resultado += "-" * 30 + "\n"
        resultado += f"Saldo Final: R$ {self._saldo:.2f}\n"
        resultado += "-" * 30 + "\n"
        
        return resultado

    def exibir_extrato(self):
        """Exibe o extrato da conta."""
        print(self.formatar_extrato())


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
    Classe que armazena dados sobre as transações realizadas.
    """

    def __init__(self, valor, tipo, saldo):
        """
        Inicializa um objeto Transacao com informações sobre a transação realizada.

        Args:
            valor (float): Valor da transação (positivo para depósitos e recebimento de transferecia, negativo para saques e saida por transferencia, ).
            tipo (str): Tipo da transação ("deposito", "saque", "(-) Saída por Transferência").
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
    """
    Exibe o menu de opções do sistema bancário para o usuário.

    Returns:
        str: A opção escolhida pelo usuário.
    """
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


def menu_yes_or_no():
    """
    Exibe um menu para o usuário escolher entre "Sim" e "Não".

    Returns:
        str: A opção escolhida pelo usuário ("1" para Sim, "0" para Não).
    """
    menu_yes_or_no = """
    Escolha Sim ou Não?
    [1] SIM
    [0] NÂO
    ->  """
    return input(menu_yes_or_no)


# Função principal do programa. Gerencia as operações bancárias.


def main():
    """
    Função principal do sistema bancário. Gerencia as operações e interações com o usuário.
    """
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
                conta = banco.criar_conta_para_usuario(cpf)

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
                conta = banco.criar_conta_para_usuario(cpf)

            if conta:
                try:
                    valor_saque = float(input("Digite o valor do saque: "))
                    conta.sacar(valor_saque)
                except ValueError as e:
                    print(e)

        elif opcao == "t":
            # Solicita o cpf da conta de origem
            cpf_origem = input("Informe o CPF de Origem: ")
            # Obtém a conta de origem a partir do CPF
            conta_origem = banco.obter_conta_por_cpf(cpf_origem)

            # Se a conta de origem não for encontrada, oferece a opção de criar uma nova conta
            if not conta_origem:
                conta = banco.criar_conta_para_usuario(cpf_origem)
                continue  # Volta para o início do loop do menu

            # Solicita o valor da transferência
            valor_deposito = input("Digite o valor a ser transferido: ")

            # Solicita o CPF da conta de destino
            cpf_destino = input("Informe o CPF Destino: ")
            # Obtém a conta de destino a partir do CPF
            conta_destino = banco.obter_conta_por_cpf(cpf_destino)

            # Se a conta de destino não for encontrada, exibe uma mensagem e volta para o menu
            if not conta_destino:
                print("Conta de destino não encontrada.")
                continue

            # Tenta realizar a transferência
            try:
                valor_transferencia = float(valor_deposito)
                conta_origem.transferir(valor_transferencia, conta_destino)
            except ValueError as e:
                print(
                    e
                )  # Exibe a mensagem de erro caso ocorra algum problema na transferência

        elif opcao == "e":
            cpf = input("Informe o CPF do usuário: ")
            conta = banco.obter_conta_por_cpf(cpf)

            if conta:
                conta.exibir_extrato()
            else:
                usuario = banco.criar_usuario_se_necessario(cpf)
                if usuario:  # Verifica se o usuário foi criado com sucesso
                    conta = banco.criar_conta_para_usuario(usuario)
                    conta.exibir_extrato()

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

            if not usuario:
                usuario = banco.criar_usuario_se_necessario(cpf)

            if usuario:
                conta = banco.criar_conta_para_usuario(usuario)

        elif opcao == "l":
            banco.listar_contas()

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
