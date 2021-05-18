url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url = url.strip()
if(url == ""):
    raise ValueError("A URL está vazia")

if(url.__contains__("?")):
    indice = url.find("?")
    print(indice)

    url_base = url[0:indice]
    url_parametros = url[indice+1:]
    print(url)
    print(url_base)
    print(url_parametros)

    parametro_busca = 'moedaOrigem'
    indice_parametro = url_parametros.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    indice_e_comercial = url_parametros.find('&', indice_valor)
    if indice_e_comercial == -1:
        valor = url_parametros[indice_valor:]
    else:
        valor = url_parametros[indice_valor:indice_e_comercial]
    print(valor)



[url_base, url_parametros] = url.split("?")
parametros = url_parametros.split("&")
print(url)
print(url_base)
print(url_parametros)
print(parametros)