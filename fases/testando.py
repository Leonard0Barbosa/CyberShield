import pygame

pygame.init()

tela = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Charmander VS Pikachu")

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((100, 180, 255))

    pygame.display.update()

pygame.quit()
