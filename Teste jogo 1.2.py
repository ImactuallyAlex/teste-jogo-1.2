import random
import pygame
import sys
from pygame.locals import * 
from sys import exit
import os

pygame.init()

carregar_telas = True

while True :

    if carregar_telas == True :
        tela1_menu1 = True
        tela1_jogo = False
        tela1_pausa = False
        tela1_derrota = False
        tela1_opcoes = False
    carregar_telas = False
    
    largura_tela1 = 1920
    altura_tela1 = 1080

    largura_player = largura_tela1 / 16
    altura_player = altura_tela1 / 8
    posicao_player_x = (largura_tela1/2) - (largura_player/2)
    posicao_player_y = altura_player*3
    movimento_esquerda_player = True
    movimento_direita_player = True
    
    velocidade_player = largura_tela1/128

    mais_dificuldade = 0
    pontos = 0

    cor_tela1_jogo = [75,150,255]
    cor_botao_normal = [0,255,0]
    cor_botao_emcima = [100,255,150]
    branco = [255,255,255]
    preto = [0,0,0]

    posicaoY_rect1 = (altura_tela1 - altura_player)
    largura_rect1 = ((largura_tela1/2) - (largura_player * 1.5))

    limite_largura_rect1 = []
    for posicao in range(largura_tela1) :
        limite_largura_rect1.insert(0, posicao)
        if posicao == (largura_tela1 - (largura_player * 3)) :
            break
        
    tamanho_fonte_pequena = int(altura_tela1/12)
    tamanho_fonte_media = int(altura_tela1/8)
    tamanho_fonte_titulo = int(altura_tela1/6)

    tela1 = pygame.display.set_mode((largura_tela1, altura_tela1))
    pygame.display.set_caption('jogo 1.2')
    
    fps = pygame.time.Clock()
    fps_q = 600
    
    tempo_base = pygame.time.get_ticks()
    meio_segundo = 0
    
    class imagem :
        def __init__(self, pasta, imagem, largura, altura) :
            local_imagem = os.path.join(pasta, imagem)
            imagem1 = pygame.image.load(local_imagem)
            self.imagem_emproporcao = pygame.transform.scale(imagem1, (largura, altura))
    
        def desenhar_composicao(self, tela, x, y) :
            tela.blit(self.imagem_emproporcao, (x, y))

        def desenhar_em_centro_objeto(self, tela, objeto) :
            posicao = self.imagem_emproporcao.get_rect(center = objeto.center)
            tela.blit(self.imagem_emproporcao, (posicao))
    
    def escrever(texto, fonte, tamanho_fonte, cor_texto, tela, x, y) :
        fonte_definida = pygame.font.SysFont(fonte, tamanho_fonte)
        texto_definido = fonte_definida.render(texto, True, (cor_texto))
        if x == 'centro':
            larguraX = texto_definido.get_width()
            x = (largura_tela1/2) - (larguraX/2)        
        tela.blit(texto_definido, (x,y))

    class botao :
        def __init__(self, x, y, largura, altura, cor_botao, fonte, tamanho_fonte, cor_texto, texto = '') :
            if x == 'centro' :
                x = (largura_tela1/2) - (largura/2)
            self.rect = pygame.Rect(x, y, largura, altura)
            self.cor_botao = cor_botao
            self.fonte = pygame.font.Font(fonte, tamanho_fonte)
            self.cor_texto = cor_texto
            self.texto = self.fonte.render(texto, True, (self.cor_texto))
            self.posicao_texto = self.texto.get_rect(center=self.rect.center)
            
        def desenhar(self, tela) :
            self.botao = pygame.draw.rect(tela, self.cor_botao, self.rect)
            tela.blit(self.texto, self.posicao_texto)
        
        def emcima(self) :
            return self.rect.collidepoint(pygame.mouse.get_pos())

        def selecionado(self) :
            return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]
        
    menu_botao1 = botao(largura_tela1/12.8, altura_player*3, largura_tela1/3.2, altura_player, cor_botao_normal, None, tamanho_fonte_media, branco, 'Jogar')
    menu_botao2 = botao(largura_tela1/12.8, altura_player*4.5, largura_tela1/3.2, altura_player, cor_botao_normal, None, tamanho_fonte_media, branco, 'Opções')
    menu_botao3 = botao(largura_tela1/12.8, altura_player*6, largura_tela1/3.2, altura_player, cor_botao_normal, None, tamanho_fonte_media, branco, 'Sair')
    
    opcao_menu_botao1 = botao('centro', altura_tela1 - altura_player*2, largura_tela1/3.2, altura_player, cor_botao_normal, None, tamanho_fonte_media, branco, 'Voltar')
    
    derrota_menu_botao1 = botao('centro', altura_player*3, largura_tela1/2, altura_player, cor_botao_normal, None, tamanho_fonte_media, branco, 'Jogar denovo')
    derrota_menu_botao2 = botao('centro', altura_player*5, largura_tela1/2, altura_player, cor_botao_normal, None, tamanho_fonte_media, branco, 'Menu principal')
    
    pausa_menu_botao1 = botao('centro', altura_player*3, largura_tela1/3, altura_player, cor_botao_normal, None, tamanho_fonte_media, branco, 'Retomar')
    pausa_menu_botao2 = botao('centro', altura_player*5, largura_tela1/3, altura_player, cor_botao_normal, None, tamanho_fonte_media, branco, 'Menu')
    
    while tela1_menu1 == True :
        tela1.fill((cor_tela1_jogo))
        
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                exit()
        
        img_menu = imagem('imagens teste jogo', 'imgMenu1.png', largura_tela1, altura_tela1)
        img_menu.desenhar_composicao(tela1, 0, 0)
        
        escrever('Suicide Maniac', None, tamanho_fonte_titulo, branco, tela1, largura_tela1/12.8, altura_player)     
        
        menu_botao1.desenhar(tela1)
        if menu_botao1.emcima() :
            menu_botao1.cor_botao = cor_botao_emcima
        else :
            menu_botao1.cor_botao = cor_botao_normal
        if menu_botao1.selecionado() :
            tela1_menu1 = False
            tela1_jogo = True
            
        menu_botao2.desenhar(tela1)
        if menu_botao2.emcima() :
            menu_botao2.cor_botao = cor_botao_emcima
        else :
            menu_botao2.cor_botao = cor_botao_normal
        if menu_botao2.selecionado() :
            tela1_menu1 = False
            tela1_opcoes = True
        
        menu_botao3.desenhar(tela1)
        if menu_botao3.emcima() :
            menu_botao3.cor_botao = cor_botao_emcima
        else :
            menu_botao3.cor_botao = cor_botao_normal
        if menu_botao3.selecionado() :
            pygame.quit()
            exit()
            
        pygame.display.flip()
        
    while tela1_opcoes == True :
        tela1.fill((0,0,0))
        
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                exit()

        escrever('Opções', None, tamanho_fonte_titulo, branco, tela1, 'centro', altura_player)

        opcao_menu_botao1.desenhar(tela1) 
        if opcao_menu_botao1.emcima() :
            opcao_menu_botao1.cor_botao = cor_botao_emcima
        else :
            opcao_menu_botao1.cor_botao = cor_botao_normal
        if opcao_menu_botao1.selecionado() :
            tela1_opcoes = False
            tela1_menu1 = True
        
        pygame.display.flip()

    while tela1_jogo == True :
        posicaoX_rect2 = (largura_rect1 + (largura_player * 3))
        largura_rect2 = (largura_tela1 - posicaoX_rect2)
        
        tela1.fill((cor_tela1_jogo))
        fps.tick(fps_q)
        
        tempo_atual = pygame.time.get_ticks() - tempo_base
        if tempo_atual >= 500 :
            meio_segundo = meio_segundo + 1
            tempo_base = tempo_base + 500
            
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE :
                    tela1_jogo = False
                    tela1_pausa = True
                    while tela1_pausa == True :
                        tela1.fill((0,0,0))
                        
                        for event in pygame.event.get() :
                            if event.type == QUIT :
                                pygame.quit()
                                exit()
                        
                        escrever('Pausa', None, tamanho_fonte_titulo, branco, tela1, 'centro', altura_player)
                        
                        pausa_menu_botao1.desenhar(tela1)
                        if pausa_menu_botao1.emcima() :
                            pausa_menu_botao1.cor_botao = cor_botao_emcima
                        else :
                            pausa_menu_botao1.cor_botao = cor_botao_normal
                        if pausa_menu_botao1.selecionado() :
                            tela1_pausa = False
                            tela1_jogo = True
                        pausa_menu_botao2.desenhar(tela1)
                        if pausa_menu_botao2.emcima() :
                            pausa_menu_botao2.cor_botao = cor_botao_emcima
                        else :
                            pausa_menu_botao2.cor_botao = cor_botao_normal
                        if pausa_menu_botao2.selecionado() :
                            tela1_pausa = False
                            carregar_telas = True                            
                                               
                        pygame.display.flip()
                
        stop_rect1 = pygame.draw.rect(tela1, (cor_tela1_jogo), (largura_rect1,posicaoY_rect1,velocidade_player*2,altura_player)) 
        stop_rect2 = pygame.draw.rect(tela1, (cor_tela1_jogo), (posicaoX_rect2-velocidade_player*2,posicaoY_rect1,velocidade_player*2,altura_player))    
                
        player = pygame.draw.rect(tela1, (cor_tela1_jogo), (posicao_player_x, posicao_player_y, largura_player, altura_player))
        player_frame1 = imagem('imagens teste jogo', 'player1_frame1.png', largura_player*1.3, altura_player*1.5)
        player_frame2 = imagem('imagens teste jogo', 'player1_frame2.png', largura_player*1.3, altura_player*1.5)
        if meio_segundo % 2 == 1 :
            player_frame1.desenhar_em_centro_objeto(tela1, player)
        elif meio_segundo % 2 == 0 :
            player_frame2.desenhar_em_centro_objeto(tela1, player)
        if movimento_esquerda_player == True :
            if pygame.key.get_pressed()[K_a]:
                if posicao_player_x > 0 :
                    posicao_player_x = posicao_player_x - velocidade_player
        if movimento_direita_player == True :
            if pygame.key.get_pressed()[K_d]:
                if posicao_player_x < (largura_tela1 - largura_player) :
                    posicao_player_x = posicao_player_x + velocidade_player
                
        rect1 = pygame.draw.rect(tela1, (0,255,0),(0,posicaoY_rect1, largura_rect1, altura_player))
        rect2 = pygame.draw.rect(tela1, (0,255,0),(posicaoX_rect2, posicaoY_rect1, largura_rect2, altura_player))
        posicaoY_rect1 = posicaoY_rect1 - (altura_tela1/480)
        if posicaoY_rect1 <= (0 - altura_player) :
            posicaoY_rect1 = altura_tela1
            largura_rect1 = random.choice(limite_largura_rect1)
            pontos = pontos + 1 
            mais_dificuldade = mais_dificuldade + 1
        if player.colliderect(stop_rect1) :
            movimento_esquerda_player = False
        elif player.colliderect(stop_rect2) :
            movimento_direita_player = False
        else :
            movimento_direita_player = True
            movimento_esquerda_player = True
        if player.colliderect(rect1) or player.colliderect(rect2) :
            tela1_jogo = False
            tela1_derrota = True
            
        if mais_dificuldade >= 5 :
            fps_q = fps_q + 20
            mais_dificuldade = 0
        
        fonte_pontos = pygame.font.SysFont(None, tamanho_fonte_pequena)
        texto_pontos = fonte_pontos.render(f'Pontuação = {pontos}',True, (255,255,255))
        largura_pontos = texto_pontos.get_width()
        altura_pontos = texto_pontos.get_height()
        posicaoY_pontos = altura_tela1 - altura_pontos * 2
        posicaoX_pontos = largura_tela1 - largura_pontos - (largura_tela1 / 64)    
        tela1.blit(texto_pontos, (posicaoX_pontos, posicaoY_pontos))
                
        pygame.display.flip()
    
    while tela1_derrota == True :
        tela1.fill((0,0,0))
        
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                exit()
        
        escrever('Derrota', None, tamanho_fonte_titulo, (255,0,0), tela1, 'centro',altura_player)
        
        derrota_menu_botao1.desenhar(tela1)
        if derrota_menu_botao1.emcima() :
            derrota_menu_botao1.cor_botao = cor_botao_emcima
        else :
            derrota_menu_botao1.cor_botao = cor_botao_normal
        if derrota_menu_botao1.selecionado() :
            tela1_jogo = True
            tela1_derrota = False
                    
        derrota_menu_botao2.desenhar(tela1)
        if derrota_menu_botao2.emcima() :
            derrota_menu_botao2.cor_botao = cor_botao_emcima
        else :
            derrota_menu_botao2.cor_botao = cor_botao_normal
        if derrota_menu_botao2.selecionado() :
            tela1_menu1 = True
            tela1_derrota = False
        
        pygame.display.flip()
        
    