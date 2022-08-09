#REQUISITOS
# O estacionamento é um pátio de apenas um andar e possui 50 vagas
# Há 5 vagas para carros e 5 para motos, as vagas de carro são maiores que de moto
# Carros e motos são identificados por suas placas
# Vagas são identificadas por um número identificador único
# Carros só podem ser estacionados em vagas de carro
# Motos preferencialmente são estacionadas em vagas de motos, se não houverem vagas
#disponíveis, podem ocupar vagas de carros
# É preciso ter controle sobre qual carros está em qual vaga para agilizar a saída quando
#o dono vem buscar
# É preciso saber o número de vagas livres de carro e de moto para que o estacionamento
#saiba se podem entrar novos carros e motos


from asyncio.windows_events import NULL
from msilib.schema import Property


class Estacionamento:
    def __init__(self, vc, vm):
        self.vagas_de_carro = vc
        self.vagas_de_moto = vm
        
    def estacionar_carro(vaga, veiculo):
        for i in vaga:
            if vaga[i].livre == True:
                vaga[i].ocupar(veiculo)
                veiculo.estacionar()
                return True 
            else:
                print ('Não há vagas disponíveis')
        

    def estacionar_moto(vaga, veiculo):
        for i in vaga:
            if vaga[i].livre == True and vaga[i].tipo == 'Moto':
                vaga[i].ocupar(veiculo)
                break
            elif vaga[i].livre == True and vaga[i].tipo == 'Carro':
                vaga[i].ocupar(veiculo)
                break
            else:
                print ('Não há vagas disponíveis')
        
    def remover_veiculo(i, vaga):
        vaga[i].desocupar()

    def encontrar_veiculo(placa, vagas):
        for i in range(0, vagas.len()):
            if placa == vagas[i].veiculo.placa:
                return i
            else:
                print('Veiculo não encontrado!')

    def estado_do_estacionamento(self):
        return

class Vaga:
    def __init__(self, num_id):
        self.id = num_id
        self.tipo = ''
        self.livre = True
        self.veiculo = Veiculo()

    def ocupar(self, veiculo):
        self.livre = False
        self.veiculo = veiculo
        
    def desocupar(self, num_id):
        if num_id == self.id:
            self.livre = True
            self.veiculo = ''

    #@Property
    def definir_tipo(self, nome_tipo):
        self.tipo = nome_tipo

    def __str__(self):
        return f'dsfnsdl'


class Veiculo:
    def __init__(self):
        self.placa = ''
        self.estacionado = False
        self._tipo = ''

    def cadastrar(self, num_placa, tipo):
        self.placa = num_placa
        self._tipo = tipo

    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False

    def __str__(self):
        return f'Placa do carro: {self.placa}, estacionado? {self.estacionado}'

#inicializando o estacionamento com a quantidade de vagas para cada tipo de veículo
estacionamento = Estacionamento(int(input("Digite a quantidade de vagas de carro: ")), int(input("Digite a quantidade de vagas de moto: ")))

#inicializado as vagas com seu id numérico e sequencial
vagas = []
for  i in range(int(estacionamento.vagas_de_carro + estacionamento.vagas_de_moto)):
    vagas.append(Vaga(i))

#definindo os tipos, no inicio da lista com as motos e em seguida 
for i in range(0,estacionamento.vagas_de_moto-1):
    vagas[i].definir_tipo('Moto')

for i in range(estacionamento.vagas_de_moto, estacionamento.vagas_de_moto + estacionamento.vagas_de_carro - 1):
    vagas[i].definir_tipo('carro')

#inicializando os veiculos
veiculos = []

while True:

    print('1 - cadastrar veículo:')
    print('2 - Estacionar carro: ')
    print('3 - Estacionar moto: ')
    print('4 - Remover veiculo: ')
    print('5 - Pesquisar veículo')
    print('0 - Sair')
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':#cadastrar veiculo
        veiculos.append(Veiculo())
        placa = input('Digite a placa: ')
        while True:
            tipo = input('Digite o tipo [Carro/Moto]:')
            if placa != 'Carro' or placa != 'Moto':
                print('Tipo inválido!')
            else:
                break    
        veiculos[-1].cadastrar(placa, tipo)
        #print(veiculos[-1])
        
    elif opcao == '2':#estacionar carro
        if veiculos[-1]._tipo == 'Carro':
            estacionamento.estacionar_carro(vagas, veiculos[-1])
        else:
            print('Veículo não é carro, digite a opção correta') 
    
    elif opcao == '3':#estacionar moto
        if veiculos[-1].tipo == 'Moto':
            estacionamento.estacionar_moto(vagas, veiculos[-1])
        else:
            print('Veículo não é moto, digite a opção correta')
        

    elif opcao == '4':#remover veiculo
        placa = input('Digite a placa do veículo que vai sair da vaga: ')
        vagas[estacionamento.encontrar_veiculo(placa, vagas)].desocupar()

        



        

    elif opcao == '5':#pesquisar veiculo

        continue

    elif opcao == '0':
        break

    else:
        print('Opção inválida!')    