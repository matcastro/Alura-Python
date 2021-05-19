from datetime import datetime, timedelta
class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        momento_cadastro = self.momento_cadastro
        return momento_cadastro.strftime("%d/%m/%Y %H:%M:%S")

    def tempo_cadastro(self):
        tempo_cadastro = datetime.now() - self.momento_cadastro
        return tempo_cadastro