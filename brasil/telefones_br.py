import re
class TelefonesBr:
    def __init__(self, telefone):
        if(self.valida_telefone(telefone)):
            self.telefone = telefone
        else:
            raise ValueError("Telefone incorreto")

    def __str__(self):
        padrao = "[+]?(\d{2,3})?[ ]?[(]?(\d{2})[)]?[ ]?(\d{4,5})[-]?(\d{4})"
        resposta = re.match(padrao, self.telefone)
        codigo_pais = resposta.group(1) if resposta.group(1) != None else "55"
        return f"+{codigo_pais} ({resposta.group(2)}) {resposta.group(3)}-{resposta.group(4)}"

    def valida_telefone(self, telefone):
        padrao = "[+]?(\d{2,3})?[ ]?[(]?\d{2}[)]?[ ]?\d{4,5}[-]?\d{4}"
        resposta = re.fullmatch(padrao, telefone)
        if(resposta):
            return True
        else:
            return False

