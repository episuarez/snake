import os
import platform
import threading
import time

import cursor

from Snake import Snake

miJuego = Snake();

actualizacion = threading.Thread(target=miJuego.actualizacion, daemon=True);
actualizacion.start();

cursor.hide();

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear");

while miJuego.puedoJugar():
    print(miJuego.pintado());

    time.sleep(0.25);

print(f"Has perdido! Has conseguido {miJuego.serpiente.puntos}.");
print("Gracias por jugar");
