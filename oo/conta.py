class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f"O valor {valor} passou o limite")

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def transfere(self, valor, contaDestino):
        self.saca(valor)
        contaDestino.deposita(valor)

    def __pode_sacar(self, valor):
        return valor <= self.saldo + self.limite

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}