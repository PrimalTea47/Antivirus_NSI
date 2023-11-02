import pygame
from tools import *
from medium_level import *

pygame.init()

def easy_level():

    screen_easy_level = pygame.display.set_mode((800,800))
    pygame.display.set_caption('Easy level')
    background_antivirus = pygame.image.load('assets/backgroundPlay.jpg')

    easy_back = pygame.Rect(240,30,290,70)
    black_back = pygame.Rect(0,0,1000,190)
    bouton_restart = Restart(screen_easy_level)
    bouton_restart.restart_button()

    #variable de lancements
    restart_condition = medium_level_condition = False

    # créer les différentes molecules
    white = Molecules(screen_easy_level,480,560)
    red = Molecules(screen_easy_level,370,450)
    purple = Molecules(screen_easy_level,330,407)
    red_dragging = purple_dragging = False

    # boucle d'exécution
    run = True
    while run:

        screen_easy_level.blit(background_antivirus,(-70,190))

        #ajouter éléments dans la fenêtre
        pygame.draw.rect(screen_easy_level, (0,0,0), black_back)
        pygame.draw.rect(screen_easy_level, (63,153,38),easy_back)
        write_text('Easy Level', font, (0,0,0), 250, 40, screen_easy_level)
        bouton_restart.show_restart_button()

        white.show_block()
        red.show_red()
        purple.show_purple()


        #vérifier conditions de lancements
        if restart_condition:
            easy_level()
        if medium_level_condition:
            medium_level()




        #gestion d'évènements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #vérifier si une ou plusieures molécules sont sélectionnées
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if red.get_rect_test(4).collidepoint(event.pos):
                        red_dragging = True
                    if purple.get_rect_test(6).collidepoint(event.pos):
                        purple_dragging = True

                    if bouton_restart.get_rect_restart().collidepoint(event.pos):
                        restart_condition = True

            #vérifier si le bouton de la souris est relaché ==> plus aucune molécule sélectionnée
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    red_dragging = purple_dragging = False

            #Si molécule sélectionnée et souris en mouvement, la molécule suit le curseur de la souris
            if event.type == pygame.MOUSEMOTION:
                if red_dragging:
                    red.set_position(event.pos)
                if purple_dragging:
                    purple.set_position(event.pos)

            #vérifier si le niveau est complété
            if red.get_rect_test(4).colliderect(black_back):
                medium_level_condition = True

        pygame.display.flip()

    pygame.quit()