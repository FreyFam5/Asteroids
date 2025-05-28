import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.timer = 0 # Timer for shooting cooldown

	# Gets the triangle shape points
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	# Rotates the player
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt
	
	# Moves the player forward
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	# Draws the player on screen
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)
	
	# Updates the players logic
	def update(self, dt):
		keys = pygame.key.get_pressed()
		# Rotate left and right
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		# Move foward and backwards
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		# Shoots a bullet
		if keys[pygame.K_SPACE]:
			self.shoot()
		# Counts down the timer
		self.timer = max(0, self.timer - dt)
	
	# Shoots a bullet logic
	def shoot(self):
		if self.timer > 0: # If on cooldown, will not shoot
			return
		shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
		shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
		self.timer = PLAYER_SHOOT_COOLDOWN