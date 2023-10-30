import pygame
from level_selection import lauching_level_selection_screen
from tools import write_text, font

pygame.init()


menu_screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Menu Antivirus")
fond = pygame.image.load('assets/background.jpg')

#Vérification de l'activation du bouton de level selection
level_condition = False


#Bouton de sélection de level
level_selection_button = pygame.Rect(240,140,320,70)
quit_button = pygame.Rect(330,500,125,70)





#boucle d'éxécution du jeu
run = True
while run:

	#éléments à ajouter dans la fenêtre
	menu_screen.blit(fond, (-810,-200))
	pygame.draw.rect(menu_screen, (247,149,79), level_selection_button)
	pygame.draw.rect(menu_screen, (247,149,79), quit_button)
	write_text('Select Level', font, (255,255,255), 250,150, menu_screen)
	write_text('Quit', font, (255,255,255), 340,510, menu_screen)



	if level_condition:
		lauching_level_selection_screen()



	#gestion d'évènements
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False

		#Click sur les boutons
		if event.type == pygame.MOUSEBUTTONDOWN:
			if level_selection_button.collidepoint(event.pos):
				print('click_level_selection')
				level_condition = True

			elif quit_button.collidepoint(event.pos):
				print('click_quit')
				run = False


		





	pygame.display.flip()

pygame.quit()


