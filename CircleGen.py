'''
    The core of the circle generator. This module contains classes 
    for the various components of a circle, as well as color management,
    exportation/saving features, and the actual random generation of
    each given circle. 

    This small package was made possible through the use of the Pillow,
    python module. This code is running Pillow v8.0.1 and no other
    dependencies, aside from default python modules like os, sys, and math.

    Author: jzaunegger
    Version: 0.1 (Dev)
'''
# Import Dependencies
###############################################################################################################
import math, sys, os, random, json
from PIL import  Image, ImageDraw, ImageFont
import numpy as np

# Helper Functions
#######################################################################################################################################################

# Returns the center point from a tuple
###############################################################################################################
def getCenterPoint(img_size):
    return (int(img_size[0] / 2), int(img_size[1] / 2))

# Check if two points are the same
###############################################################################################################
def checkPoints(point1, point2):
    if point1[0] == point2[0] and point1[1] == point2[1]:
        return True
    else:
        return False

# Get the distance between two points
###############################################################################################################
def getDistance(point1, point2):
    temp1 = math.pow(point2[0] - point1[0], 2)
    temp2 = math.pow( (point2[1] - point1[1]), 2)
    dist = math.sqrt(temp1 + temp2)
    return dist

def getCenterOfTwoPoint(point1, point2):
    cx = (point1[0] + point2[0]) / 2
    cy = (point1[1] + point2[1]) / 2
    return [cx, cy]


# Takes a path to a ttf file and the font size, returns a PIL Font
###############################################################################################################
def getFont(font_path, font_size):
    if font_path.endswith('.ttf'):
        return ImageFont.truetype(font_path, font_size)
    else:
        print("Error: The font could not be loaded.")
        print("")
        sys.exit()

# Get a random character from a given case
###############################################################################################################
def getRandomChar(case):
    if case == 'lower':
        return chr(random.randint(97, 122))

# Layer Management  
#######################################################################################################################################################

# Create a circle object, this contains each drawing layer
###############################################################################################################
class Circle:
    # Object to store the various layers, and compose them together
    def __init__(self, filename, img_size):
        self.layers = []
        self.filename = filename
        self.img_size = img_size
        self.image = base_image = Image.new('RGB', self.img_size, 'black')

    # Add in a new image
    def addLayer(self, layer):
        self.layers.append(layer)

    # Save the image
    def saveImage(self):
        for layer in self.layers:
            layer_image = layer.drawLayer()
            if hasattr(layer, 'layer_rotation'):
                layer_image = layer_image.rotate(layer.layer_rotation)
            self.image.paste(layer_image, (0,0), layer_image)
        
        self.image.save(self.filename + ".png", 'PNG')

# Outer Layers 
#######################################################################################################################################################


# Class to create a N-Sided Polygon, and draw it 
###############################################################################################################
class NGON:
    def __init__(self, img_size, pos, diameter, num_sides, bg_color, fg_color, line_width, rotation, filled):
        self.img_size = img_size
        self.pos = pos
        self.center_point = getCenterPoint(img_size)
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.num_sides = num_sides
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.line_width = line_width
        self.rotation = rotation
        self.filled = filled
        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawLayer(self):
        current_draw = ImageDraw.Draw(self.current_layer)
        x,y, angle = 0, 0, 0
        self.points = []
        for i in range(self.num_sides):
            angle = math.pi * i * 2 / self.num_sides
            x = int( self.pos[0] + self.radius * math.cos(angle))
            y = int( self.pos[1] + self.radius * math.sin(angle))
            self.points.append((x, y))

        if(self.filled == True):
            current_draw.polygon(self.points, fill=self.fg_color, outline=self.fg_color)


        for i in range(len(self.points)):
            if i == len(self.points)-1:
                line_points = [self.points[i], self.points[0]]
            else:
                line_points = self.points[i:i+2]
            
            current_draw.line(line_points, fill=self.fg_color, width=self.line_width, joint='curve')
        rotated = self.current_layer.rotate(self.rotation, resample=Image.BICUBIC, center=self.center_point)
        return rotated

