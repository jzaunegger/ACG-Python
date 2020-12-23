# Import Dependencies
from CircleGen import *
from PIL import Image

image_size = (500, 500)
font_path = os.path.join(os.getcwd(), 'fonts', 'Misc-Languages', 'The-Calling.ttf')

trans_col = (0, 0, 0, 0)
fg_color = (255, 255, 255, 255)

# Generate the base image
base_image = Image.new('RGB', (500, 500), 'black')

# Create the layers
layer1 = NGON(image_size, 175, 64, trans_col, fg_color, 2, 0)
base_image.paste(layer1, (0, 0), layer1)

layer2 = TextRing(image_size, 200, 32, font_path, 32, fg_color, trans_col)
base_image.paste(layer2, (0, 0), layer2)

layer3 = NGON(image_size, 225, 64, trans_col, fg_color, 2, 0)
base_image.paste(layer3, (0, 0), layer3)

# Save the image
base_image.save('Gen-Test.png', 'PNG')