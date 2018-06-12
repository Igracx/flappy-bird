import pygame

width, height = (800, 600)
radius = 10
gravity = 0.1
up_force = -30

class Bird:
    
    def __init__(self):
        self.y = height / 2;
        self.x = 50
        self.gravity = 0.1
        self.up_force = -30
        self.velocity = 0
        self.force_up = False
        self.score = 0
        self.dead = False
        
    
    def update(self):
        if not self.dead:
            self.velocity += gravity
            self.velocity *= 0.7
            if (self.y > height):
                self.y = height
                self.velocity = 0
            self.up()
            if (self.y < 0):
                self.y = 0
                self.velocity = 0
            self.y += self.velocity

    def draw(self, screen):
        if not self.dead:
            color = (255, 255, 255)
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), radius)

    def up(self):
        if self.force_up:
            self.velocity += up_force
            self.force_up = False
    
    def go_up(self):
        self.force_up = True

    def hit(self, pipes):
        if not self.dead:
            for pipe in pipes:
                if (self.x + radius >= pipe.left_x and self.x - radius <= pipe.left_x + pipe.width):
                    if (self.y - radius <= pipe.window_top or self.y + radius >= pipe.window_top + pipe.window_height):
                        pipe.hit = True
                        self.dead = True
                        print(self.score)
    