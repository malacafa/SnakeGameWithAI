import random

class FoodSpawn():
    def __init__(self):
        self.position = [random.randrange(1,6)*50,random.randrange(1,6)*50]
        self.isFoodOnScreen = True

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,6)*50,random.randrange(1,6)*50]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self,b):
        self.isFoodOnScreen = b
    
    def reset(self):
        self.position = [random.randrange(1,6)*50,random.randrange(1,6)*50]
        self.isFoodOnScreen = True
