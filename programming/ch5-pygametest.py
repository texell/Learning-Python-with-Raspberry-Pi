import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
screen = pygame.display.get_surface()
rect = pygame.Rect(400, 400, 100, 100)
pygame.draw.rect(screen, (100, 0, 0), rect, 0)
pygame.display.update()
