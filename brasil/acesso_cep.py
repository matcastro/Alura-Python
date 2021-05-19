import requests
class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if(self.cep_valido(cep)):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return f"{self.cep[0:5]}-{self.cep[5:8]}"

    def cep_valido(self, cep):
        if(len(cep) == 8):
            return True
        else:
            return False

    def acessa_via_cep(self):
        r = requests.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        dados = r.json()
        return {
            "cep": dados['cep'],
            "logradouro": dados['logradouro'],
            "complemento": dados['complemento'],
            "bairro": dados['bairro'],
            "localidade": dados['localidade'],
            "uf": dados['uf'],
            "ibge": dados['ibge'],
            "gia": dados['gia'],
            "ddd": dados['ddd'],
            "siafi": dados['siafi']
        }