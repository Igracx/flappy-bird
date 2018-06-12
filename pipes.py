import pygame
import numpy as np

width, height = (800, 600)

class Pipe:

    def __init__(self):
        self.width = 20
        self.speed = -0.2
        self.window_height = 120
        self.window_top = np.random.randint(0, height - self.window_height)
        self.left_x = width
        self.hit = False
        

    def draw(self, screen):
        if (not self.hit):
            color_pipe = (255, 255, 255)
        else:
            color_pipe = (255, 0, 0)
        color_window = (0, 0, 0)
        self.pipe_rect = pygame.Rect(self.left_x, 0, self.width, height)
        self.window_rect = pygame.Rect(self.left_x, self.window_top, self.width, self.window_height)
        pygame.draw.rect(screen, color_pipe, self.pipe_rect)
        pygame.draw.rect(screen, color_window, self.window_rect)
    
    def update(self):
        self.left_x += self.speed