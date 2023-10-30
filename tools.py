import pygame
pygame.init()



#variable utile pour la suite
font = pygame.font.SysFont('arialblack', 75)

#écriture de texte dans la fenêtre
def write_text(text: str, font, color, x, y, fenetre):
    img = font.render(text, True, color)
    fenetre.blit(img, (x, y))




#définir chaque molécules dans une classe
class Molecules:
	"""
	*Block
	*LightGreen
	*Lightblue
	*Red
	*Orange
	*Purple
	*Darkblue
	*Darkgreen
	*Pink
	"""
	def __init__(self,window,x,y):
		self.window = window
		self.x = x
		self.y = y
	
	def show_block(self):
		self.img_block = pygame.image.load('assets/molecule/block.png')
		self.hit_block = self.img_block.get_rect(center=(self.x,self.y))
		self.window.blit(self.img_block, self.hit_block)

	def show_lightgreen(self):
		self.img_lightgreen = pygame.image.load('assets/molecule/1.png')
		self.hit_lightgreen = self.img_lightgreen.get_rect(center=(self.x,self.y))
		self.window.blit(self.img_lightgreen, self.hit_lightgreen)

	def show_lightblue(self):
		self.img_lightblue = pygame.image.load('assets/molecule/2.png')
		self.hit_lightblue = self.img_lightblue.get_rect(center=(self.x,self.y))
		self.window.blit(self.img_lightblue, self.hit_lightblue)

	def show_red(self):
		self.img_red = pygame.image.load('assets/molecule/3.png')
		self.hit_red = self.img_red.get_rect(center=(self.x,self.y))
		self.window.blit(self.img_red, self.hit_red)

	def show_orange(self):
		self.img_orange = pygame.image.load('assets/molecule/4.png')
		self.hit_orange = self.img_orange.get_rect(center=(self.x,self.y))
		self.window.blit(self.img_orange, self.hit_orange)

	def show_purple(self):
		self.img_purple = pygame.image.load('assets/molecule/5.png')
		self.hit_purple = self.img_purple.get_rect(center=(self.x,self.y))
		self.window.blit(self.img_purple, self.hit_purple)

	def show_darkblue(self):
		self.img_darkblue = pygame.image.load('assets/molecule/6.png')
		self.hit_darkblue = self.img_darkblue.get_rect(center=(self.x,self.y))
		self.window.blit(self.img_darkblue, self.hit_darkblue)

	def show_darkgreen(self):
		self.img_darkgreen = pygame.image.load('assets/molecule/7.png')
		self.hit_darkgreen = self.img_darkgreen.get_rect(center=(self.x,self.y))
		self.window.blit(self.img_darkgreen, self.hit_darkgreen)

	def show_pink(self):
		self.img_pink = pygame.image.load('assets/molecule/8.png')
		self.hit_pink = self.img_pink.get_rect(center=(self.x,self.y))
		self.window.blit(self.img_pink, self.hit_pink)