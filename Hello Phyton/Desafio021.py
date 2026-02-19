import pygame
input('Dê enter para ouvir o aúdio!')
pygame.init() #Inicializar o pygame!
pygame.mixer.init() #Inicializar o mixer de aúdio

pygame.mixer.music.load("receba-made-with-Voicemod.mp3") # .mp3 ou .wav
pygame.mixer.music.play()

input('Pressione ENTER para parar...')