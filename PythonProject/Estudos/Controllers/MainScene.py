# cena principal
import pygame

from math import pi
from pygame import draw
from pygame import Surface
from pygame.font import Font

from Estudos.Controllers import Colors


class MainScene:
    """Representa uma cena do jogo"""

    def __init__(self, screen: Surface):
        self.screen = screen

    def draw(self):
        # uma linha
        # draw.line(self.screen, Colors.GREEN, [0, 0], [100, 100], 5)

        # desenha algumas linhas de (0, 10) a (100, 110)
        # com 5 pixels de largura
        # for y_offset in range(0, 100, 10):
        #    draw.line(self.screen, Colors.RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)

        # desenhe um retangulo
        # draw.rect(self.screen, Colors.BLACK, [20, 20, 250, 100], 2)

        # desenhe uma elipse
        # draw.ellipse(self.screen, Colors.BLACK, [20, 20, 250, 100], 2)

        # arcos como parte de elipse
        # arc_dim = [20, 220, 250, 200]
        # draw.arc(self.screen, Colors.BLACK, arc_dim, 0, pi / 2, 2)
        # draw.arc(self.screen, Colors.GREEN, arc_dim, pi / 2, pi, 2)

        text_loop(self.screen)


def text_loop(screen: Surface):
    texto_str = ''
    texto_altura = 30
    font = pygame.font.SysFont('Consolas', texto_altura, True, False)

    for i in range(10):
        for j in range(5):
            texto_str += '*'

        text = font.render(texto_str, True, Colors.BLACK)
        screen.blit(text, [30, 30 + (i * texto_altura)])
        texto_str = ''
