import sys
import pygame
from settings import Settings
from ship import Ship

def log(obj):
	print(str(obj))
	
class GameFunctions():
	def __init__(self,settings,screen,ship):
		self.settings = settings
		self.screen = screen;
		self.ship = ship;
	
	def update_screen(self):
		self.screen.fill(self.settings.bgcolor)
		self.ship.blitme()
		pygame.display.flip()

	def key_events_handle(self,event):
		if event.type == pygame.KEYDOWN or  event.type == pygame.KEYUP:
			if(event.key == pygame.K_RIGHT ):
				self.ship.move_right = (event.type == pygame.KEYDOWN);
				
			if(event.key == pygame.K_LEFT ):
				self.ship.move_left = (event.type == pygame.KEYDOWN)
			
			if(event.key == pygame.K_UP ):
				self.ship.move_up = (event.type == pygame.KEYDOWN);
				
			if(event.key == pygame.K_DOWN ):
				self.ship.move_down = (event.type == pygame.KEYDOWN)
			
	
	def check_events(self):
		move_step = 5;
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
					sys.exit()
			self.key_events_handle(event)
			
				
					