# Class to create a Ring with a series of lines going out through the ring
###############################################################################################################
class LineRing:
    def __init__(self, img_size, diameter, line_height, num_points, line_width, fg_color, bg_color):
        self.img_size = img_size
        self.center_point = getCenterPoint(self.img_size)
        self.diameter = diameter
        self.radius = int(self.diameter/2)
        self.line_height = line_height
        self.num_points = num_points
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawLayer(self):
        x, y, angle = 0, 0, 0
        self.points = []
        
        current_draw = ImageDraw.Draw(self.current_layer)

        for i in range(self.num_points):
            angle = math.pi * i * 2 / self.num_points
            x1 = int( self.center_point[0] + self.radius * math.cos(angle))
            y1 = int( self.center_point[1] + self.radius * math.sin(angle))
            x2 = int( self.center_point[0] + (self.radius + self.line_height) * math.cos(angle))
            y2 = int( self.center_point[1] + (self.radius + self.line_height) * math.sin(angle))
            self.points.append([(x1, y1), (x2, y2)])

        ngon1 = NGON(self.img_size, self.center_point, self.diameter, self.num_points, self.bg_color, self.fg_color, self.line_width, 0, False)
        ngon1_img = ngon1.drawLayer()
        self.current_layer.paste(ngon1_img, (0,0), ngon1_img)

        diameter2 = self.diameter + (self.line_height * 2)

        ngon2 = NGON(self.img_size, self.center_point,  diameter2 , self.num_points, self.bg_color, self.fg_color, self.line_width, 0, False)
        ngon2_img = ngon2.drawLayer()
        self.current_layer.paste(ngon2_img, (0,0), ngon2_img)

        for line_points in self.points:
            current_draw.line(line_points, fill=self.fg_color, width=self.line_width, joint='curve')

        return self.current_layer


class Mandala:
    def __init__(self, img_size, diameter, burst_height, num_points, line_width, fg_color, bg_color, offset, rotation):
        self.img_size = img_size
        self.center_point = getCenterPoint(self.img_size)
        self.diameter = diameter
        self.radius = int(self.diameter/2)
        self.burst_height = burst_height
        self.num_points = num_points
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.offset = offset
        self.layer_rotation = rotation

        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawCurve(self, start_point, end_point):

        # Get the center of the two points, its distance from the center 
        # of the layer
        center = getCenterOfTwoPoint(start_point, end_point)
        dist = getDistance(self.center_point, center)

        curve_x = center[0] + (self.offset / dist) * (center[0] - self.center_point[0])
        curve_y = center[1] + (self.offset / dist) * (center[1] - self.center_point[1])

        current_points = []

        for i in np.arange(0.0, 1.0, 0.01):
            x = (1-i) * (1-i) * start_point[0] + 2 * (1-i) * i * curve_x + i * i * end_point[0]
            y = (1-i) * (1-i) * start_point[1] + 2 * (1-i) * i * curve_y + i * i * end_point[1]
            current_points.append((x, y))
        return current_points


    def drawLayer(self):
        x, y, angle = 0, 0, 0
        self.points = []

        current_draw = ImageDraw.Draw(self.current_layer)

        # Find the locations for the petal base points
        for i in range(self.num_points):
            angle = math.pi * i * 2 / self.num_points
            if i % 2 == 0:
                x = int( self.center_point[0] + self.radius * math.cos(angle))
                y = int( self.center_point[1] + self.radius * math.sin(angle))
            else:
                x = int( self.center_point[0] + (self.radius + self.burst_height) * math.cos(angle))
                y = int( self.center_point[1] + (self.radius + self.burst_height) * math.sin(angle))
            self.points.append((x, y))

        for i in range(len(self.points)):
            if i == len(self.points)-1:
                line_points = self.drawCurve(self.points[i], self.points[0])
            else:
                line_points = self.drawCurve(self.points[i], self.points[i+1])
            
            
            current_draw.line(line_points, fill=self.fg_color, width=self.line_width, joint='curve')

        return self.current_layer

