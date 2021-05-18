endereco = "Rua de Teste 12, apartamento 123, Bairro Fake, Cidade, UF, 12345-678"

import re

pattern = re.compile("\d{5}-?\d{3}")
search = pattern.search((endereco))

if(search):
    cep = search.group()
    print(cep)