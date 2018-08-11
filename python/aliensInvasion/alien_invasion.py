#coding=utf-8
import sys
import pygame
from settings import Settings
from ship import Ship
from game_manager import GameFunctions

def run_game():
	pygame.init()
	ai_setting = Settings()
	screen = pygame.display.set_mode(ai_setting.screen)
	aShip = Ship(screen);
	gf = GameFunctions(ai_setting,screen,aShip)
	pygame.display.set_caption('Alien Invasion')
	bgcolor = ai_setting.bgcolor
	while True:
		gf.check_events()
		gf.update_screen();
			
	
	while True:
		input = raw_input('input name')
		if input == 'q' :
			break;
			
run_game()