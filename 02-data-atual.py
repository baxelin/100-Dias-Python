from datetime import datetime

class Dia002:

    @staticmethod
    def principal():
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        print(data_hora_formatada)

# Executa o método principal
Dia002.principal()
