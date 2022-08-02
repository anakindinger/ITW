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


class Estacionamento:
    def __init__(self):
        self.vagas_de_carro = 5
        self.vagas_de_moto = 5
        self.carro_para_vaga = ''
        self.moto_para_vaga = ''
        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_moto = 5

    def estacionar_carro(carro, vaga):
        for i in vaga:
            if vaga[i].livre == True and vaga[i].tipo == 'Carro':
                vaga[i].ocupar()
                break
            else:
                print ('Não há vagas disponíveis')
            
    def estacionar_moto(moto, vaga):
        for i in vaga:
            if vaga[i].livre == True and vaga[i].tipo == 'Moto':
                vaga[i].ocupar()
                break
            elif vaga[i].livre == True and vaga[i].tipo == 'Carro':
                vaga[i].ocupar()
                break
            else:
                print ('Não há vagas disponíveis')
        
    def remover_carro(carro):
        return 0

    def remover_moto(carro):
        return 0

    def estado_do_estacionamento(self):
        return

class Vaga:
    def __init__(self, n):
        self.id = n
        self.tipo = ''
        self.livre = True
        self.placa = ''

    def ocupar(self):
        self.livre = False
      
    def desocupar(self):
        self.livre = True


class Veiculo:
    def __init__(self):
        self.placa = ''
        self.estacionado = False
        self.tipo = ''

    def estacionar():
        return 0

    def sair_da_vaga():
        return 0

class Moto(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = 'Moto'

class Carro(Veiculo):
    def __init__(self):
        super().__init__()
        self.tipo = 'Carro'




vagas = []
for i in vagas:
    vagas.append( Vaga(i))

for i in range(0,4):
    vagas[i].tipo = 'Moto'

for i in range(5,9):
    vagas[i].tipo = 'Carro'

estacionamento = Estacionamento()