# Import Dependencies
from CircleGen import *
from PIL import Image

# Basic parameters
image_size = (500, 500)
font_path = os.path.join(os.getcwd(), 'fonts', 'Misc-Languages', 'Lovecraft.ttf')
unicode_font = os.path.join(os.getcwd(), 'fonts', 'DejaVuSans.ttf')
trans_col = (0, 0, 0, 0)
fg_color = (255, 255, 255, 255)
font_color = (200, 0, 0, 255)
font2_color = (255, 255, 255, 15)
center_point = (int(image_size[0]/2), int(image_size[1]/2))

# Generate the base image
magic_circle = Circle("Magic-Circle 1", (500, 500))

# Add the layers
magic_circle.addLayer( Mandala(image_size, 150, 10, 32, 2, fg_color, trans_col, -30, -10) )
magic_circle.addLayer( Mandala(image_size, 170, 10, 32, 2, fg_color, trans_col, 5, 0) )
magic_circle.addLayer( Mandala(image_size, 200, 10, 32, 2, fg_color, trans_col, 10, 10) )
magic_circle.addLayer( Mandala(image_size, 230, 10, 32, 2, fg_color, trans_col, 20, 20) )
magic_circle.addLayer( Mandala(image_size, 260, 10, 32, 2, fg_color, trans_col, 40, 30) )

# Save the image
magic_circle.saveImage()
