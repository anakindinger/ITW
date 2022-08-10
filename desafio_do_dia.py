class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = ""
        self.modelo = ""
        self.velocidade = 0
    
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def acelerar(self):
        if not self.ligado:
            return
        self.velocidade += 1
    
    def desacelerar(self):
        if not self.ligado:
            return
        if self.velocidade > 0:
            self.velocidade -= 1

    def __str__(self) -> str:
        return f'Carro - ligado {self.ligado} - cor {self.cor} - modelo {self.modelo} - velocidade {self.velocidade}'

carro_familia = Carro()
carro_familia.modelo = 'Celta'
carro_familia.cor = 'Prata'
carro_familia.ligar()
for _ in range(40):
    carro_familia.acelerar()
print('velocidade antes de parar: {}'.format(carro_familia.velocidade))
for _ in range(carro_familia.velocidade):
    carro_familia.desacelerar()
print('velocidade depois de parar: {}'.format(carro_familia.velocidade))
print(carro_familia)