'''
from PIL import Image, ImageFont, ImageDraw
import os

font_size = 50
center_point = (250, 250)
radius = 100
numSides = 32
text_color = (255, 255, 255, 255)
points = []

#font_path = os.path.join(os.getcwd(), os.path.join('fonts', os.path.join('Fictional-Languages', 'Atlantean.ttf')))
#if(os.path.exists(font_path)):
#    print("Font loaded.")
#    loaded_font = ImageFont.truetype(font_path, font_size)
#else:
loaded_font = ImageFont.load_default()


new_image = Image.new('RGBA', (font_size*2, font_size*2), color=(0, 0, 0, 0))
d = ImageDraw.Draw(new_image)
d.text((250, 250), "TESasldfjalsdjf", font=loaded_font, fill=text_color)
#new_image.rotate(45)
new_image.save('Test.png')
new_image.show()

'''


from PIL import Image, ImageDraw, ImageFont
import os, random

def getRandomChar():
    return chr(random.randint(97, 122))


font_size = 50
num_chars = 10
font_path = os.path.join(os.getcwd(), 'fonts', 'Magic-Languages', 'Enochian.ttf')
img_font = ImageFont.truetype(font_path, font_size)

x_off = 0
base_image = Image.new('RGBA', (font_size * num_chars, 300), color=(0, 0, 0, 255))

for i in range(0, num_chars):
    img = Image.new('RGBA', (font_size+10, font_size+10), color = (0, 0, 0, 0))
        
    d = ImageDraw.Draw(img)
    char = getRandomChar()
    
    d.text((0, 0), char, font=img_font, fill=(255,0,0, 255), align="center")
    img = img.rotate(random.randint(0, 0))
    base_image.paste(img, (x_off, 10))
    x_off += font_size
     
base_image.save('test.png')