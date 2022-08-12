# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas paraclientes mulheres.
# # Modele um sistema orientado a objetos para representar contas correntes em do BancoDelas seguindo os requisitos abaixo.
# #
# # 1. Cada conta corrente pode ter um ou mais clientes como titular.
# #
# # 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# #
# # 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
# #    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela
# #    fizer um depósito, aumentaremos o saldo.
# #
# # 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à suarenda
# #    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até -renda_mensal.
# #
# # 5. Clientes homens por enquanto não têm direito a cheque especial.
# #
# # Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e"polimorfismo".
# # Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classeabstrata".
# #  no item 4 é onde provavelmente vai ser usado o polimorfismo

import uuid

class Banco:
    def __init__(self):
        self.conta_comum = Conta()
        self.conta_especial = ContaEspecial()
        self.clientes = Cliente()

 class Cliente:
    def __init__(self, nome, telefone, sexo, renda_mensal):
        self._nome = nome
        self.telefone = telefone
        self.__sexo = sexo
        self._renda_mensal = renda_mensal

    @property
    def sexo(self):
        return self.__sexo

    @property
    def renda_mensal(self):
        return self._renda_mensal

    def atualizar_cadastro(self, op, dado):
        if op == 1:
            self.nome = str(dado)
        elif op == 2:
            self.telefone = str(dado)
        elif op == 3:
            self.renda_mensal = float(dado)



class Conta:
    def __init__(self, cliente):
        self.id_conta: uuid()
        self.clientes = Cliente()

    def sacar(self, valor):
        return 0

    def depositar(self, valor):
        return 0

    def mostrar_saldo(self):
        return 0

class ContaEspecial(Conta):
    def __init__(self, cliente):
        super().__init__(cliente)

    def sacar(self):
        return 0


contas = []
contas_especiais = []
clientes = []
banco_delas = Banco()

while True:
    print(
        '''
        1 - Cadastrar cliente
        2 - Alterar dados de cliente
        3 - Vincular nova conta
        4 - Exibir operações de conta
        5 - Encerrar conta
        '''
    )
    opcao = int(input('\nDigite a opção desejada: '))
    
    if opcao == 1: #CADASTRAR CLIENTE
        nome = str(input('Digite o nome completo do cliente:'))
        telefone = str(input('Digite o telefone do cliente:'))
        while True:
            sexo = str(input('Digite o sexo do cliente [F/M]:'))
            if sexo != 'F' and sexo != 'M':
                print('Campo inválido, digite F para feminino e M para masculino.')
            else:
                break
        renda_mensal = float(input('Digite a renda mensal do cliente:'))
        
        clientes.append(Cliente(nome, telefone, sexo, renda_mensal))

    elif opcao == 2:
        while True:
            operacao_atualizar = int(input('\nDigite a opção desejada: '))
            print(
                '''
                    Escolha o dado que deseja atualizar:
                    1 - Nome
                    2 - Telefone
                    3 - Renda Mensal
                    0 - Sair
                '''
            )

            if operacao_atualizar == range(1,3):
               clientes[cliente]
            
            elif else:
                print('Operação inválida, digite novamente.')
        
    elif opcao == 4:
        while True:
            print(
                '''
                1 - Consultar saldo
                2 - Realizar saque
                3 - Realizar depósito
                0 - Sair
                '''
            )
            operacao_conta = int(input('\nDigite a operacao desejada: '))
            
            if operacao_conta == 0:
                break
            else:
                print('Operação inválida, digite novamente.')
    
    




    if opcao == 0:
        break
    else:
        print('Opção inválida, digite novamente')