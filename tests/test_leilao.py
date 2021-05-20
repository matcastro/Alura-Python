from unittest import TestCase
from dominio import Usuario, Lance, Leilao
from excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario("Gui", 500.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario("Yuri", 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_descrescente(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario("Yuri", 500.0)
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_tres_lances(self):
        vini = Usuario("Vini", 500.0)
        lance_do_vini = Lance(vini, 200.0)

        yuri = Usuario("Yuri", 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_lance_caso_leilao_tenha_lance(self):
        self.leilao.propoe(self.lance_do_gui)
        self.assertEqual(1, len(self.leilao.lances))

    def test_deve_permitir_propor_lance_caso_ultimo_usuario_seja_diferente(self):
        yuri = Usuario("Yuri", 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.assertEqual(2, len(self.leilao.lances))

    def test_nao_deve_permitir_propor_lance_caso_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200.0)
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)