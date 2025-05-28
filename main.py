import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()

	# Screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Internal clock
	clock = pygame.time.Clock()
	dt = 0

	# Creates groups to easily change the objects in them
	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	# Adds the game objects/classes to their respective groups
	Player.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = (updatables)

	# Instantiates player object at center of screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	# Starts the asteroid field
	asteroid_field = AsteroidField()

	# Frame loop
	while True:
		for event in pygame.event.get(): # Closes window if the X is hit
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black") # Background color

		updatables.update(dt) # Updates these every frame

		for obj in drawables: # Draws each every frame
			obj.draw(screen)
		
		pygame.display.flip() # Updates the screen

		# Saves the amount of time between frames and limits the frame rate to 60, divides by 1000 to convert milliseconds to seconds
		dt = clock.tick(60) / 1000 



if __name__ == "__main__":
	main()