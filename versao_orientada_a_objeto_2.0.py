# Cria uma Class chamada Cliente
class Cliente:
    # atributos
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

#Class Pessoa Fisica que usa Heranca de CLiente
class PessoaFisica(Cliente):

    def __init__(self, nome, data_nascimento, cpf, endereco):
        # importa o atributo da class Cliente como herança
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

#Class usada para gerenciar usuario filtro e validadaçoes de duplicida
class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def criar_usuario(self):
            # Usuarios
            if any(usuario.cpf == self.cpf for usuario in self.usuarios):
                print("Usuário já cadastrado")
                return
            
            
            nome = input("Seu nome Completo é: ")
            data_nascimento = input(
                "Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input(
                "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
                )

            novo_usuario = PessoaFisica(nome, data_nascimento,self.cpf,endereco)
            self.usuarios.append(novo_usuario)
            print("=== Usuário criado com sucesso! ===")  # Imprima aqui
            print(self.usuarios)
            
    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
            return None
        
        