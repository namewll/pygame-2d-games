import random
import time
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
snake=[[100,100,10,10],[90,100,10,10],[80,100,10,10]]
snake_head=pygame.draw.rect(screen,(0,255,0),snake[0],0)
snake_body=pygame.draw.rect(screen,(0,255,0),snake[1],0)
snake_tail=pygame.draw.rect(screen,(0,255,0),snake[2],0)

food_x=random.randint(0,39)*10
food_y=random.randint(0,39)*10
pygame.draw.rect(screen,(255,0,0),(food_x,food_y,10,10),0)

pygame.display.set_caption('贪吃蛇')
pygame.display.flip()
x_speed=10
y_speed=10
end=False
score=0
def draw_snake(snake):
    global end
    if snake[0][0]<=0 or snake[0][0]>=400:
        end=True
    if snake[0][1]<=0 or snake[0][1]>=400:
        end=True
    pygame.draw.rect(screen, (0, 255, 0), snake[0], 0)
    pygame.draw.rect(screen, (0, 255, 0), snake[1], 0)
    pygame.draw.rect(screen, (0, 255, 0), snake[2], 0)

def eat_food():
    global food_x,food_y,score
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 10, 10), 0)
    if [food_x, food_y, 10, 10]==snake[0]:
        score+=10
        pygame.draw.rect(screen, (0, 0, 0), (food_x, food_y, 10, 10), 0)
        food_x = random.randint(0, 39) * 10
        food_y = random.randint(0, 39) * 10
        pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, 10, 10), 0)
        pygame.display.update()


while True:
    font = pygame.font.Font('./STHUPO.TTF', 25)
    text=font.render(f'得分{score}', True, (255, 255, 255), (0, 0, 0))
    width,height=text.get_size()
    screen.blit(text,(200-width/2,10))
    pygame.display.update()

    if score==100:
        font = pygame.font.Font('./STHUPO.TTF', 40)
        text = font.render(f'恭喜通过游戏', True, (255, 255, 0), (0, 0, 0))
        width, height = text.get_size()
        screen.blit(text, (200-width/2,200-height))
        pygame.display.update()
        time.sleep(1)
        end=True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_speed=-10
            if event.key == pygame.K_DOWN:
                y_speed=10
            if event.key == pygame.K_LEFT:
                x_speed=-10
            if event.key == pygame.K_RIGHT:
                x_speed=10
            if (event.key == pygame.K_UP or event.key == pygame.K_DOWN) and snake[0][1]+y_speed!=snake[1][1]:
                snake.insert(0,[snake[0][0],snake[0][1]+y_speed,10,10])
                snake.pop()
                screen.fill((0,0,0))
                draw_snake(snake)
                eat_food()
                pygame.display.update()
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and snake[0][0]+x_speed!=snake[1][0]:
                snake.insert(0,[snake[0][0]+x_speed,snake[0][1],10,10])
                snake.pop()
                screen.fill((0,0,0))
                draw_snake(snake)
                eat_food()
                pygame.display.update()
    if end==True:
        break




