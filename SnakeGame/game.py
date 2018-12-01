import pygame
import time
from snake import Snake
from food import FoodSpawn

window = pygame.display.set_mode((1200,1200))
pygame.display.set_caption("Snake Game AI!")
fps = pygame.time.Clock()
score=0
snake = Snake()
foodspawn = FoodSpawn()
END=False

def gameOver():
    pygame.quit()

while END!=True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirectionTo("right")
            if event.key == pygame.K_UP:
                snake.changeDirectionTo("up")
            if event.key == pygame.K_LEFT:
                snake.changeDirectionTo("left")
            if event.key == pygame.K_DOWN:
                snake.changeDirectionTo("down")
    foodPos = foodspawn.spawnFood()
    if snake.move(foodPos)==1:
        score+=1
        foodspawn.setFoodOnScreen(False)

    window.fill(pygame.Color(225,225,225))
    body = snake.getBody()
    pos = body[0]
    pygame.draw.rect(window, pygame.Color(0,225,0), pygame.Rect(pos[0],pos[1],40,40))
    for pos in snake.getBody()[1:]:
        pygame.draw.rect(window, pygame.Color(0,0,225), pygame.Rect(pos[0],pos[1],40,40))
    pygame.draw.rect(window,pygame.Color(225,0,0),pygame.Rect(foodPos[0],foodPos[1],40,40))
    if snake.checkCollision()==1:
        END=True
        window.fill(pygame.Color(225,0,0))
    pygame.display.set_caption("score: %d"%score)
    pygame.display.flip()
    fps.tick(15)