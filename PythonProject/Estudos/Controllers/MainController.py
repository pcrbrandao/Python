import pygame

from Estudos.Controllers import Colors
from Estudos.Controllers.MainScene import MainScene

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
mainScene = MainScene(screen)

pygame.display.set_caption("Meu Jogo")

# Laço (Loop) até o o usuário pressionar o botão fechar
done = False

# Usado para gerenciar quão rápido a tela é atualizada
clock = pygame.time.Clock()

# Laço principal
while not done:
    # evento principal
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # A lógica do jogo vem aqui

    # O código da limpeza da tela vem aqui

    # Aqui, tornaremos a tela branca. Não coloque outros comandos de desenho
    # acima, ou eles serão apagados com esse comando

    # se você quer uma imagem de fundo, substitua o fill(WHITE) com a imagem
    screen.fill(Colors.WHITE)

    # O código do desenho vem aqui
    mainScene.draw()

    # Após o desenho a tela deve ser atualizada
    pygame.display.flip()

    # limite de 60 quadros por segundo
    clock.tick(60)

# fecha a janela e termina
pygame.quit()