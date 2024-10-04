import pygame, random

#carregando imagens
imagemTubarao = pygame.image.load("img/tubarao.png")
imagemPeixe = pygame.image.load("img/peixe.png")
imagemFundo = pygame.image.load("img/cenario.png")

# definindo outras constantes do jogo
LARGURAJANELA = 800
ALTURAJANELA = 700
LARGURAPEIXE = 80
ALTURAPEIXE = 30
LARGURATUBARAO = 290
ALTURATUBARAO = 190
VEL = 6
ITERACOES = 30

#redimensionando as imagens
imagemFundo = pygame.transform.scale (imagemFundo, (LARGURAJANELA, ALTURAJANELA))
imagemPeixe = pygame.transform.scale (imagemPeixe, (LARGURAPEIXE, ALTURAPEIXE))
imagemTubarao = pygame.transform.scale (imagemTubarao, (LARGURATUBARAO, ALTURATUBARAO))

# definindo a função moverJogador(), que registra a posição do jogador
def moverJogador(jogador, teclas, dimensaoJanela):
    bordaEsquerda = 0
    bordaSuperior = 0
    bordeDireita = dimensaoJanela[0]
    bordaInferior = dimensaoJanela[1]
    if teclas["esquerda"] and jogador["objRect"].left > bordaEsquerda:
        jogador["objRect"].x -= jogador["vel"]
    if teclas["direita"] and jogador["objRect"].right < bordeDireita:
        jogador["objRect"].x += jogador["vel"]
    if teclas["cima"] and jogador["objRect"].top > bordaSuperior:
        jogador["objRect"].y -= jogador["vel"]
    if teclas["baixo"] and jogador["objRect"].bottom < bordaInferior:
        jogador["objRect"].y += jogador["vel"]

# definindo a função moverBloco(), que registra a posição do bloco
def moverPeixe(peixe):
    peixe["objRect"].x += peixe["vel"]

# inicializando pygame
pygame.init()

# instanciando método Clock para variavel relogio
relogio = pygame.time.Clock()

# criando janela
janela = pygame.display.set_mode((LARGURAJANELA, ALTURAJANELA))
pygame.display.set_caption("Imagem e Som")

# criando jogador
jogador = {"objRect": pygame.Rect(300, 100, LARGURATUBARAO, ALTURATUBARAO), "imagem": imagemTubarao, "vel": VEL, 
"colisaoRect": pygame.Rect(300 + 50, 100 + 50, LARGURATUBARAO - 100, ALTURATUBARAO - 100)}

# Configurando o som
somComer = pygame.mixer.Sound("mp3/comer.mp3")
# Carregar a música de fundo
# pygame.mixer.music.load('mp3/musicaFundo.mp3')
# Definir o volume (por exemplo, 0.1 para 10% do volume máximo)
# pygame.mixer.music.set_volume(0.1)
# Reproduzir a música em loop
# pygame.mixer.music.play(-1, 0.0)
somAtivado = True

# definindo o dicionario que guardará as direcoes pressionadas
teclas = {"esquerda": False, "direita": False, "cima": False, "baixo": False}

# inicializando outras variáveis
contador = 0
peixes = []
deve_continuar = True

# loop do jogo
while deve_continuar:
    # checando os eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

    # quando uma tecla é pressionada
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            deve_continuar = False
        if evento.key == pygame.K_m:
            if somAtivado:
                pygame.mixer.music.stop()
                somAtivado = False
            else:
                pygame.mixer.music.play(-1, 0.0)
                somAtivado = True


    # Verifique o estado atual das teclas
    teclas = pygame.key.get_pressed()
    teclas = {
        "esquerda": teclas[pygame.K_LEFT] or teclas[pygame.K_a],
        "direita": teclas[pygame.K_RIGHT] or teclas[pygame.K_d],
        "cima": teclas[pygame.K_UP] or teclas[pygame.K_w],
        "baixo": teclas[pygame.K_DOWN] or teclas[pygame.K_s],
    }

    # quando um botao do mouse é pressionado
    if evento.type == pygame.MOUSEBUTTONDOWN:
        peixes.append({"objRect": pygame.Rect(evento.pos[0], evento.pos[1], LARGURAPEIXE, ALTURAPEIXE), "imagem": imagemPeixe, "vel": -3 })

    contador += 1
    if contador >= ITERACOES:
        contador = 0
        posY = random.randint(0, (ALTURAJANELA - ALTURAPEIXE))
        posX = -LARGURAPEIXE
        velRandom = random.randint(VEL - 3, VEL + 3)
        peixes.append({"objRect": pygame.Rect(posX, posY, LARGURAPEIXE, ALTURAPEIXE), "imagem": imagemPeixe, "vel": velRandom})

    # preenchendo o fundo de janela com a cor preta
    janela.blit(imagemFundo, (0,0))

    # movendo o jogador
    moverJogador(jogador, teclas, (LARGURAJANELA, ALTURAJANELA))

    # desenhando jogador
    janela.blit(jogador["imagem"], jogador["objRect"])

    # checando se jogador bateu em algum bloco ou se bloco saiu da janela para retirá-lo da lista
    for peixe in peixes:
        comeu = jogador["colisaoRect"].colliderect(peixe["objRect"])
        if comeu and somAtivado:
            somComer.play()
        if comeu or peixe["objRect"].x > LARGURAJANELA:
            peixes.remove(peixe)

    # Não esqueça de atualizar a posição do rect de colisão a cada movimento do jogador
    jogador["colisaoRect"].topleft = (jogador["objRect"].x + 50, jogador["objRect"].y + 50)

    # Movendo e desenhando os peixes
    for peixe in peixes:
        moverPeixe(peixe)
        janela.blit(peixe["imagem"], peixe["objRect"])

    # atualizando a janela
    pygame.display.update()

    # FPS
    relogio.tick(40)

# encerrando módulos de Pygame
pygame.quit()      