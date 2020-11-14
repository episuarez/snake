import random
import copy

from GameObject import GameObject


class Player():
    def __init__(self, x, y):
        self.elementos = [GameObject('0', x, y)];
        self.puntos = 0;

        # 0 -> Arriba
        # 1 -> Abajo
        # 2 -> Derecha
        # 3 -> Izquierda
        self.direccion = random.randint(0, 3);

    def agregarBola(self):
        ultimaPosicion = self.elementos[-1].posicion;
        self.elementos.append(GameObject("O", ultimaPosicion.x, ultimaPosicion.y));
        self.puntos += 25;

    def mover(self, tamano):
        for indice in range(len(self.elementos) - 1, 0, -1):
            self.elementos[indice].posicion.x = self.elementos[indice - 1].posicion.x;
            self.elementos[indice].posicion.y = self.elementos[indice - 1].posicion.y;

        if self.direccion == 0:
            self.elementos[0].posicion.y -= 1;
        elif self.direccion == 1:
            self.elementos[0].posicion.y += 1;
        elif self.direccion == 2:
            self.elementos[0].posicion.x += 1;
        elif self.direccion == 3:
            self.elementos[0].posicion.x -= 1;

        if self.elementos[0].posicion.y < 0:
            self.elementos[0].posicion.y = tamano - 1;
        if self.elementos[0].posicion.y > tamano - 1:
            self.elementos[0].posicion.y = 0;

        if self.elementos[0].posicion.x < 0:
            self.elementos[0].posicion.x = tamano - 1;
        if self.elementos[0].posicion.x > tamano - 1:
            self.elementos[0].posicion.x = 0;

    def posicionUsada(self, vector2D):
        for elemento in self.elementos:
            if elemento.posicion == vector2D:
                return True;

        return False;
