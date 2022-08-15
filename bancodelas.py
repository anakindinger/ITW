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
        self.conta_comum = []
        self.conta_especial = []
        self.cliente = []

    def procurar_cliente(self, nome):
        for i in range(0,len(self.cliente)):
            if self.cliente[i].nome == nome:
                return i
            else:
                print('Cliente não encontrado')

    def procurar_conta_comum(self, nome):
        for i in range(0,len(self.conta_comum)):
            for j in range(0, len(self.conta_comum[i].cliente[j])):
                if self.conta_comum[i].cliente[j].nome == nome:
                    return i
            else:
                print('Cliente não encontrado')

    def procurar_conta_especial(self, nome):
        for i in range(0,len(self.conta_especial)):
            for j in range(0, len(self.conta_especial[i].cliente[j])):
                if self.conta_especial[i].cliente[j].nome == nome:
                    return i
            else:
                print('Cliente não encontrado')                        

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
        self.cliente = cliente
        self.saldo = 0.00

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')   

    def depositar(self, valor):
        self.saldo += valor

    def mostrar_saldo(self):
        return self.saldo

class ContaEspecial(Conta):
    def __init__(self, cliente):
        super().__init__(cliente)

    def sacar(self, valor):
        if (self.saldo - valor) >= -(self.cliente[0].renda_mensal):
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')



banco_delas = Banco()

while True:
    print(
        '''
        1 - Cadastrar cliente
        2 - Alterar dados de cliente
        3 - Vincular nova conta
        4 - Vincular novo titular
        5 - Exibir operações de conta
        6 - Encerrar conta
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
        
        banco_delas.cliente.append(Cliente(nome, telefone, sexo, renda_mensal))

    elif opcao == 2: #ALTERAR DADOS DE CLIENTE
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
            nome_procurar = input('Qual é o nome do cliente que deseja atualizar? ')
            if banco_delas.procurar_cliente(nome_procurar):
                id_cadastro = banco_delas.procurar_cliente(nome_procurar)
                dado_atualizar = input('Digite o dado para atualizar:')
            else:
                print('Não foi possível encontrar o cliente')

           
            if operacao_atualizar >= 1 and operacao_atualizar < 4:
               banco_delas.cliente[id_cadastro].atualizar_cadastro(operacao_atualizar, dado_atualizar)
            
            elif operacao_atualizar == 0:
                break
                
            else:
              print('Operação inválida, digite novamente.')

    elif opcao == 3:#VINCULAR NOVA CONTA
        nome_procurar = input('Qual é o nome do cliente que deseja vincular? ')
        if banco_delas.procurar_cliente(nome_procurar):
            id_cadastro = banco_delas.procurar_cliente(nome_procurar)
            if banco_delas.cliente[id_cadastro].sexo == 'F':
                banco_delas.conta_especial.append(ContaEspecial(banco_delas.cliente[id_cadastro]))
            elif banco_delas.cliente[id_cadastro].sexo == 'M':
                banco_delas.conta_comum.append(Conta(banco_delas.cliente[id_cadastro]))
            else:
                print('Não foi possível vincular a conta, certifique-se de que os dados do cliente estão corretos e o cliente foi cadastrado')   
        else:
            print('Não foi possível encontrar o cliente')

        
    elif opcao == 4:#VINCULAR NOVO TITULAR
        tipo_conta = input('Digite o tipo de conta [Comum/Especial]: ')
        titular_procurar = input('Qual é o 1º titular da conta deseja vincular? ')
        
        
        

    elif opcao == 5:#EXIBIR OPERAÇÕES DE CONTA
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
            tipo_conta = input('Digite o tipo de conta [Comum/Especial]: ')
            titular_procurar = input('Qual é o nome do cliente que fará movimentação? ')
                        
            if operacao_conta == 1:
                if tipo_conta == 'Comum':
                    banco_delas.conta_comum[banco_delas.procurar_conta_comum(titular_procurar)].mostrar_saldo()
                elif tipo_conta == 'Especial':
                    banco_delas.conta_comum[banco_delas.procurar_conta_especial(titular_procurar)].mostrar_saldo()
                else:
                    print('Tipo de conta inválido')

            elif operacao_conta == 2:
                valor_saque = input(float('Insira o valor que deseja sacar: '))
                if tipo_conta == 'Comum':
                    banco_delas.conta_comum[banco_delas.procurar_conta_comum(titular_procurar)].sacar(valor_saque)
                elif tipo_conta == 'Especial':
                    banco_delas.conta_comum[banco_delas.procurar_conta_especial(titular_procurar)].sacar(valor_saque)
                else:
                    print('Tipo de conta inválido')        

            elif operacao_conta == 3:
                valor_deposito = input(float('Insira o valor que deseja depositar: '))
                if tipo_conta == 'Comum':
                    banco_delas.conta_comum[banco_delas.procurar_conta_comum(titular_procurar)].sacar(valor_deposito)
                elif tipo_conta == 'Especial':
                    banco_delas.conta_comum[banco_delas.procurar_conta_especial(titular_procurar)].sacar(valor_deposito)
                else:
                    print('Tipo de conta inválido')

            elif operacao_conta == 0:
                break

            else:
                print('Opção de operação inválida, digite novamente.')            
                
    
    elif opcao == 6:#ENCERRAR CONTA
        
        tipo_conta = input('Digite o tipo de conta [Comum/Especial]: ')
        titular_procurar = input('Qual é o 1º titular da conta deseja encerrar? ')
        if tipo_conta == 'Comum':
            banco_delas.conta_comum.pop(banco_delas.procurar_conta_comum(titular_procurar))
            print('Conta encerrada com sucesso!')
        elif tipo_conta == 'Especial':
            banco_delas.conta_especial.pop(banco_delas.procurar_conta_especial(titular_procurar))
            print('Conta encerrada com sucesso!')
        else:
            print('Conta não localizada')


    if opcao == 0:
        break
    else:
        print('Opção inválida, digite novamente')