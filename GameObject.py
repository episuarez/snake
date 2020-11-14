from Vector2D import Vector2D


class GameObject:
    def __init__(self, caracter, x=0, y=0):
        self.caracter = caracter;
        self.posicion = Vector2D(x, y);

    def __repr__(self):
        return self.caracter;
