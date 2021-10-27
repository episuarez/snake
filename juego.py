import random
import msvcrt

from serpiente import Serpiente
from vector2D import Vector2D

class Juego:
    def __init__(self, size_x=10, size_y=10):
        self.jugar = True;
        self.puntos = 0;
        self.size_x = size_x;
        self.size_y = size_y;
        self.mapa = self.generar_mapa_vacio();
        self.serpiente = Serpiente(5, 5);
        self.frutas = [];

        self.generar_frutas(15);

    def generar_mapa_vacio(self):
        mapa = []
        for _ in range(self.size_x):
            fila = [];
            for _ in range(self.size_y):
                fila.append(" ");
            mapa.append(fila);
        return mapa

    def rellenar_mapa(self):
        for bola in self.serpiente.bolas:
            self.mapa[bola.y][bola.x] = "O";

        for fruta in self.frutas:
            self.mapa[fruta.y][fruta.x] = "*";

    def generar_frutas(self, cantidad):
        if len(self.frutas) < cantidad:
            for _ in range(cantidad - len(self.frutas)):
                self.frutas.append(Vector2D(random.randrange(0, self.size_x), random.randrange(0, self.size_y)));

    def comprobar_colision(self):
        if self.serpiente.bolas[0] in self.serpiente.bolas[1:]:
            self.jugar = False;

        for fruta in self.frutas:
            if fruta == self.serpiente.bolas[0]:
                self.frutas.remove(fruta);
                self.puntos += 12;
                self.serpiente.bolas.append(Vector2D(fruta.x, fruta.y));

    def input(self):
        if msvcrt.kbhit():
            tecla = ord(msvcrt.getch());

            if tecla == 72: #Arriba
                self.serpiente.mover(0);
            elif tecla == 80: #Abajo
                self.serpiente.mover(1);
            elif tecla == 75: #Izquierda
                self.serpiente.mover(2);
            elif tecla == 77: #Derecha
                self.serpiente.mover(3);

    def update(self):
        self.mapa = self.generar_mapa_vacio();
        self.generar_frutas(15);
        self.rellenar_mapa();

        self.serpiente.actualizar(self.size_x, self.size_y);
        self.comprobar_colision();

    def draw(self):
        texto = f"""SNAKE 1.0
Puntos: {self.puntos}\n\n""";

        texto += "#" * (self.size_x * 2 + 2) + "\n";
        for fila in self.mapa:
            texto += "#";
            for valor in fila:
                texto += f"{valor} ";
            texto += "#\n";
        texto += "#" * (self.size_x * 2 + 2);

        return texto;
