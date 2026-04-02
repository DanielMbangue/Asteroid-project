from circleshape import *
import pygame
from constants import *
from main import *



class Shots(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self,dt):
        self.position = self.position + (self.velocity * dt)
