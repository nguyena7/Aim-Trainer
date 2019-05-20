import pygame
import random
import math
pygame.init()

class target(object):
    def __init__(self, radius, width, height):
        self.radius = radius
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.hitbox = math.pi * self.radius**2
        self.targetHit = False

    def draw(self, screen, color):
        pygame.time.delay(100)
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

    def clickDetection(self, clickPos):
        if clickPos[0] < self.x+ self.radius and clickPos[0] > self.x - self.radius:
            if clickPos[1] < self.y + self.radius and clickPos[1] > self.y - self.radius:
                return True
        else:
            return False