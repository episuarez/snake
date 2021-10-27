import os
import time
from threading import Thread

import cursor

from juego import Juego

miJuego = Juego(25, 25);

os.system("cls");
cursor.hide();

class Input(Thread):
    def __init__(self):
        Thread.__init__(self);

    def run(self):
        global miJuego;

        while miJuego.jugar:
            miJuego.input();

input = Input();
input.start();

while miJuego.jugar:
    print("\033[%d;%dH" % (0, 0));
    miJuego.update();
    print(miJuego.draw());
    time.sleep(0.15);

input.join();

os.system("cls");
print(f"¡Has perdido! Tu puntuación ha sido de {miJuego.puntos} y has recogido {int(miJuego.puntos / 12)} frutas");
