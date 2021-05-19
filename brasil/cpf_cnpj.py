from validate_docbr import CPF
from validate_docbr import CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if(len(documento) == 11):
            return (DocCpf(documento))
        elif (len(documento) == 14):
            return (DocCnpj(documento))
        else:
            raise ValueError("Quantidade de digitos inválida!")

class DocCpf:
    def __init__(self, documento):
        cpf = str(documento)
        if(self.cpf_eh_valido(cpf)):
            self.cpf = cpf
        else:
            raise ValueError("CPF Inválido!")

    def __str__(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


    def cpf_eh_valido(self, cpf):
        if(len(cpf) == 11):
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos inválida!")

class DocCnpj:
    def __init__(self, documento):
        cnpj = str(documento)
        if (self.cnpj_eh_valido(cnpj)):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ Inválido!")

    def __str__(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def cnpj_eh_valido(self, cnpj):
        if(len(cnpj) == 14):
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos inválida!")