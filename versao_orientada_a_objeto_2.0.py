# Cria uma Class chamada Cliente
class Cliente:
    # atributos
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

# Class Pessoa Fisica que usa Heranca de CLiente


class PessoaFisica(Cliente):

    def __init__(self, nome, data_nascimento, cpf, endereco):
        # importa o atributo da class Cliente como herança
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class UsuarioJaCadastradoError(Exception):
    pass

# Class usada para gerenciar usuario filtro e validadaçoes de duplicida


class GerenciadorUsuarios:
    def __init__(self):
        # armazena os usuários em um Dicionario
        self.usuarios = {}

    def criar_usuario(self, cpf):
        # Cria uma funçõa para validar se oCPF é válido e possui 11 digitos
        def validar_cpf(cpf):
            return cpf.isdigit() and len(cpf) == 11  # Validação básica

        if not validar_cpf(cpf):
            print("CPF inválido. Por favor, digite apenas números com 11 dígitos.")
            return False

        if cpf in self.usuarios:
            raise UsuarioJaCadastradoError(
                "Usuário já cadastrado com esse CPF.")

        nome = input("Seu nome Completo é: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input(
            "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        # Cria um objeto PessoaFisica
        novo_usuario = PessoaFisica(nome, data_nascimento, cpf, endereco)
        self.usuarios[cpf] = novo_usuario  # Adiciona ao dicionário

        print("=== Usuário criado com sucesso! ===")
        return True

    def obter_usuario(self, cpf):
        return self.usuarios.get(cpf)

    def filtrar_usuario(self, cpf):
        return cpf in self.usuarios


def main():

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
        ->  """  # Removido o texto "Digite uma opção:"
        return input(menu)

    # Variaveis
    # Limite de saques dia
    LIMITE_SAQUES = 3

    # usuarios = []
    # Saldo incial zero
    saldo = 0
    # Limite de valor por saque
    limite_por_saque = 500
    # Texto Extrato
    extrato = ""
    # Contador Saque Diário
    numero_saques = 0
    # Usuarios

    # Contas
    contas = []
    # linha
    linha = ""

    # Cria o Loop While com True
    while True:
        opcao = menu()

        if opcao == "d":
            pass

        elif opcao == "s":
            pass
        elif opcao == "e":
            pass

        elif opcao == "u":
            # Pede o CPF paara checar se o cliente pessoa fisica esta cadstrado
            cpf = input("Digite o cpf (apenas numeros): ")
            # cria uma variavel chamada gerenciador de usuarios
            gerenciador_usuarios = GerenciadorUsuarios()

            try:
                # if gerenciador usuarios igual a true
                if gerenciador_usuarios.criar_usuario(cpf):
                    # exiba a mensagem
                    print("Seja Bem vindo!")
                else:
                    print("Tente novamente")

            # Obter o usuário (se existir)
                usuario = gerenciador_usuarios.obter_usuario(cpf)
                if usuario:
                    print(f"Nome do usuário: {usuario.nome}")
            except UsuarioJaCadastradoError as e:
                print(e)  # Exibe a mensagem da exceção

        elif opcao == "n":
            pass

        elif opcao == "l":
            pass

        elif opcao == "q":
            print("Sair")
            break
        else:
            print(f"===ATENÇÃO===\nVocê digitou {opcao}")
            print("\nPor favor, digite um Opção válida!\n")


main()
