import re
from decimal import Decimal

class ExtratorUrl:
    def __init__(self, url):
        self.__url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.__url)

    def __str__(self):
        return self.__url

    def __eq__(self, other):
        return self.__url == other.url

    def sanitiza_url(self, url):
        if(type(url) == str):
            return url.strip()
        return ""

    @property
    def url(self):
        return self.__url

    def valida_url(self):
        if not (self.__url):
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.__url)

        if not (match):
            raise ValueError("A URL é valida")

    def get_url_base(self):
        indice_interrogacao = self.__url.find("?")
        url_base = url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.__url.find("?")
        url_base = self.__url[indice_interrogacao+1:]
        return url_base

    def get_valor_parametro(self, parametro_busca):
        url_parametros = self.get_url_parametros()
        indice_parametro = url_parametros.find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = url_parametros.find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = url_parametros[indice_valor:]
        else:
            valor = url_parametros[indice_valor:indice_e_comercial]
        return valor

VALOR_DOLAR = Decimal(5.5)
url_busca = "https://www.bytebank.com/cambio?moedaOrigem=dolar&moedaDestino=real&quantidade=100"
extrator = ExtratorUrl(url_busca)
extrator2 = ExtratorUrl(url_busca)

moeda_destino = extrator.get_valor_parametro("moedaDestino")
quantidade = extrator.get_valor_parametro("quantidade")
moeda_origem = extrator.get_valor_parametro("moedaOrigem")

if moeda_origem == "real" and moeda_destino == "dolar":
    valor_conversao = int(quantidade) / VALOR_DOLAR
    print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
elif moeda_origem == "dolar" and moeda_destino == "real":
    valor_conversao = int(quantidade) * VALOR_DOLAR
    print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
print(f"O tamanho da URL é {len(extrator)}")
print(extrator)
print(extrator == extrator2)