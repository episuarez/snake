import random

from vector2D import Vector2D

class Serpiente:
    def __init__(self, x=10, y=10):
        self.movimientos = ["Arriba", "Abajo", "Derecha", "Izquierda"];
        self.direccion = random.choice(self.movimientos);
        self.bolas = [Vector2D(x, y)];

    def actualizar_posiciones_bolas(self):
        for indice in range(len(self.bolas) - 1, 0, -1):
            self.bolas[indice].x = self.bolas[indice - 1].x;
            self.bolas[indice].y = self.bolas[indice - 1].y;

    def actualizar(self, max_size_x, max_size_y):
        self.actualizar_posiciones_bolas();

        if self.direccion == "Arriba":
            self.bolas[0].y -= 1;

            if self.bolas[0].y < 0:
                self.bolas[0].y = max_size_y - 1;

        elif self.direccion == "Abajo":
            self.bolas[0].y += 1;

            if self.bolas[0].y > max_size_y - 1:
                self.bolas[0].y = 0;

        elif self.direccion == "Izquierda":
            self.bolas[0].x -= 1;

            if self.bolas[0].x < 0:
                self.bolas[0].x = max_size_x - 1;

        elif self.direccion == "Derecha":
            self.bolas[0].x += 1;

            if self.bolas[0].x > max_size_x - 1:
                self.bolas[0].x = 0;

    def mover(self, direccion):
        # 0: Arriba, 1: Abajo, 2: Izquierda, 3: Derecha

        if direccion == 0:
            self.direccion = "Arriba";
        if direccion == 1:
            self.direccion = "Abajo";
        if direccion == 2:
            self.direccion = "Izquierda";
        if direccion == 3:
            self.direccion = "Derecha";
