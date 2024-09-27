import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255 )

PI = 3.1416

pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Figuras e texto")

janela.fill(PRETO)

fonte = pygame.font.Font(None, 48)
texto = fonte.render("ola mundo!", True, BRANCO, AZUL)
janela.blit(texto, [30, 150])

pygame.draw.line(janela, VERDE, [60, 260], [420, 260], 4)
pygame.draw.polygon(janela, AZUL, ([191, 206], [236, 277],[156, 277]), 0)
pygame.draw.circle(janela, BRANCO, (300, 500),50,0)
pygame.draw.ellipse(janela, VERMELHO, (400, 250, 40 ,80 ),5)
pygame.draw.rect(janela, VERDE, (20, 20,60,50),0)
pygame.draw.arc(janela, BRANCO, (250, 75,150,125), PI / 2, 3 * PI, 2)
pygame.draw.arc(janela, VERMELHO, (250, 75,150,125), -PI / 2, PI / 2, 2)

pygame.display.update()

deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False

pygame.quit()
