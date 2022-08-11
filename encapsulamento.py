#tecnica para ocultar detalhes internos
#_protegido = não devem ser acessados pelo mundo externo, com ressalvas
#__privados = não devem ser acessados de forma nenhuma

#@property -> getter e setter

from http.client import NON_AUTHORITATIVE_INFORMATION
from mailbox import NotEmptyError


class Pessoa:
    def __init__(self, nome, profissao, identidade):
        self._nome = nome
        self.profissao = profissao
        self.__identidade = identidade

    def __str__(self) -> str:
        return f'Nome: {self._nome}, Profissão: {self.profissao} Identidade: {self.__identidade}'
    
   
pessoa1 = Pessoa('Ana', 'Programadora', '123456')
print(pessoa1)

#ao tentar alterar um atributo público, o valor é alterado
pessoa1.profissao = 'Médica'
print(pessoa1)

#o protegido é alterado caso seja colocado o _ ao fazer a alteração
pessoa1._nome = 'Beatriz'
print(pessoa1)

#ao tentar alterar um atributo privado, o valor não é alterado
pessoa1.__identidade = '22340'
print(pessoa1)

