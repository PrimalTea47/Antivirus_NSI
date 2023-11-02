import pygame
from tools import *
from hard_level import *

pygame.init()

def medium_level():

	screen_medium_level = pygame.display.set_mode((800,800))
	pygame.display.set_caption('Medium level')
	background_antivirus = pygame.image.load('assets/backgroundPlay.jpg')

	medium_back = pygame.Rect(190,30,360,70)
	black_back = pygame.Rect(0,0,1000,190)
	bouton_restart = Restart(screen_medium_level)
	bouton_restart.restart_button()

	#variables de conditions
	restart_condition = hard_level_condition = False


	#créer les différentes molécules
	white = Molecules(screen_medium_level,412,490)
	white2 = Molecules(screen_medium_level,412,340)
	red = Molecules(screen_medium_level,590,380)
	lightblue = Molecules(screen_medium_level,225,380)
	red_dragging = lightblue_dragging = False


	#boucle d'exécution
	run = True
	while run:

		screen_medium_level.blit(background_antivirus,(-70,190))

		#ajouter éléments dans la fenêtre
		pygame.draw.rect(screen_medium_level, (224,127,15),medium_back)
		write_text('Medium Level', font, (0,0,0), 200,40, screen_medium_level)
		bouton_restart.show_restart_button()

		#afficher les molécules
		white.show_block()
		white2.show_block()
		red.show_red()
		lightblue.show_lightblue()


		#vérifier les variables de lancements
		if restart_condition:
			medium_level()
		if hard_level_condition:
			hard_level()





		#gestion d'évènements
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		#vérifier si un ou plusieurs molécules sonbt sélectionnées (ou si bouton restart sélectionné)
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if red.get_rect_test(4).collidepoint(event.pos):
						red_dragging = True
					if lightblue.get_rect_test(3).collidepoint(event.pos):
						lightblue_dragging = True
					if bouton_restart.get_rect_restart().collidepoint(event.pos):
						restart_condition = True

		#vérifier si molécules ne sont plus sélectionnées
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					red_dragging = lightblue_dragging = False

		#déplacement des molécules selon la souris
			if event.type == pygame.MOUSEMOTION:
				if red_dragging:
					red.set_position(event.pos)
				if lightblue_dragging:
					lightblue.set_position(event.pos)

		#vérifier si le but du jeu est atteint
			if red.get_rect_test(4).colliderect(black_back):
				hard_level_condition = True



		pygame.display.flip()

	pygame.quit()

