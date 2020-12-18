'''
    The core of the circle generator. This module contains classes 
    for the various components of a circle, as well as color management,
    exportation/saving features, and the actual random generation of
    each given circle. 

    Author: jzaunegger
'''

# Import Dependencies
########################################################################
import math, sys, os
from graphics import *
from PIL import  Image, ImageDraw

# Class to create a NGON (N-Sided Polygon)
########################################################################
class NGON:
    # Constructor Function
    def __init__(self, center_pos, radius, num_sides, color):
        self.centerPos = center_pos
        self.radius = radius
        self.numSides = num_sides
        self.color = color

        self.points = []

    # Determine the points of the shape
    def calcPoints(self):
        x, y, angle = 0, 0, 0

        for i in range(self.numSides):
            angle = math.pi * 2 * i / self.numSides
            x = self.centerPos.getX() + self.radius * math.cos(angle)
            y = self.centerPos.getY() + self.radius * math.sin(angle)
            self.points.append(Point(x, y))

    # Rotate the NGON by a given angle
    def rotate(self, angle):
        theta = math.radians(angle)
        cosang, sinang = math.cos(theta), math.sin(theta)

        new_points = []
        for p in self.points:
            x, y = p.getX(), p.getY()
            tx, ty = x-self.centerPos.getX(), y-self.centerPos.getY()
            new_x = (tx * cosang + ty * sinang ) + self.centerPos.getX()
            new_y = (-tx * sinang + ty * cosang ) + self.centerPos.getX()
            new_points.append(Point(new_x, new_y))

        self.points = new_points

    # Function to display the NGON
    def show(self, win, filled):
        NGON = Polygon(self.points)
        if(filled == True):
            NGON.setFill(self.color)
            NGON.setOutline(self.color)
        else:
            NGON.setOutline(self.color)

        NGON.draw(win)