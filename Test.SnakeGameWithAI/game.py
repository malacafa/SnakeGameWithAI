import pygame
import time
from math import atan2,hypot,pi
from snake import Snake
from food import FoodSpawn
import numpy as np

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((300,300))
        pygame.display.set_caption("Snake Game AI!")
        self.fps = pygame.time.Clock()
        self.score=0
        self.snake = Snake()
        self.foodspawn = FoodSpawn()
        self.END=False
        self.actionlist = ["right","up","left","down"]
        self.collwithwallorbody = False
        self.eatfood = False
        self.maxdist = 0

    def getmaxdist(self):
        headpos = self.snake.getHeadPos()
        self.maxdist = distance = hypot(headpos[1]-self.foodspawn.position[1], headpos[0]-self.foodspawn.position[0])

    def getgoaldist(self):
        headpos = self.snake.getHeadPos()
        distance = hypot(headpos[1]-self.foodspawn.position[1], headpos[0]-self.foodspawn.position[0])
        return distance

    def reset(self):
        self.snake.reset()
        self.foodspawn.reset()
        self.score=0
        self.END=False
        self.getmaxdist()
        state = self.get_state()
        return state

    def snake_to_wall(self):
        l=[]
        l.append(abs(self.snake.position[0]-0))
        l.append(abs(self.snake.position[0]-250))
        l.append(abs(self.snake.position[1]-0))
        l.append(abs(self.snake.position[1]-250))
        return [min(l),l.index(min(l))]

    def get_reward(self,state):
        reward=0

        if self.eatfood:
            reward +=500*(len(self.snake.body)-2)
            self.eatfood = False

        if self.collwithwallorbody:
            reward = -500
            self.collwithwallorbody=False

        return reward

    def get_state(self):
        foodsurr=self.snake.getsurrfood(self.foodspawn.position)
        wallsurr=self.snake_to_wall()
        bodysurr=self.snake.getsurrbody()
        return np.asarray( foodsurr+bodysurr+wallsurr+[self.actionlist.index(self.snake.direction)] )

    def Step(self,action):
        done = False
        if action == 0:
            self.snake.changeDirectionTo("right")
        if action == 1:
            self.snake.changeDirectionTo("up")
        if action == 2:
            self.snake.changeDirectionTo("left")
        if action == 3:
            self.snake.changeDirectionTo("down")
        foodPos = self.foodspawn.spawnFood()
        if self.snake.move(foodPos)==1:
            self.score+=1
            self.foodspawn.setFoodOnScreen(False)
            self.eatfood = True
        self.window.fill(pygame.Color(225,225,225))
        body = self.snake.getBody()
        pos = body[0]
        pygame.draw.rect(self.window, pygame.Color(0,225,0), pygame.Rect(pos[0],pos[1],50,50))
        for pos in self.snake.getBody()[1:]:
            pygame.draw.rect(self.window, pygame.Color(0,0,225), pygame.Rect(pos[0],pos[1],50,50))
        pygame.draw.rect(self.window,pygame.Color(225,0,0),pygame.Rect(foodPos[0],foodPos[1],50,50))
        if self.snake.checkCollision()==1:
            self.END=True
            self.window.fill(pygame.Color(225,0,0))
            self.collwithwallorbody = True
            done = True
        
        pygame.display.set_caption("score: %d"%self.score)
        pygame.display.flip()
        self.fps.tick(8)
        new_state = self.get_state()
        reward = self.get_reward(new_state)
        return new_state, reward, done
