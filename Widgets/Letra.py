# from widgets import Widget
import pyglet
from .widgets import Widget

class Letra(Widget):
    def __init__(self, x: int, y: int, width: int, height: int, letra: str):
        super().__init__(x, y, width, height)
        self.__letra = letra
        self.label = pyglet.text.Label(self.__letra,
                font_name='Arial',
                font_size=32,
                color=(0, 0, 0, 255),
                # anchor_x='center', anchor_y='center',
                x = self.x + self.width // 2,
                y = self.y + self.height // 2)
        self.__clicada = False
    @property
    def letra(self):
        return self.__letra
    
    def draw(self):
        self.label.draw()

    def __repr__(self):
        return f"{self.letra}"
    def __eq__(self, other):
        return (self.__letra == other.__letra) and (self.__index == other.__index)

    def click(self, *argumentos):
        campo_resposta = argumentos[0]
        campo_resposta.digita(self.letra)
        self.label.color = (255, 0, 0, 255)

    @property
    def clicada(self):
        return self.__clicada
    @clicada.setter
    def clicada(self, state):
        self.__clicada = state