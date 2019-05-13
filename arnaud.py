#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [800, 800]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    # DESSIN
    ecran.fill(BLANC)
    
    a=0
    while a < 800:
        pygame.draw.rect(ecran, NOIR, [a,0, 100,100])
        a=a+200
    
    a=0
    while a < 800:
        pygame.draw.rect(ecran, NOIR, [a,200, 100,100])
        a=a+200
        
    pygame.draw.rect(ecran, NOIR, [0,400, 100,100])
    pygame.draw.rect(ecran, NOIR, [200,400, 100,100])
    pygame.draw.rect(ecran, NOIR, [400,400, 100,100])
    pygame.draw.rect(ecran, NOIR, [600,400, 100,100])    
    pygame.draw.rect(ecran, NOIR, [0,600, 100,100])
    pygame.draw.rect(ecran, NOIR, [200,600, 100,100])
    pygame.draw.rect(ecran, NOIR, [400,600, 100,100])
    pygame.draw.rect(ecran, NOIR, [600,600, 100,100])        
    
    pygame.draw.rect(ecran, NOIR, [100,100, 100,100])
    pygame.draw.rect(ecran, NOIR, [300,100, 100,100])
    pygame.draw.rect(ecran, NOIR, [500,100, 100,100])
    pygame.draw.rect(ecran, NOIR, [700,100, 100,100])    
    pygame.draw.rect(ecran, NOIR, [100,300, 100,100])
    pygame.draw.rect(ecran, NOIR, [300,300, 100,100])
    pygame.draw.rect(ecran, NOIR, [500,300, 100,100])
    pygame.draw.rect(ecran, NOIR, [700,300, 100,100])       
    pygame.draw.rect(ecran, NOIR, [100,500, 100,100])
    pygame.draw.rect(ecran, NOIR, [300,500, 100,100])
    pygame.draw.rect(ecran, NOIR, [500,500, 100,100])
    pygame.draw.rect(ecran, NOIR, [700,500, 100,100])          
    pygame.draw.rect(ecran, NOIR, [100,700, 100,100])
    pygame.draw.rect(ecran, NOIR, [300,700, 100,100])
    pygame.draw.rect(ecran, NOIR, [500,700, 100,100])
    pygame.draw.rect(ecran, NOIR, [700,700, 100,100])        
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()