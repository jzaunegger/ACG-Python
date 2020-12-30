from PIL import Image, ImageDraw
import math, os, sys, random

base_image = Image.new('RGB', (500, 500), (0, 0, 0))
base_draw = ImageDraw.Draw(base_image)

print('\U0001F700')




base_image.save("Constellation.png", "PNG")