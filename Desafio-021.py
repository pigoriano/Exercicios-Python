print ('========== DESAFIO 021 ==========') 
#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3
#OBS: para instalar a biblioteca do pygame no vscode, crie um novo terminal e digite pip install pygame

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

