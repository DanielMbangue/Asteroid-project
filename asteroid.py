from circleshape import *
from constants import *
import pygame
import random
from logger import log_event
from main import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            x = self.position.x
            y = self.position.x
            random.uniform(20,50)
            self.aster1_vector = self.velocity.rotate(1)
            self.aster2_vector = self.velocity.rotate(-1)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            self.Asteroid1 = Asteroid (x, y, self.new_radius)
            self.Asteroid2 = Asteroid (x, y, self.new_radius)
            self.Asteroid1.velocity = self.aster1_vector * 1.2
            self.Asteroid2.velocity = self.aster2_vector * 1.2
            
        
        
