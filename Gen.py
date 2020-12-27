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
center_point = (int(image_size[0]/2), int(image_size[1]/2))

# Generate the base image
magic_circle = Circle("Magic-Circle 1", (500, 500))

# Add the layers
magic_circle.addLayer( Rosette(image_size, 8, 175, 2, fg_color, trans_col) )
magic_circle.addLayer( CharBase(image_size, font_path, 64, font_color, fg_color, trans_col, 0, True) )
magic_circle.addLayer( NGON(image_size, center_point, 175, 64, trans_col, fg_color, 2, 0, False) )
magic_circle.addLayer( TextRing(image_size, 200, 32, font_path, 16, fg_color, trans_col) )
magic_circle.addLayer( NGON(image_size, center_point, 225, 64, trans_col, fg_color, 2, 0, False) )
magic_circle.addLayer( TextRings(image_size, 250, 8, 25, 32, 2, fg_color, trans_col, font_path, 16, fg_color, False)  )
magic_circle.addLayer( Burst(image_size, 275, 10, 128, 2, fg_color, trans_col) )
magic_circle.addLayer( TextRing(image_size, 325, 64, font_path, 12, font_color, trans_col) )
#magic_circle.addLayer( ZodiacRing(image_size, 375, unicode_font, 32, fg_color, trans_col  ) )
magic_circle.addLayer( AlchemicRing(image_size, 16, 450, unicode_font, 32, fg_color, trans_col  ) )

# Save the image
magic_circle.saveImage()
