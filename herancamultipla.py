#uma classe pode herdar de multiplas classes em python
#tambem chamada de mixin

class Logavel:
    def __init__(self):
        self.nome_da_classe = ''

    def logar(self, mensagem):
        print('Mensagem da classe' + self.nome_da_classe + ':' + mensagem)
class Conexao:
    def __init__(self):
        self.servidor = ''
    def conectar(self):
        print('Conectando ao banco de dados no servidor' + self.servidor)
        #Lógica para realizar a conxão com o BD

class MySqlDatabase(Conexao, Logavel):
    def __init__(self):
        super().__init__()
        self.nome_da_classe = 'MySqlDatabase'
        self.servidor = 'Meu Servidor'

def framework(item):
    if isinstance(item, Conexao):
        item.conectar()
    if isinstance(item, Logavel):
        mensagem = 'Boa noite, minhas queridas.'
        item.logar(mensagem)

Conexao_mysql = MySqlDatabase()
framework(Conexao_mysql)
