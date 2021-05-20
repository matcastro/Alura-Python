import sys
from excecoes import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propoe_lance(self, leilao, valor):
        if(valor > self.__carteira):
            raise LanceInvalido("Não pode propor um lance como valor maior que o valor da carteira!")
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance: Lance):
        if(not self.lances or
                self.lances[-1].usuario != lance.usuario and self.lances[-1].valor < lance.valor):
            if (not self.lances):
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise LanceInvalido("Erro ao propor lance")

