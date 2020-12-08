from graphics import *
import random

'''
    Notes about Alphabets

    1. Characters

'''

class Character:
    def __init__(self, win, pos, size, num_features, rotationAngle):
        self.centerPoint = pos
        self.size = size
        self.num_features = num_features
        self.rotationAngle = rotationAngle

    def genChar(self):
        
        self.width = self.size
        self.height = self.size * 2 


        widthBounds = [self.centerPoint.getX() - self.width/2, self.centerPoint.getX() + self.width/2]
        heightBounds = [self.centerPoint.getY() - self.height/2, self.centerPoint.getY() + self.height/2]

        for i in range(0, self.num_features):
            feat_type = random.randint(0, 1)

            if(feat_type == 0):
                rand_x1 = random.randint(int(widthBounds[0]), int(widthBounds[1]))
                rand_y1 = random.randint(int(heightBounds[0]), int(heightBounds[1]))
                point1 = Point(rand_x1, rand_y1)    

                rand_x2 = random.randint(int(widthBounds[0]), int(widthBounds[1]))
                rand_y2 = random.randint(int(heightBounds[0]), int(heightBounds[1]))
                point2 = Point(rand_x2, rand_y2)    

                line = Line(point1, point2)
                line.setOutline('black')
                line.draw(win)

            elif(feat_type == 1):
                rand_x1 = random.randint(int(widthBounds[0]), int(widthBounds[1]))
                rand_y1 = random.randint(int(heightBounds[0]), int(heightBounds[1]))
                point1 = Point(rand_x1, rand_y1)   

                circ = Circle(point1, self.size * 0.025)
                circ.setFill('black')
                circ.draw(win)







# Create Window
win = GraphWin('Alchemic/Magic Circle Generator', 512, 512)

char = Character(win, Point(256, 256), 150, 10, 0)
char.genChar()

win.getMouse()
win.close()