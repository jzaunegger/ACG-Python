from PIL import Image, ImageDraw, ImageFont
import os

font_size = 36
width = 500
height = 100
bg_color = (255, 255, 255)
font_color = (0, 0, 0)



font_path = os.path.join(os.getcwd(), 'fonts', 'Symbola-AjYx.ttf')

img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)
unicode_font = ImageFont.truetype(font_path, font_size)
draw.text( (10, 10), text, font=unicode_font, fill=font_color)

img.save("Test-Text.png")