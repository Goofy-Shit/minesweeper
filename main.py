import pygame, random

pygame.init()

class field: v=0

AREA=[16,16]
MINES=50
miness=0
fields = [[field() for i in range(AREA[1])] for j in range(AREA[0])]

def getRandomField():
    global AREA, fields
    return fields[random.randint(0, AREA[0])][random.randint(0, AREA[1])]

window=w=pygame.display.set_mode((200,200))

running = True

while running:
    
    for e in pygame.event.get():pass

    pygame.display.update()