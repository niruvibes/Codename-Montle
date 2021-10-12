import pygame

#Intializing pygame
pygame.init()

#Creating screen with size 800x600
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

#Setting the title and icon
pygame.display.set_caption("Montle")
icon = pygame.image.load('smallbook.png')
pygame.display.set_icon(icon)
pygame.display.update

#Game loop so it doesnt close
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.FULLSCREEN:
            pygame.display.toggle_fullscreen
