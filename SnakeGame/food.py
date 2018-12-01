import random

class FoodSpawn():
    def __init__(self):
        self.position = [random.randrange(1,30)*40,random.randrange(1,30)*40]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,30)*40,random.randrange(1,30)*40]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self,b):
        self.isFoodOnScreen = b