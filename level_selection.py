import pygame
from tools import *
from easy_level import *
from medium_level import *
from hard_level import *


pygame.init()
 
def lauching_level_selection_screen():

	screen = pygame.display.set_mode((800,800))
	pygame.display.set_caption('Select your level')

	#Trois boutons de level : EASY  | MEDIUM  | HARD  +  Retour_Menu
	easy_button = pygame.Rect(330,140,135,70)
	medium_button = pygame.Rect(280,320,220,70)
	hard_button = pygame.Rect(330,500,135,70)


	#Variable d'activation de levels
	easy_condition = False
	medium_condition = False
	hard_condition = False


	#gestion d'évènements
	running = True
	while running:

		#ajout d'éléments à la fenêtre
		write_text('Select Level',font, (255,255,255),250,40, screen)
		pygame.draw.rect(screen, (63,153,38),easy_button)
		pygame.draw.rect(screen, (224,127,15),medium_button)
		pygame.draw.rect(screen, (193,24,15),hard_button)
		write_text('Easy', font, (0,0,0), 340,150,screen)
		write_text('Medium', font, (0,0,0), 290,330,screen)
		write_text('Hard', font, (0,0,0), 340,510,screen)

		#vérification des lancements des levels
		if easy_condition:
			easy_level()

		if medium_condition:
			medium_level()
 	
		if hard_condition:
			hard_level()




		#gestion d'évènements
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			#Détection de choix de level via bouttons
			if event.type == pygame.MOUSEBUTTONDOWN:
				if easy_button.collidepoint(event.pos):
					easy_condition = True

				if medium_button.collidepoint(event.pos):
					medium_condition = True

				if hard_button.collidepoint(event.pos):
					hard_condition = True



		pygame.display.flip()

	tout()

