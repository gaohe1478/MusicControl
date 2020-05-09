import pygame

pygame.mixer.init()
pygame.mixer.music.load("D:\CloudMusic\西原健一郎 - Say You Love Me feat. Tamala.mp3")
pygame.mixer.music.play()
while True:
    x=input()
    if x=="1":
        pygame.mixer.music.pause()
    if x=="2":
        pygame.mixer.music.unpause()