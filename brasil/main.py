from cpf_cnpj import Documento
from telefones_br import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

cpf = Documento.cria_documento("13728469726")
print(cpf)

cnpj = Documento.cria_documento("30306294000145")
print(cnpj)

tel = TelefonesBr("+55 (21)922293110")
print(tel)

data = DatasBr()
print(data)
print(data.tempo_cadastro())

cep = BuscaEndereco("20940060")
print(cep)
print(cep.acessa_via_cep())