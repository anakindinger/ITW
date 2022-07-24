#definição da classe
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 3
        self.canal_min = 1
        self.canal_max = 90
        self.volume = 30
        self.volume_min = 0
        self.volume_max = 100

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def mudar_canal_para_cima(self):
        if not self.ligada:
            return
        if self.canal < self.canal_max:
            self.canal += 1
    
    def mudar_canal_para_baixo(self):
        if not self.ligada:
            return
        if self.canal > self.canal_min:
            self.canal -= 1
    
    def aumenter_volume(self):
        if not self.ligada:
            return
        if self.volume < self.volume_max:
            self.volume += 10

    def diminuir_volume(self):
        if not self.ligada:
            return
        if self.volume > self.volume_min+10:
            self.volume -= 10

    def deixar_mudo(self):
        if not self.ligada:
            return
        if self.volume > self.volume_min:
            self.volume = 0

    def __str__(self) -> str:
        return f'Televisao - ligada {self.ligada} - canal {self.canal} - volume {self.volume}'


# Criando instancias da class Televisao
tv_sala = Televisao()
tv_quarto = Televisao()

tv_sala.ligar()
print('tv_sala está ligada? {}'.format(tv_sala.ligada))
print('tv_quarto está ligada? {}'.format(tv_quarto.ligada))

for _ in range(3):
    tv_sala.aumenter_volume()

print('tv_sala volume: {}'.format(tv_sala.volume))
print('tv_quarto volume: {}'.format(tv_quarto.volume))

#imprimir o conteudo do objeto
print('tv_sala: ', tv_sala)
print('tv_quarto: ', tv_quarto)