# Class to create a Burst ring pattern
###############################################################################################################
class Burst:
    def __init__(self, img_size, diameter, burst_height, num_points, line_width, fg_color, bg_color):
        self.img_size = img_size
        self.center_point = getCenterPoint(self.img_size)
        self.diameter = diameter
        self.radius = int(self.diameter/2)
        self.burst_height = burst_height
        self.num_points = num_points
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color

        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawLayer(self):
        x, y, angle = 0, 0, 0
        self.points = []
        
        current_draw = ImageDraw.Draw(self.current_layer)

        for i in range(self.num_points):
            angle = math.pi * i * 2 / self.num_points
            if i % 2 == 0:
                x = int( self.center_point[0] + self.radius * math.cos(angle))
                y = int( self.center_point[1] + self.radius * math.sin(angle))
            else:
                x = int( self.center_point[0] + (self.radius + self.burst_height) * math.cos(angle))
                y = int( self.center_point[1] + (self.radius + self.burst_height) * math.sin(angle))
            self.points.append((x, y))

        for i in range(len(self.points)):
            if i == len(self.points)-1:
                line_points = [self.points[i], self.points[0]]
            else:
                line_points = self.points[i:i+2]
            
            current_draw.line(line_points, fill=self.fg_color, width=self.line_width, joint='curve')

        return self.current_layer


# Class to create a series of N-GONs in a ring shape
###############################################################################################################
class Rings:
    def __init__(self, img_size, main_diameter, num_rings, ring_diameter, ring_sides, line_width, fg_color, bg_color, filled):
        self.img_size = img_size
        self.center_point = getCenterPoint(self.img_size)
        self.main_diameter = main_diameter
        self.main_radius = int(self.main_diameter/2)
        self.num_rings = num_rings
        self.ring_sides = ring_sides
        self.ring_diameter = ring_diameter
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.filled = filled

        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawLayer(self):
        x, y, angle = 0, 0, 0

        for i in range(self.num_rings):
            angle = math.pi * 2 * i / self.num_rings
            x = int(self.center_point[0] + self.main_radius * math.sin(angle))
            y = int(self.center_point[1] + self.main_radius * math.cos(angle))

            sub_layer = NGON(self.img_size, (x,y), self.ring_diameter, self.ring_sides, self.bg_color, self.fg_color, self.line_width, 0, self.filled)
            sub_image = sub_layer.drawLayer()

            self.current_layer.paste(sub_image, (0, 0), sub_image)

        return self.current_layer

# Class to create a series of N-GONs in a ring shape, with a random character in each ngon
###############################################################################################################
class TextRings:
    def __init__(self, img_size, main_diameter, num_rings, ring_diameter, ring_sides, line_width, fg_color, bg_color, font_path, font_size, font_color, filled):
        self.img_size = img_size
        self.center_point = getCenterPoint(img_size)
        self.main_diameter = main_diameter
        self.main_radius = int(self.main_diameter / 2)
        self.num_rings = num_rings
        self.ring_diameter = ring_diameter
        self.ring_sides = ring_sides
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color
        self.filled = filled

        self.font = getFont(self.font_path, self.font_size)
        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawLayer(self):
        x, y, angle = 0, 0, 0

        for i in range(self.num_rings):
            new_image = Image.new('RGBA', self.img_size, color=self.bg_color)

            angle = math.pi * 2 * i / self.num_rings
            x = int(self.center_point[0] + self.main_radius * math.sin(angle))
            y = int(self.center_point[1] + self.main_radius * math.cos(angle))
    
            # Draw Character
            char = getRandomChar('lower')
            charImg = Image.new('RGBA', self.img_size, color=self.bg_color)
            charDraw = ImageDraw.Draw(charImg)
            charDraw.text((x, y), char, font=self.font, fill=self.font_color, anchor='mm', align='center')

            # Draw NGON 
            sub_layer = NGON(self.img_size, (x,y), self.ring_diameter, self.ring_sides, self.bg_color, self.fg_color, self.line_width, 0, self.filled)
            sub_image = sub_layer.drawLayer()

            self.current_layer.paste(charImg, (0, 0), charImg)
            self.current_layer.paste(sub_image, (0, 0), sub_image)
        return self.current_layer

