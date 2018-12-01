class Snake():
    def __init__(self):
        self.position = [150,150]
        self.body = [[150,150],[100,150],[50,150]]
        self.direction = 'right'
        self.changeDirection = self.direction

    def reset(self):
        self.position = [150,150]
        self.body = [[150,150],[100,150],[50,150]]
        self.direction = 'right'
        self.changeDirection = self.direction

    def changeDirectionTo(self, dir):
        if dir=='right' and not self.direction=='left':
            self.direction = 'right'
        if dir=='left' and not self.direction=='right':
            self.direction = 'left'
        if dir=='up' and not self.direction=='down':
            self.direction = 'up'
        if dir=='down' and not self.direction=='up':
            self.direction = 'down'
    
    def move(self, foodPos):
        if self.direction == "right":
            self.position[0] += 50
        if self.direction == "left":
            self.position[0] -= 50
        if self.direction == "up":
            self.position[1] -= 50
        if self.direction == "down":
            self.position[1] += 50
        self.body.insert(0,list(self.position))
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0
        
    def checkCollision(self):
        if self.position[0]>250 or self.position[0]<0:
            return 1
        elif self.position[1]>250 or self.position[1]<0:
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:       
                return 1
        return 0
        
    def getsurrfood(self,foodpos):
        l=[-1]*4
        if foodpos[1]==self.position[1]:
            if foodpos[0]>self.position[0]:
                l[0]=foodpos[0]-self.position[0]
            elif foodpos[0]<self.position[0]:
                l[1]=self.position[0]-foodpos[0]
        elif foodpos[0]==self.position[0]:
            if foodpos[1]>self.position[1]:
                l[2]=foodpos[1]-self.position[1]
            elif foodpos[1]<self.position[1]:
                l[3]=self.position[1]-foodpos[1]
        return l

    def getsurrbody(self):
        l=[-1]*4
        for bodyPart in self.body[1:]:
            if bodyPart[0] == self.position[0]:
                if bodyPart[1] > self.position[1]:
                    l[3]=bodyPart[1]-self.position[1]
                elif bodyPart[1] < self.position[1]:
                    l[2]=self.position[1]-bodyPart[1]
            elif bodyPart[1] == self.position[1]:
                if bodyPart[0] > self.position[0]:
                    l[1]=bodyPart[0]-self.position[0]
                elif bodyPart[0] < self.position[0]:
                    l[0]=self.position[0]-bodyPart[0]
        return l

    def getHeadPos(self):
        return self.position
        
    def getBody(self):
        return self.body