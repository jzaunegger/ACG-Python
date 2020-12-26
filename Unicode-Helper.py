import os, json
from PIL import Image, ImageDraw, ImageFont

symbols_data = os.path.join(os.getcwd(), 'config', 'symbols.json')

if(os.path.exists(symbols_data)):
    with open(symbols_data) as json_file:
        data = json.load(json_file)


# Print all of the values
text = ""
font_size = 32
font_path = os.path.join(os.getcwd(), 'fonts', 'Symbola-AjYx.ttf')

for i in range(len(data['symbols']['greek']['lower'])):
    val = data['symbols']['greek']['lower'][i]
    text += chr(val)

sample = Image.new('RGB', (1800, 200), 'white')
draw = ImageDraw.Draw(sample)
font = ImageFont.truetype(font_path, font_size)

draw.text((10, 10), text, fill='black', font=font)

sample.save("Greek.png", "PNG")