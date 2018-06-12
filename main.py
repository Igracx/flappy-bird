import pygame
from pipes import Pipe
from agent import Bird

width, height = (800, 600)
s_color = (0, 0, 0)
caption = "flappy bird game"

def setup():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    
    agents = []
    bird = Bird()
    agents.append(bird)
    
    pipes = []
    new_pipe = Pipe()
    pipes.append(new_pipe)
    
    
    
    
    running = True
    pipe_time = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    agents[0].go_up()
        if pipe_time == 3000:
            new_pipe = Pipe()
            pipes.append(new_pipe)
            pipe_time = 0
        for agent in agents:
            agent.update()
        for pipe in pipes:
            pipe.update()
            if (pipe.left_x + pipe.width < 0):
                pipes.remove(pipe)
                for agent in agents:
                    if not agent.dead:
                        agent.score += 1
        for agent in agents:
            agent.hit(pipes)
        draw(screen, agents, pipes)
        pipe_time += 1

def draw(screen, agents, pipes):
    screen.fill(s_color)
    
    for pipe in pipes:
        pipe.draw(screen)
    
    for agent in agents:
        agent.draw(screen)

    pygame.display.flip()

setup()