import pygame

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255,255,0)

LARGURAJANELA = 800
ALTURAJANELA = 700

def mover(bloco, dim_janela):
    borda_esquerda = 0
    borda_superior = 0
    borda_direita = dim_janela[0]
    borda_inferior = dim_janela[1]

    if bloco["objRect"].top < borda_superior or bloco["objRect"].bottom > borda_inferior:
        # figura atingiu o topo ou a base da janela
        bloco["vel"][1] = -bloco["vel"][1]

    if bloco["objRect"].left < borda_esquerda or bloco["objRect"].right > borda_direita:
        # figura atingiu o lado esquerdo ou direito da janela
        bloco["vel"][0] = -bloco["vel"][0]

    bloco["objRect"].x += bloco["vel"][0]
    bloco["objRect"].y += bloco["vel"][1]

# inicializando módulos de pygame
pygame.init()

# criando objeto pygame time clock
relogio = pygame.time.Clock()

# criando a janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Colisão")

b1 = {"objRect": pygame.Rect(375,80,40,80), "cor": VERMELHO, "vel":[0,-5]}
b2 = {"objRect": pygame.Rect(175,200,20,20), "cor": VERDE, "vel":[5,5]}
b3 = {"objRect": pygame.Rect(275,150,60,60), "cor": AZUL, "vel":[-5,5]}
b4 = {"objRect": pygame.Rect(75,150,80,40), "cor": BRANCO, "vel":[-5,5]}

blocos = [b1, b2, b3, b4]

bola = {"objRect": pygame.Rect(270,330,30,30), "cor": BRANCO, "vel": [3,3]}

deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False

    janela.fill(PRETO)
    for bloco in blocos:
        mover(bloco,(LARGURAJANELA, ALTURAJANELA))
        pygame.draw.rect(janela,bloco["cor"], bloco["objRect"])
        mudaCor = bola["objRect"].colliderect(bloco["objRect"],)
        if mudaCor:
            bola["cor"] = bloco["cor"]

    mover(bola,(LARGURAJANELA, ALTURAJANELA))
    pygame.draw.ellipse(janela,bola["cor"],bola["objRect"])

    pygame.display.update()
    relogio.tick(40)

pygame.quit()
