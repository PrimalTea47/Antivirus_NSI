import pygame
from tools import write_text, font, Molecules

pygame.init()

def easy_level():

	screen_easy_level = pygame.display.set_mode((800,800))
	pygame.display.set_caption('Easy level')
	background_antivirus = pygame.image.load('assets/backgroundPlay.jpg')

	easy_back = pygame.Rect(240,30,290,70)


	#boucle d'exécution
	run = True
	while run:

		screen_easy_level.blit(background_antivirus,(-70,190))

		#ajouter éléments dans la fenêtre
		pygame.draw.rect(screen_easy_level, (63,153,38),easy_back)
		write_text('Easy Level', font, (0,0,0), 250,40, screen_easy_level)

		Molecules(screen_easy_level,480,560).show_block()
		Molecules(screen_easy_level,370,450).show_red()
		Molecules(screen_easy_level,330,410).show_purple()



		#gestion d'évènements
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False


		pygame.display.flip()

	pygame.quit()

easy_level()