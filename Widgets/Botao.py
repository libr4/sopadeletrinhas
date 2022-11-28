import pyglet
from abc import ABC, abstractmethod

# import Campo_resposta
from .widgets import *
from Widgets.Campo_resposta import Campo_resposta
# from ..main import *


class Botao(Widget, ABC):
    def __init__(self, x:int, y:int, width:int, height:int, texto:str=""):
        super().__init__(x, y, width, height)
        self.texto:str = texto
        self.moldura = pyglet.shapes.BorderedRectangle(x, y, width, height, color=(0,75,173), border_color=(255, 255, 255))
        self.label = Widget.gerar_label(self.x, self.y, self.width, self.height, self.texto, (255, 255, 255, 255))
    def draw(self):
        self.moldura.draw()
        self.label.draw()
    @abstractmethod
    def click(self):
        pass


class Btn_Deletar(Botao):
    def __init__(self, x:int, y:int, width:int, height:int, texto:str="deletar"):
        super().__init__(x, y, width, height, texto)
    def click(self, *argumentos):
        campo_resposta:Campo_resposta = argumentos[0]
        campo_resposta.deleta()


class Btn_Enviar(Botao):
    def __init__(self, x, y, width, height, texto="enviar"):
        super().__init__(x, y, width, height, texto)

    def click(self, *argumentos):
        print("oi")
        campo_resposta:Campo_resposta = argumentos[0]
        palavras_certas:list[str] = argumentos[1]
        area_resp_certas:Area_certas = argumentos[2]
        palavra:str = campo_resposta.label.text
        print(palavra, palavras_certas)
        if palavra in palavras_certas:
            campo_resposta.label.text = ""
            try:
                note = pyglet.resource.media("Assets/acerto.mp3")
                note.play()
            except:
                print("ERRO AO REPRODUZIR AUDIO")
            coluna:int = len(palavra) - 3 #palavra eh, aqui, a resposta certa dada pelo jogador
            area_resp_certas.digita(coluna, palavra)
            palavras_certas.remove(palavra)
        else:
            note = pyglet.resource.media("Assets/erro.wav")
            note.play()   