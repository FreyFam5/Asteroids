import sys
import pygame
import pygame.freetype
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
	pygame.init()

	# Screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Font for text in the game
	GAME_FONT = pygame.freetype.SysFont(None, 30)

	# Current score of the player
	score = 0

	# Internal clock
	clock = pygame.time.Clock()
	dt = 0

	# Creates groups to easily change the objects in them
	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# Adds the game objects/classes to their respective groups
	Player.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = (updatables)
	Shot.containers = (shots, updatables, drawables)

	# Instantiates player object at center of screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	# Starts the asteroid field
	asteroid_field = AsteroidField()

	# Frame loop
	run = True
	while run:
		for event in pygame.event.get(): # Closes window if the X is hit
			if event.type == pygame.QUIT:
				run = False
		
		screen.fill("black") # Background color
		
		updatables.update(dt) # Updates these every frame
		
		# Checks collisions with asteroids
		for asteroid in asteroids:
			if player.is_colliding(asteroid): # If player collides with asteroid, ends game
				print(f"Game over!\nScore was: {score}")
				sys.exit()
			for shot in shots: # Finds if each bullet hit an asteroid, if it did, kill both
				if shot.is_colliding(asteroid):
					shot.kill()
					asteroid.split()
					score += 1

		for obj in drawables: # Draws each every frame
			obj.draw(screen)

		# Renders the text to screen for score
		GAME_FONT.render_to(screen, (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.1), str(score), (255, 255, 255))
		
		pygame.display.flip() # Updates the screen

		# Saves the amount of time between frames and limits the frame rate to 60, divides by 1000 to convert milliseconds to seconds
		dt = clock.tick(60) / 1000 



if __name__ == "__main__":
	main()