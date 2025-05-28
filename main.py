import pygame
from constants import *
from player import Player

def main():
	pygame.init()

	# Screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Internal clock
	clock = pygame.time.Clock()
	dt = 0

	# Creates to groups to easily update and draw things every frame
	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()

	Player.containers = (updatables, drawables)

	# Instantiates player object at center of screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# Frame loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black")

		updatables.update(dt)

		for obj in drawables:
			obj.draw(screen)
		
		pygame.display.flip()

		# Saves the amount of time between frames and limits the frame rate to 60, divides by 1000 to convert milliseconds to seconds
		dt = clock.tick(60) / 1000 



if __name__ == "__main__":
	main()