# Class to create a ring with alchemical icons in it
###############################################################################################################
class AlchemicRing:
    def __init__(self, img_size, num_points, diameter, font_path, font_size, font_color, bg_color):
        self.img_size = img_size
        self.center_point = getCenterPoint(self.img_size)
        self.num_points = num_points
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color
        self.bg_color = bg_color

        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)
        self.font = getFont(self.font_path, self.font_size)

    def drawLayer(self):
        # Draw the chars
        filepath = os.path.join(os.getcwd(), 'config', 'symbols.json')
        if(os.path.exists(filepath)):
            with open(filepath) as json_file:
                data = json.load(json_file)
    
        symbols = data['symbols']['alchemical-symbols']['values']

        x, y, angle = 0, 0, 0
        for i in range(self.num_points):
            angle = math.pi * 2 * i / self.num_points
            x = int(self.center_point[0] + self.radius * math.sin(angle))
            y = int(self.center_point[1] + self.radius * math.cos(angle))

            char = random.choice(symbols).encode('unicode-escape')
            charImg = Image.new('RGBA', self.img_size, color=self.bg_color)
            charDraw = ImageDraw.Draw(charImg)
            charDraw.text((x, y), char, font=self.font, fill=self.font_color, anchor='mm', align='center')
            self.current_layer.paste(charImg, (0, 0), charImg)

        return self.current_layer

# Class to create a ring with zodiac symbols in it
###############################################################################################################
class ZodiacRing:
    def __init__(self, img_size, diameter, font_path, font_size, font_color, bg_color):
        self.img_size = img_size
        self.center_point = getCenterPoint(self.img_size)
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color
        self.bg_color = bg_color

        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)
        self.font = getFont(self.font_path, self.font_size)

    def drawLayer(self):
        # Draw the chars
        filepath = os.path.join(os.getcwd(), 'config', 'symbols.json')
        if(os.path.exists(filepath)):
            with open(filepath) as json_file:
                data = json.load(json_file)
    
        zodiac = data['symbols']['zodiac']['values']

        x, y, angle = 0, 0, 0
        for i in range(12):
            angle = math.pi * 2 * i / 12
            x = int(self.center_point[0] + self.radius * math.sin(angle))
            y = int(self.center_point[1] + self.radius * math.cos(angle))

            char = zodiac[i]
            charImg = Image.new('RGBA', self.img_size, color=self.bg_color)
            charDraw = ImageDraw.Draw(charImg)
            charDraw.text((x, y), char, font=self.font, fill=self.font_color, anchor='mm', align='center')

            #angle_degrees = int(math.degrees(angle))
            #rotated_img = charImg.rotate(angle_degrees + (-1 * math.pi / 2 ), resample=Image.BICUBIC, center=self.center_point)

            self.current_layer.paste(charImg, (0, 0), charImg)

        return self.current_layer

# Class to create a Ring with icons for the planets in it
###############################################################################################################
class PlanetaryRing:
    def __init__(self, img_size, diameter, font_path, font_size, font_color, bg_color):
        self.img_size = img_size
        self.center_point = getCenterPoint(self.img_size)
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color
        self.bg_color = bg_color

        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)
        self.font = getFont(self.font_path, self.font_size)

    def drawLayer(self):
        # Draw the chars
        filepath = os.path.join(os.getcwd(), 'config', 'symbols.json')
        if(os.path.exists(filepath)):
            with open(filepath) as json_file:
                data = json.load(json_file)
    
        planets = data['symbols']['planets']['values']

        x, y, angle = 0, 0, 0
        for i in range(len(planets)):
            angle = math.pi * 2 * i / len(planets)
            x = int(self.center_point[0] + self.radius * math.sin(angle))
            y = int(self.center_point[1] + self.radius * math.cos(angle))

            char = planets[i]
            charImg = Image.new('RGBA', self.img_size, color=self.bg_color)
            charDraw = ImageDraw.Draw(charImg)
            charDraw.text((x, y), char, font=self.font, fill=self.font_color, anchor='mm', align='center')
            self.current_layer.paste(charImg, (0, 0), charImg)

        return self.current_layer

