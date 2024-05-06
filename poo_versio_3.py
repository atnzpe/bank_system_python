

# Importa a biblioteca date time
import datetime

# Cria a classe Banco


class Banco:
    def __init__(self):
        # Inclui os atributos conta e usuario
        self.contas = []
        self.usuarios = []

    # Função para criar conta com os atributos numero, agencia, titular
    def criar_conta(self, numero, agencia, titular):
        # Seta a variável conta como o objeto Conta
        conta = Conta(numero, agencia, titular)
        # Adiciona o Objeto conta, a lista self.contas
        self.contas.append(conta)
        # retorna a variável conta
        return conta

    def criar_usuario(self, nome, cpf, data_nascimento, endereco):
        if self.obter_usuario_por_cpf(cpf):
            raise ValueError("Usuário já cadastrado com esse CPF.")
        usuario = PessoaFisica(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(usuario)
        return usuario

    def listar_contas(self):
        for conta in self.contas:
            print(f"Número: {conta.numero}, Agência: {conta.agencia}, Titular: {conta.titular.nome}")

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
        transacao = Transacao(valor, "deposito")
        self.extrato.append(transacao)
        self._saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        if len([t for t in self.extrato if t.tipo == "saque" and t.data.date() == datetime.date.today()]) >= 3:
            raise ValueError("Limite de saques diários atingido.")
        transacao = Transacao(valor, "saque")
        self.extrato.append(transacao)
        self._saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def exibir_extrato(self):
        print("-" * 30)
        print(f"Extrato da conta {self.numero}")
        print("-" * 30)
        for transacao in self.extrato:
            print(f"{transacao.data} - {transacao.tipo}: R$ {transacao.valor:.2f}")
        print(f"Saldo: R$ {self._saldo:.2f}")
        print("-" * 30)


class PessoaFisica:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco


class Transacao:
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo
        self.data = datetime.datetime.now()


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

# Menu auxiliar para escolha de sim ou não


def menu_yes_or_no():
    menu_yes_or_no = """
    Sim ou Não?
    [s] SIM
    [n] NÂO
    ->"""
    return input(menu_yes_or_no)


#menu_aux = menu_yes_or_no()


def main():
    banco = Banco()  # Cria um objeto Banco

    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do usuário: ")
            conta = banco.obter_conta_por_cpf(cpf)

            if conta:
                try:
                    valor_deposito = float(
                        input("Digite o valor do depósito: "))
                    conta.depositar(valor_deposito)
                except ValueError as e:
                    print(e)
            else:
                input("Conta não encontrada. Deseja criar uma conta? ")
                print(menu_aux)
                pass

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
                print("Conta não encontrada.")

        elif opcao == "e":
            cpf = input("Informe o CPF do usuário: ")
            conta = banco.obter_conta_por_cpf(cpf)

            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "u":
            nome = input("Digite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            data_nascimento = input(
                "Digite a data de nascimento (dd/mm/aaaa): ")
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
                print("Usuário não encontrado.")

        elif opcao == "l":
            banco.listar_contas()

        elif opcao == "q":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


main()
