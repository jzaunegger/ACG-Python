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
import math, sys, os, random
from PIL import  Image, ImageDraw, ImageFont

# Returns the center point from a tuple
###############################################################################################################
def getCenterPoint(img_size):
    return (int(img_size[0] / 2), int(img_size[1] / 2))


def getFont(font_path, font_size):
    if font_path.endswith('.ttf'):
        return ImageFont.truetype(font_path, font_size)
    else:
        print("Error: The font could not be loaded.")
        print("")
        sys.exit()

def getRandomChar(case):
    if case == 'lower':
        return chr(random.randint(97, 122))

# Function to draw a NGON
###############################################################################################################
def NGON(img_size, diameter, num_sides, bg_color, fg_color, line_width, rotation):
    
    # Create new layer, get the drawing context, and find the center point
    layer = Image.new('RGBA', img_size, color=bg_color)
    draw = ImageDraw.Draw(layer)
    centerPoint = getCenterPoint(img_size)
    
    radius = diameter / 2

    # Determine where the points are
    x, y, angle = 0, 0, 0
    points = []
    for i in range(num_sides):
        angle = math.pi * i * 2 / num_sides
        x = int(centerPoint[0] + radius * math.cos(angle))
        y = int(centerPoint[1] + radius * math.sin(angle))

        points.append((x, y))

    # Draw the Layer
    for i in range(0, len(points)):
        if i == len(points)-1:
            line_points = [points[i], points[0]]
        else:
            line_points = points[i:i+2]

        draw.line(line_points, fill=fg_color, width=line_width, joint='curve')

    rotated = layer.rotate(rotation, resample=Image.BICUBIC, center=centerPoint)
    return rotated


# Function to draw a ring of text
###############################################################################################################
def TextRing(img_size, radius, num_chars, font_path, font_size, font_color, bg_color):
        # Create new layer, get the drawing context, and find the center point
        layer = Image.new('RGBA', img_size, color=bg_color)
        draw = ImageDraw.Draw(layer)
        centerPoint = getCenterPoint(img_size)

        # Load the image font
        current_font = getFont(font_path, font_size)

        # Draw the chars
        x, y, angle = 0, 0, 0

        for i in range(num_chars):
            angle = math.pi * 2 * i / num_chars
            x = int(centerPoint[0] + radius * math.sin(angle))
            y = int(centerPoint[1] + radius * math.cos(angle))

            char = getRandomChar('lower')
            charImg = Image.new('RGBA', img_size, color=bg_color)
            charDraw = ImageDraw.Draw(charImg)

            charDraw.text((x, y), char, font=current_font, fill=font_color, anchor='mm', align='center')
            #rotateImg = charImg.rotate(math.degrees(angle), resample=Image.BICUBIC, center=centerPoint)
            layer.paste(charImg, (0, 0), charImg)

        return layer