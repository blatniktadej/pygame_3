import random

import pygame

pygame.init()
width=800
height=600
screen=pygame.display.set_mode((width,height))
bg_color=(0,0,0)
pygame.display.set_caption("Flappy bird")
def jump():
    global ball_speed
    ball_speed=JUMP_SPEED
#OVIRA
ovira_sirina=100
ovira_dolzina=300
ovira_barva=(0,255,0)
ovira_speed=5
#ŽOGA
ball_radius=10
ball_color=(255,0,0)
ball_zac_poz=(600,300)
ball_gravity=0.3
ball_space=10

#PRIPRAVA ŽOGE
ball_position=list(ball_zac_poz)
ball_speed=0

#test
#priprava ovire
ovira_x=width
ovira_gap=200
ovira_y=random.randint(ovira_gap,height-ovira_gap)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                jump()