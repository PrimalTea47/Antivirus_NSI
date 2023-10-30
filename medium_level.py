import pygame
from tools import write_text, font, Molecules

pygame.init()

def medium_level():

	screen_medium_level = pygame.display.set_mode((800,800))
	pygame.display.set_caption('Medium level')
	background_antivirus = pygame.image.load('assets/backgroundPlay.jpg')

	medium_back = pygame.Rect(190,30,360,70)


	#boucle d'exécution
	run = True
	while run:

		screen_medium_level.blit(background_antivirus,(-70,190))

		#ajouter éléments dans la fenêtre
		pygame.draw.rect(screen_medium_level, (224,127,15),medium_back)
		write_text('Medium Level', font, (0,0,0), 200,40, screen_medium_level)

		Molecules(screen_medium_level,100,100).show_pink()
		Molecules(screen_medium_level,400,300).show_red()

		#gestion d'évènements
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


		pygame.display.flip()

	pygame.quit()

