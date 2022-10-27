# importando o pacote necessário pygame
import pygame

pygame.init()
pygame.mixer.music.load('suamusica.ogg') # local da sua música no formato .ogg
pygame.mixer.music.play()
pygame.event.wait()
input()