# Class to create a ring of text
###############################################################################################################
class TextRing:
    def __init__(self, img_size, diameter, num_chars, font_path, font_size, font_color, bg_color):
        self.img_size = img_size
        self.center_point = getCenterPoint(self.img_size)
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.num_chars = num_chars
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color
        self.bg_color = bg_color

        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)
        self.font = getFont(self.font_path, self.font_size)

    def drawLayer(self):
        # Draw the chars
        x, y, angle = 0, 0, 0

        for i in range(self.num_chars):
            angle = math.pi * 2 * i / self.num_chars
            x = int(self.center_point[0] + self.radius * math.sin(angle))
            y = int(self.center_point[1] + self.radius * math.cos(angle))

            char = getRandomChar('lower')
            charImg = Image.new('RGBA', self.img_size, color=self.bg_color)
            charDraw = ImageDraw.Draw(charImg)

            charDraw.text((x, y), char, font=self.font, fill=self.font_color, anchor='mm', align='center')
            #rotateImg = charImg.rotate(math.degrees(angle), resample=Image.BICUBIC, center=centerPoint)
            self.current_layer.paste(charImg, (0, 0), charImg)

        return self.current_layer

# Base Layers 
#######################################################################################################################################################

# Class to generate a character at the center of the circle
###############################################################################################################
class CharBase:
    def __init__(self, img_size, font_path, font_size, font_color, fg_color, bg_color, rotation, filled):
        self.img_size = img_size
        self.center_point = getCenterPoint(self.img_size)
        self.font_path = font_path
        self.font_size = font_size
        self.font_color = font_color
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.rotation = rotation
        self.filled = filled

        self.font = ImageFont.truetype(self.font_path, self.font_size)
        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawLayer(self):

        if(self.filled == True):
            ngon_background = NGON(self.img_size, self.center_point, int(self.font_size * 1.25), 32, self.bg_color, self.fg_color, 2, 0, self.filled)
            ngon_image = ngon_background.drawLayer()
            self.current_layer.paste(ngon_image, (0, 0), ngon_image)



        char = getRandomChar('lower')
        current_Img = Image.new('RGBA', self.img_size, color=self.bg_color)
        currentDraw = ImageDraw.Draw(current_Img)   
        currentDraw.text(self.center_point, char, fill=self.font_color, font=self.font, anchor='mm', align='center')
        #rotateImg = current_Img.rotate(self.rotation, resample=Image.BICUBIC, center=self.center_point)
        self.current_layer.paste(current_Img, (0, 0), current_Img)
        return self.current_layer

# Class to create a Constellation pattern
###############################################################################################################
class Constellation:
    def __init__(self, img_size, num_points, diameter, line_width, fg_color, bg_color):
        self.img_size = img_size
        self.center_point = getCenterPoint(img_size)
        self.num_points = num_points
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawLayer(self):
        self.points = []
        base_draw = ImageDraw.Draw(self.current_layer)

        # Calculate the base points
        x, y, angle = 0, 0, 0
        for i in range(self.num_points):
            angle = 2 * math.pi * random.random()
            currentRad = random.randint(-self.radius, self.radius)
            x = int(self.center_point[0] + currentRad * math.cos(angle))
            y = int(self.center_point[1] + currentRad * math.sin(angle))
            self.points.append((x, y))

        # Find the nearest point for each point
        for point1 in self.points:
            closestPoint = None
            closestDist = 1000000
            for point2 in self.points:
                if checkPoints(point1, point2) == False:
                    current_dist = getDistance(point1, point2)
                    if current_dist < closestDist:
                        closestPoint = point2
                        closestDist = current_dist

            line_points = [point1, closestPoint]
            base_draw.line(line_points, fill=self.fg_color, width=self.line_width, joint='curve')

        return self.current_layer

# Class to create a Maurer Rose pattern
###############################################################################################################
class MaurerRose:
    def __init__(self, img_size, num_points, diameter, line_width, fg_color, bg_color, n, d):
        self.img_size = img_size
        self.center_point = getCenterPoint(img_size)
        self.num_points = num_points
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.n = n
        self.d = d

        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)
        self.points = []

    def drawLayer(self):    
        current_draw = ImageDraw.Draw(self.current_layer)

        for i in range(0, 361):
            k = i * self.d * math.pi / 180
            r = self.radius * math.sin(self.n * k)
            x = int(self.center_point[0] + r * math.cos(k))
            y = int(self.center_point[1] + r * math.sin(k))
            self.points.append((x, y))


        for i in range(len(self.points)):
            if i == len(self.points)-1:
                line_points = [self.points[i], self.points[0]]
            else:
                line_points = self.points[i:i+2]
            
            current_draw.line(line_points, fill=self.fg_color, width=self.line_width, joint='curve')
        return self.current_layer

