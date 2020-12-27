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

# Returns the center point from a tuple
###############################################################################################################
def getCenterPoint(img_size):
    return (int(img_size[0] / 2), int(img_size[1] / 2))


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

class Circle:
    def __init__(self, name, img_size):
        self.layers = []
        self.name = name
        self.img_size = img_size
        self.image = base_image = Image.new('RGB', self.img_size, 'black')

    def addLayer(self, layer):
        self.layers.append(layer)

    def saveImage(self):
        for layer in self.layers:
            layer_image = layer.drawLayer()
            self.image.paste(layer_image, (0,0), layer_image)
        
        self.image.save(self.name + ".png", 'PNG')


# Class to create a N-Sided Polygon, and draw it 
###############################################################################################################
class NGON:
    def __init__(self, img_size, pos, diameter, num_sides, bg_color, fg_color, line_width, rotation, filled ):
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

    def createImage(self):
        x,y, angle = 0, 0, 0
        self.points = []
        for i in range(self.num_sides):
            angle = math.pi * i * 2 / self.num_sides
            x = int( self.pos[0] + self.radius * math.cos(angle))
            y = int( self.pos[1] + self.radius * math.sin(angle))
            self.points.append((x, y))

    def drawLayer(self):
        self.createImage()
        current_draw = ImageDraw.Draw(self.current_layer)

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

def getDistance(point1, point2):
    temp1 = math.pow(point2[0] - point2[1], 2)
    temp2 = math.pow( (point2[1] - point2[1]), 2)
    dist = math.sqrt(temp1 + temp2)
    return dist


def getNearestPoints(points):
    
    lines = []

    for i in range(len(points)):
        point_i = points[i]
        closest_dist = 100000
        closest_point = points[0]

        for j in range(len(points)):
            point_j = points[j]

            dist = getDistance(point_i, point_j)
            if(dist < closest_dist):
                closest_dist = dist
                closest_point = point_j
        
        lines.append([point_i, closest_point])
    
    return lines


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
        x, y, angle = 0, 0, 0
        for i in range(self.num_points):
            angle = 2 * math.pi * random.random()
            currentRad = random.randint(-self.radius, self.radius)
            x = int(self.center_point[0] + currentRad * math.cos(angle))
            y = int(self.center_point[1] + currentRad * math.sin(angle))
            self.points.append((x, y))
        
        print(self.points)

        lines_points = getNearestPoints(self.points)
        for points in lines_points:
            current_Img = Image.new('RGBA', self.img_size, color=self.bg_color)
            currentDraw = ImageDraw.Draw(current_Img)
            currentDraw.point(self.points[i], fill=self.fg_color)
            currentDraw.line(points, fill=self.fg_color, width=self.line_width)
            self.current_layer.paste(current_Img, (0, 0), current_Img)
        
        return self.current_layer

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
