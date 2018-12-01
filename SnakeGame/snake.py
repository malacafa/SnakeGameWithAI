
#################################################################################
class Snake():
    def __init__(self):
        self.position = [400,200]
        self.body = [[400,200],[360,300],[320,200]]
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
            self.position[0] += 40
        if self.direction == "left":
            self.position[0] -= 40
        if self.direction == "up":
            self.position[1] -= 40
        if self.direction == "down":
            self.position[1] += 40
        self.body.insert(0,list(self.position))
        if self.position == foodPos:
            return 1
        else:
            self.body.pop()
            return 0
        
    def checkCollision(self):
        if self.position[0] > 1160 or self.position[0]<0:
            return 1
        elif self.position[1]>1160 or self.position[1]<0:
            return 1
        for bodyPart in self.body[1:]:
        #print(self.position,bodyPart)
            if self.position == bodyPart:       
                return 1
        return 0

    def getHeadPos(self):
        return self.position
        
    def getBody(self):
        return self.body
#################################################################################

#################################################################################

