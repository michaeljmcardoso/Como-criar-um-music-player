import pygame

pygame.init()
pygame.mixer.music.load('suamusica.ogg')
pygame.mixer.music.play()
pygame.event.wait()
input()