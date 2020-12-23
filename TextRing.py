from PIL import Image, ImageDraw, ImageFont
import os, random, math

config = {
    'font-size': 30,
    'num-chars': 32,
    'radius': 200,
    'img-size': (500, 500),
    'font-path': os.path.join(os.getcwd(), 'fonts', 'Misc-Languages', 'Lovecraft.ttf'),
    'bg-color': (0, 0, 0, 255),
    'text-color': (255, 255, 255, 255)
}

def getRandomChar():
    return chr(random.randint(97, 122))

def drawTextRing2(config):
    base_image = Image.new('RGBA', (config['img-size'][0], config['img-size'][1]), color=config['bg-color'])
    base_draw = ImageDraw.Draw(base_image)
    img_font = ImageFont.truetype(config['font-path'], config['font-size'])

    x, y, currentAngle = 0, 0, 0
    centerX = config['img-size'][0] / 2
    centerY = config['img-size'][1] / 2

    for i in range(0, config['num-chars']):
        currentAngle = math.pi * 2 * i / config['num-chars']
        x = int(centerX + config['radius'] * math.cos(currentAngle))
        y = int(centerX + config['radius'] * math.sin(currentAngle))

        char = getRandomChar()
        base_draw.text((x, y), char, font=img_font, fill=config['text-color'], anchor='ms', align='center')
        
    base_image.save('ring2.png')

drawTextRing2(config)