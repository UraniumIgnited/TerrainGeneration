import os
import sys
import string
import random
import json
import pygame
from pygame.locals import *
import time


SQUARE_SIZE = 32

GRID_WIDTH = 16
GRID_HEIGHT = 16
width = 600
height = 600
BIAS = 32


class World:
    def Load():
        Grid = [
        ['grass', 'grass', 'grass', 'water', 'sand', 'stone', 'sand', 'sand', 'grass', 'grass', 'dirt', 'stone', 'grass', 'dirt', 'grass', 'sand'],
        ['grass', 'grass', 'grass', 'dirt', 'stone', 'dirt', 'dirt', 'water', 'grass', 'water', 'grass', 'stone', 'grass', 'grass', 'sand', 'dirt'],
        ['water', 'sand', 'stone', 'stone', 'grass', 'dirt', 'water', 'dirt', 'grass', 'stone', 'stone', 'grass', 'sand', 'grass', 'dirt', 'water'],
        ['stone', 'stone', 'water', 'sand', 'sand', 'stone', 'water', 'dirt', 'stone', 'stone', 'dirt', 'grass', 'grass', 'stone', 'sand', 'grass'],
        ['water', 'sand', 'water', 'sand', 'water', 'grass', 'grass', 'sand', 'sand', 'stone', 'water', 'grass', 'dirt', 'dirt', 'grass', 'grass'],
        ['grass', 'grass', 'water', 'grass', 'dirt', 'grass', 'sand', 'stone', 'grass', 'sand', 'stone', 'stone', 'grass', 'sand', 'sand', 'grass'],
        ['water', 'dirt', 'sand', 'water', 'dirt', 'stone', 'dirt', 'sand', 'sand', 'water', 'water', 'water', 'grass', 'stone', 'stone', 'dirt'],
        ['grass', 'dirt', 'sand', 'water', 'sand', 'dirt', 'grass', 'dirt', 'stone', 'dirt', 'stone', 'grass', 'water', 'water', 'sand', 'stone'],
        ['dirt', 'dirt', 'grass', 'sand', 'grass', 'grass', 'sand', 'stone', 'sand', 'grass', 'stone', 'water', 'water', 'grass', 'water', 'sand'],
        ['grass', 'dirt', 'grass', 'grass', 'sand', 'water', 'grass', 'grass', 'grass', 'sand', 'water', 'water', 'stone', 'sand', 'water', 'stone'],
        ['sand', 'grass', 'grass', 'water', 'water', 'grass', 'water', 'sand', 'water', 'stone', 'dirt', 'sand', 'dirt', 'stone', 'water', 'sand'],
        ['water', 'dirt', 'dirt', 'stone', 'dirt', 'water', 'dirt', 'grass', 'water', 'stone', 'dirt', 'stone', 'sand', 'dirt', 'sand', 'stone'],
        ['stone', 'grass', 'grass', 'stone', 'stone', 'grass', 'dirt', 'stone', 'sand', 'water', 'water', 'grass', 'stone', 'sand', 'water', 'stone'],
        ['dirt', 'grass', 'grass', 'grass', 'sand', 'dirt', 'sand', 'grass', 'dirt', 'water', 'grass', 'stone', 'water', 'stone', 'sand', 'dirt'],
        ['dirt', 'grass', 'sand', 'stone', 'sand', 'grass', 'grass', 'stone', 'water', 'grass', 'dirt', 'water', 'sand', 'dirt', 'grass', 'water'],
        ['sand', 'stone', 'sand', 'dirt', 'water', 'stone', 'water', 'stone', 'grass', 'sand', 'grass', 'water', 'grass', 'sand', 'stone', 'sand']]
        return Grid
    def Generate(worldSizeY: int, worldSizeX: int):
        worldGrid = [[random.choice(["stone", "dirt", "grass", "sand", "water"]) for _ in range(worldSizeX)] for _ in range(worldSizeY)]
        return worldGrid

pygame.init()
screen = pygame.display.set_mode((GRID_WIDTH * BIAS, GRID_HEIGHT * BIAS))
pygame.display.set_caption("Pygame Terrain Generation Template with Character")

Grid = World.Generate(GRID_HEIGHT, GRID_WIDTH)

def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if Grid[y][x] == "stone":
                color = (128, 128, 128)
            elif Grid[y][x] == "grass":
                color = (34, 188, 49)
            elif Grid[y][x] == "dirt":
                color = (169, 81, 30)
            elif Grid[y][x] == "sand":
                color = (232, 186, 89)
            elif Grid[y][x] == "water":
                color = (0, 166, 212)
            else:
                color = (0, 0, 0)
            pygame.draw.rect(screen, color, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

PlayerX = 0
PlayerY = 0
PlayerColor = (255, 0, 0)
PlayerSize = 32

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX -= GRID_WIDTH * 2
            elif event.key == pygame.K_RIGHT:
                PlayerX += GRID_WIDTH * 2
            elif event.key == pygame.K_UP:
                PlayerY -= GRID_HEIGHT * 2
            elif event.key == pygame.K_DOWN:
                PlayerY += GRID_HEIGHT * 2
            
    draw_grid()
    pygame.draw.rect(screen, PlayerColor, (PlayerX, PlayerY, PlayerSize, PlayerSize))
    pygame.display.flip()


pygame.quit()
