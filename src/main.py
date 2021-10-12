import pygame

#Intializing pygame
pygame.init()

#Creating screen with size 800x600
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False