# Class to create a Rose pattern
###############################################################################################################
class Rose:
    def __init__(self, img_size, num_points, diameter, line_width, fg_color, bg_color, n, d):
        self.img_size = img_size
        self.center_point = getCenterPoint(img_size)
        self.num_points = num_points
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.n = n
        self.d = d
        self.k = self.n / self.d

        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)
        self.points = []


    def drawLayer(self):    
        current_draw = ImageDraw.Draw(self.current_layer)
        x, y, angle = 0, 0, 0

        vals = np.arange(0, math.pi * self.d * 2, 0.01)

        for a in vals:

            r = self.radius * math.cos(self.k * a)
            x = int(self.center_point[0] + r * math.cos(a))
            y = int(self.center_point[1] + r * math.sin(a))
            self.points.append((x, y))

        for i in range(len(self.points)):
            if i == len(self.points)-1:
                line_points = [self.points[i], self.points[0]]
            else:
                line_points = self.points[i:i+2]
            
            current_draw.line(line_points, fill=self.fg_color, width=self.line_width, joint='curve')
        return self.current_layer

# Class to create a Rosette pattern
###############################################################################################################
class Rosette:
    def __init__(self, img_size, num_points, diameter, line_width, fg_color, bg_color):
        self.img_size = img_size
        self.center_point = getCenterPoint(img_size)
        self.num_points = num_points
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawLayer(self):
        x, y, angle = 0, 0, 0
        self.points = []

        for i in range(self.num_points):
            angle = math.pi * i * 2 / self.num_points
            x = self.center_point[0] + self.radius * math.cos(angle)
            y = self.center_point[1] + self.radius * math.sin(angle)
            self.points.append((x, y))

        for i in range(len(self.points)):
            for j in range(len(self.points)):
                dist = getDistance(self.points[i], self.points[j])
                if(dist > 0):
                    points = self.points[i], self.points[j]
                    current_Img = Image.new('RGBA', self.img_size, color=self.bg_color)
                    currentDraw = ImageDraw.Draw(current_Img)   
                    currentDraw.line(points, fill=self.fg_color, width=self.line_width)
                    self.current_layer.paste(current_Img, (0, 0), current_Img)

        return self.current_layer

class Star:
    def __init__(self, img_size, num_points, diameter, line_width, fg_color, bg_color):
        self.img_size = img_size
        self.center_point = getCenterPoint(img_size)
        self.num_points = num_points
        self.diameter = diameter
        self.radius = int(self.diameter / 2)
        self.line_width = line_width
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.current_layer = Image.new('RGBA', self.img_size, color=self.bg_color)

    def drawLayer(self):
        x, y, angle = 0, 0, 0
        self.points = []
        self.lines = []
        currentDraw = ImageDraw.Draw(self.current_layer)
        temp = []

        # Find points around a ring
        for i in range(self.num_points):
            angle = math.pi * i * 2 / self.num_points
            x = self.center_point[0] + self.radius * math.cos(angle)
            y = self.center_point[1] + self.radius * math.sin(angle)
            self.points.append((x, y))

        # Determine even points
        for i in range(len(self.points)):
            if i % 2 == 1:
                temp.append(self.points[i])

        # Determine odd points
        for i in range(len(self.points)):
            if i % 2 == 0:
                temp.append(self.points[i])

        # Determine line vertices
        for i in range(len(temp)):
            if i + 1 < len(temp):
                self.lines.append( [ temp[i], temp[i+1]] )
            else:
                self.lines.append([temp[i], temp[0]])

        # Draw lines
        for line in self.lines:
            currentDraw.line(line, fill=self.fg_color, width=self.line_width)

        return self.current_layer