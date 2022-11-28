from .widgets import Widget
import pyglet
from partida import Partida

class Total_palavras(Widget):
    palavras = Partida.gerar_palavras()
    cont = len(palavras)
    def __init__(self, x: int, y: int, width: int, height: int, texto='Total de palavras'):
        super().__init__(x, y, width, height)
        self.label = Widget.gerar_label(x, y, width, height, anchor_x = 'left', anchor_y = 'baseline')
        self.texto = str('Total de palavras: ') + str(Total_palavras.cont)
        self.moldura = pyglet.shapes.BorderedRectangle(x-90, y-5, width +160, height, color=(0,75,173), border_color=(255, 255, 255))
        self.label = Widget.gerar_label(self.x, self.y, self.width, self.height, self.texto, (255, 255, 255, 255))
    def draw(self):
        self.moldura.draw()
        self.label.draw()
