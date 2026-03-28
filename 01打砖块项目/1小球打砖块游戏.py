import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((800,600))
screen.fill((255,255,255))
pygame.draw.rect(screen,(255,0,0),(350,590,100,10),0)
center_x=400
center_y=580
pygame.draw.circle(screen,(0,0,255),(center_x,center_y),10,0)
blocks=[]
for row in range(4):
    for col in range(7):
        block=pygame.draw.rect(screen,(0,255,0),(col*115,row*25,100,10),0)
        blocks.append(block)
        pygame.display.update()
        col+=1
    row+=1

pygame.display.set_caption('打砖小游戏')
pygame.display.flip()
start=0
x_speed=0.3
y_speed=-0.3
rect_x=350
win_sign=0
end=0
while True:
    for loaded_block in blocks:
        if center_y>=loaded_block[1]-10 and center_y<=loaded_block[1]+10 and center_x>=loaded_block[0] and center_x<=loaded_block[0]+100:
            y_speed=-y_speed
            blocks.remove(loaded_block)
            block = pygame.draw.rect(screen, (255, 255, 255), (loaded_block[0], loaded_block[1], 100, 10), 0)
            pygame.display.update()
    if not blocks:
        print(blocks)
        win_sign=1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                start=1

        if event.type==pygame.MOUSEMOTION and start==1:
            mouse_x=event.pos[0]
            if mouse_x >= 0 and mouse_x <= 700:
                pygame.draw.rect(screen, (255,255, 255), (rect_x, 590 , 100, 10), 0)
                rect_x=mouse_x
                pygame.draw.rect(screen, (255,0,0), (rect_x, 590, 100, 10), 0)
                pygame.display.update()

    if start==1:
        pygame.draw.circle(screen, (255, 255, 255), (center_x, center_y), 10, 0)
        center_x+=x_speed
        center_y+=y_speed
        pygame.draw.circle(screen, (0,0,255), (center_x, center_y), 10, 0)
        pygame.display.update()

    if center_x>=790 or center_x<=10:
        x_speed = x_speed * (-1)
    if center_y <= 10:
        y_speed=y_speed*(-1)

    if center_y == 580 and center_x >= rect_x and center_x <= rect_x + 100:
        y_speed = y_speed * (-1)

    if center_y>580:
        end=1

    if end==1 or win_sign==1:
        break


