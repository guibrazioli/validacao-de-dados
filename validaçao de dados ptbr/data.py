from datetime import datetime

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()


    def mes_cadastro(self):
        meses = [
            "janeiro", "fevereiro", "março", "abril",
            "maio", "junho", "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month -1
        return mes_cadastro[mes_cadastro]

    def dia_da_semana(self):
        dias = [
            "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"
        ]
        dia_da_semana = self.momento_cadastro.weekday
        return dia_da_semana[dia_da_semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro 


