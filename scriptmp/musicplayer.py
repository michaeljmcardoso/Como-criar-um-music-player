#instalando módulo pygame
%pip install pygame # no vs code
!pip install pygame # no pycharm ou colab

# Importando a biblioteca necessária pygame
import pygame

# Para inicializar todos os módulos Pygame importados
# pygame.init()

# Para inicializar apenas o mixer do PyGame
pygame.mixer.init()

# Carregar um arquivo de música para reprodução
pygame.mixer.music.load('sua_musica.mp3') # local da sua música

# Iniciar a reprodução do fluxo de música
pygame.mixer.music.play()

# Esse loop verifica se o canal de música está em uso,
# quando não mais em uso, ele sai do loop
while pygame.mixer.music.get_busy():
    continue # usado para voltar ao início do loop

# sair do programa
pygame.quit()
