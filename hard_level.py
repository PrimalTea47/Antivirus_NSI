import pygame
from tools import write_text, font, Molecules

pygame.init()

def hard_level():

	screen_hard_level = pygame.display.set_mode((800,800))
	pygame.display.set_caption('Easy level')
	background_antivirus = pygame.image.load('assets/backgroundPlay.jpg')

	hard_back = pygame.Rect(240,30,290,70)


	#boucle d'exécution
	run = True
	while run:

		screen_hard_level.blit(background_antivirus,(-70,190))

		#ajouter éléments dans la fenêtre
		pygame.draw.rect(screen_hard_level, (193,24,15),hard_back)
		write_text('Hard Level', font, (0,0,0), 250,40, screen_hard_level)



		#gestion d'évènements
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


		pygame.display.flip()

	pygame.quit()

