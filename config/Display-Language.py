from PIL import Image, ImageDraw, ImageFont
import math, os, sys, random
from HelperFunctions import *

# Parameters
img_name = 'Armenian'
font_size = (18, 24, 32)
font_color = (0, 0, 0)
font_path = os.path.join(os.getcwd(), 'DejaVuSans.ttf')
folder_path = os.path.join(os.getcwd(), 'Unicode-Values', 'Armenian')

# Create base image and draw object
base_image = Image.new('RGB', (500, 500), (255, 255, 255))
base_draw = ImageDraw.Draw(base_image)

# Load Font and get language data 
dejavu_font_s = ImageFont.truetype(font_path, font_size[0])
dejavu_font_m = ImageFont.truetype(font_path, font_size[1])
dejavu_font_l = ImageFont.truetype(font_path, font_size[2])
Armenian = readPath(folder_path)
displayLangObject(Armenian)

base_draw.text((250, 25), img_name, font=dejavu_font_l, fill=font_color, align='center', anchor='mm' )

x, y = 10, 30
for key in Armenian:
    sub_object = Armenian[key]
    header_text = key.replace('-', ' ')
    current_text = u''
    for char in sub_object['characters']:
        current_text += ' ' + char[0]

        base_draw.text((x, y), current_text, fill=font_color, font=dejavu_font_s)
    y += 50

# Save the Image
base_image.save("Constellation.png", "PNG")