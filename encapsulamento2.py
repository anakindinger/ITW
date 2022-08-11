#Geter = retorna o valor
#Setter = definir ou atualizar o valor

class Retangulo:
    def __init__(self, alt, larg):
        self.altura = alt
        self.largura = larg

    @property
    def altura(self):
        print('Getter de altura: ')
        return self.__alt

    @altura.setter
    def altura(self, valor):
        print('Setter de altura: ')

        if valor < 0:
            raise ValueError()
        self.__alt = valor

    @property
    def largura(self):
        print('Getter da largura: ')
        return self.__larg

    @largura.setter
    def largura(self, valor):
        print('Setter de largura: ')

        if valor < 0:
            raise ValueError()
        self.__larg = valor

    def area(self):
        return self.largura * self.altura


quadrado = Retangulo(4,4)
quadrado.altura = 3
quadrado.largura = 2

print(quadrado.altura)

print(quadrado.area())