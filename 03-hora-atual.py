import time
from datetime import datetime
from threading import Timer

class Dia003:

    def __init__(self):
        self.timer = None
        self.running = True

    def imprimir_hora_atual_a_cada_2_segundos(self):
        if self.running:
            print(datetime.now().time())
            self.timer = Timer(2, self.imprimir_hora_atual_a_cada_2_segundos)
            self.timer.start()

    def parar_impressao(self):
        self.running = False
        if self.timer:
            self.timer.cancel()

# Executa o código
dia003 = Dia003()
dia003.imprimir_hora_atual_a_cada_2_segundos()
time.sleep(15)
dia003.parar_impressao()
