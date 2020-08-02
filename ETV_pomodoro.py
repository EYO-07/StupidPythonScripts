# Programas Estupidos em Python [ POMODORO ]
from time import time, sleep
import os
from math import floor
import colorama
colorama.init()

R = colorama.Fore.RED
W = colorama.Fore.WHITE

class pomodoro():
    def __init__(self):
        self.tempo_inicial = time()
        self.tempo_corrente = time()
        self.tempo_maximo = 45
    def tempo_var(self):
        return self.tempo_corrente - self.tempo_inicial
    def update(self):
        self.tempo_corrente = time()
    def display_update(self):
        print( W + ' Pomodoro Estupido (45 minutos) :', self.tempo_formatado(), '\n' )
        print( R ,self.progress_bar() )
    def tempo_formatado(self):
        T = self.tempo_maximo - self.tempo_var()
        MIN = floor(  T / 60. )
        SEC = floor( T - MIN*60 )
        return '( ' + str(MIN) + ' : ' + str(SEC) + ' )'
    def progress_bar(self):
        NUM_CHR = 70
        X = floor ( ( self.tempo_maximo - self.tempo_var() ) / self.tempo_maximo * NUM_CHR )
        Y = max( NUM_CHR - X , 0 )
        return  '[ ' + X*'#' + Y*'-' +' ]' 
    def mainLoop(self):
        while True:
            os.system('cls')
            self.update()
            self.display_update()
            sleep(1)
            if self.tempo_var() > self.tempo_maximo:
                os.system('start https://www.youtube.com/watch?v=0OZyleriwRU')
                break
M = pomodoro()
M.mainLoop()

