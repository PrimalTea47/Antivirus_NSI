import pygame
from tools import *

pygame.init()

def hard_level():
 
	screen_hard_level = pygame.display.set_mode((800,800))
	pygame.display.set_caption('Hard level')
	background_antivirus = pygame.image.load('assets/backgroundPlay.jpg')

	hard_back = pygame.Rect(240,30,290,70)
	black_back = pygame.Rect(0,0,1000,190)
	bouton_restart = Restart(screen_hard_level)
	bouton_restart.restart_button()
	
	

	#création de chaque molécule à l'aide de la classe Molecules
	white = Molecules(screen_hard_level,480,410)
	white2 = Molecules(screen_hard_level,195,705)
	red = Molecules(screen_hard_level,520,600)
	darkblue = Molecules(screen_hard_level,625,545)
	orange = Molecules(screen_hard_level,335,525)
	lightgreen = Molecules(screen_hard_level,230,525)
	red_dragging = darkblue_dragging = orange_dragging = lightgreen_dragging = False

	#boucle d'exécution
	run = True
	while run:

		screen_hard_level.blit(background_antivirus,(-70,190))

		#ajouter éléments dans la fenêtre
		pygame.draw.rect(screen_hard_level, (0,0,0), black_back)
		pygame.draw.rect(screen_hard_level, (193,24,15),hard_back)
		write_text('Hard Level', font, (0,0,0), 250,40, screen_hard_level)
		bouton_restart.show_restart_button()
		

		#afficher chaque molécules
		white.show_block()
		white2.show_block()
		red.show_red()
		darkblue.show_darkblue()
		orange.show_orange()
		lightgreen.show_lightgreen()


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			
			#vérifier si une ou plusieures molécules sont sélectionnées
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					if red.get_rect_test(4).collidepoint(event.pos):
						red_dragging = True
					if darkblue.get_rect_test(7).collidepoint(event.pos):
						darkblue_dragging = True
					if orange.get_rect_test(5).collidepoint(event.pos):
						orange_dragging = True
					if lightgreen.get_rect_test(2).collidepoint(event.pos):
						lightgreen_dragging = True
					#redémerre le level si nécéssaire
					if bouton_restart.get_rect_restart().collidepoint(event.pos):
						hard_level()

			#vérifier si le bouton de la souris est relaché ==> plus aucune molécule sélectionnée
			if event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1:
					red_dragging = darkblue_dragging = orange_dragging = lightgreen_dragging = False

			#Si molécule sélectionnée et souris en mouvement, la molécule suit le curseur de la souris
			if event.type == pygame.MOUSEMOTION:
				if red_dragging:
					red.set_position(event.pos)
				if darkblue_dragging:
					darkblue.set_position(event.pos)
				if orange_dragging:
					orange.set_position(event.pos)
				if lightgreen_dragging:
					lightgreen.set_position(event.pos)

			#vérifier si le niveau est complété
			if red.get_rect_test(4).colliderect(black_back):
				run = False


		pygame.display.flip()

	pygame.quit()
