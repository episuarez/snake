import random

import keyboard

from Player import Player
from Vector2D import Vector2D
from GameObject import GameObject


class Snake:
    def __init__(self, tamano=10):
        self.tamano = tamano;

        self.numeroMaximoFrutas = 5;
        self.frutas = [];

        self.generarPantalla();

        centro = int(self.tamano / 2) - 1;
        self.serpiente = Player(centro, centro);

        self.generarFrutas();

    def actualizacion(self):
        while True:
            if keyboard.is_pressed('esc'):
                exit(0);

            if keyboard.is_pressed("W"):
                self.serpiente.direccion = 0;
            if keyboard.is_pressed("S"):
                self.serpiente.direccion = 1;
            if keyboard.is_pressed("D"):
                self.serpiente.direccion = 2;
            if keyboard.is_pressed("A"):
                self.serpiente.direccion = 3;

    def puedoJugar(self):
        for elemento in self.serpiente.elementos:

            contador = 0;
            for elementoComprobar in self.serpiente.elementos:
                if elemento.posicion == elementoComprobar.posicion:
                    contador += 1;

            if contador > 1:
                return False;

        return True;

    def pintado(self):
        print("\033[%d;%dH" % (0, 0));

        self.comerFrutas();
        self.serpiente.mover(self.tamano);
        self.generarFrutas();

        self.limpiarPantalla();
        self.rellenarPantalla();

        return self.obtenerPantalla();

    def comerFrutas(self):
        for fruta in self.frutas:
            if fruta == self.serpiente.elementos[0].posicion:
                self.frutas.remove(fruta);
                self.serpiente.agregarBola();

    def generarFrutas(self):
        while len(self.frutas) < self.numeroMaximoFrutas:
            posicion = Vector2D(random.randint(0, self.tamano - 1), random.randint(0, self.tamano - 1));

            if not self.serpiente.posicionUsada(posicion):
                self.frutas.append(posicion);

    def generarPantalla(self):
        self.pantalla = [];

        for x in range(0, self.tamano):
            fila = [];
            for y in range(0, self.tamano):
                fila.append(" ");

            self.pantalla.append(fila);

    def limpiarPantalla(self):
        for x in range(0, self.tamano):
            for y in range(0, self.tamano):
                self.pantalla[y][x] = " ";

    def rellenarPantalla(self):
        for fruta in self.frutas:
            self.pantalla[fruta.y][fruta.x] = "*";

        for elemento in self.serpiente.elementos:
            self.pantalla[elemento.posicion.y][elemento.posicion.x] = elemento.caracter;

    def obtenerPantalla(self):
        contenido = "SNAKE - @episuarez\n";
        contenido += f"Puntos: {self.serpiente.puntos}\n";

        contenido += "-" * ((self.tamano * 2) + 2) + "\n";
        for fila in self.pantalla:
            contenido += "|";
            for valor in fila:
                contenido += valor + " ";
            contenido += "|\n";
        contenido += "-" * ((self.tamano * 2) + 2);
        
        return contenido;
