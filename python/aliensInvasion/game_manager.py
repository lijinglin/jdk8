import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group

def log(obj):
	print(str(obj))
	
class GameFunctions():
	def __init__(self,settings,screen,ship,bullets):
		self.settings = settings
		self.screen = screen;
		self.ship = ship;
		self.bullets = bullets
	
	def update_screen(self):
		self.screen.fill(self.settings.bgcolor)
		for bullet in self.bullets.sprites():
			if bullet.rect.bottom < 0:
				del bullet
				self.bullets.remove(bullet)
			else:
				bullet.update()
				bullet.draw_bullet()
		self.ship.blitme()
		pygame.display.flip()
		
		

	def key_events_handle(self,event):
		if event.type == pygame.KEYDOWN or  event.type == pygame.KEYUP:
			if(event.key == pygame.K_RIGHT ):
				self.ship.move_right = (event.type == pygame.KEYDOWN);
				
			if(event.key == pygame.K_LEFT ):
				self.ship.move_left = (event.type == pygame.KEYDOWN)
			elif(event.key == pygame.K_UP ):
				self.ship.move_up = (event.type == pygame.KEYDOWN);
				
			elif(event.key == pygame.K_DOWN ):
				self.ship.move_down = (event.type == pygame.KEYDOWN)
				
			elif(event.key == pygame.K_SPACE and event.type == pygame.KEYDOWN):
				bullet = Bullet(self.settings,self.screen,self.ship)
				self.bullets.add(bullet)
			
			
	
	def check_events(self):
		move_step = 5;
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
					sys.exit()
			self.key_events_handle(event)
			
				
					