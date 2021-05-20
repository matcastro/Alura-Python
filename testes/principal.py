from dominio import Usuario, Lance, Leilao

gui = Usuario("Gui")
yuri = Usuario("Yuri")

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao("Celular")
leilao.propoe(lance_do_yuri)
leilao.propoe(lance_do_gui)

for lance in leilao.lances:
    print(f"O usuario {lance.usuario.nome} deu um lance de {lance.valor}")

print(f"O maior lance foi {leilao.maior_lance} e o menor lance foi {leilao.menor_lance}")