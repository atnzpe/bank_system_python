lista_usuarios = []

class Conta:
    def __init__(self, saldo, nr_conta):
        self.saldo = saldo
        self.nr_conta = nr_conta

    def depositar(self):
        pass

    def sacar(self):
        pass


class Usuario:
    
    def __init__(self,cpf):
        #self.nome = nome
        self.cpf = cpf
        #self.dt_nasc = dt_nasc
        #self.endereco = endereco
         
        
        

    def criar_usuario(self, usuarios):
        # Usuarios
        usuarios = lista_usuarios
        cpf = self.cpf
        usuario = self.filtrar_usuario(cpf, usuarios)
        
        if usuario:
            print(' Usuario ja cadastrado')
            return
        else:
            nome = input('Seu nome Completo é: ')
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input(
                "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                         "cpf": cpf, "endereco": endereco})
        print("=== Usuário criado com sucesso! ===")  # Imprima aqui
        print(usuarios)
    def filtrar_usuario(self, cpf, usuarios):
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                return usuario
        return None


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
        -> """  # Removido o texto "Digite uma opção:"
        return input(menu)

    # Variaveis
    # Limite de saques dia
    LIMITE_SAQUES = 3
    # AGENCIA
    AGENCIA = "0001"
    #usuarios = []
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
            #usuarios = usuarios
            cpf = input('Digite o cpf (apenas numeros): ')
            #nome = input('Seu nome Completo é: ')
            #data_nascimento = input(
            #    "Informe a data de nascimento (dd-mm-aaaa): ")
            #endereco = input(
            #    "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            #usuario = int(cpf)
            novo_usuario = Usuario(cpf)
            novo_usuario.criar_usuario(cpf)  # Não é necessário passar o CPF aqui

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
