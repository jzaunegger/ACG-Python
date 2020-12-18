from PIL import Image, ImageDraw
import sys, os, json

def loadPalleteData():
    filePath = os.path.join('config', 'palletes.json')
    pathName = os.path.join(os.getcwd(), filePath)

    if(os.path.exists(pathName)):
        with open(pathName) as json_file:
            data = json.load(json_file)
            return data
    else:
        print('The pallete data could not be found.')
        print('Using default color profile.')
        return None

palleteData = loadPalleteData()

# Params 
selected_pallete = 'nebula'

config = {
    'numImages': 10,
    'imageSize': (512, 512),
    'outputFolder': 'output'
}
bg_color = ''
fg_colors = []

if(palleteData != None):
    for i in range(len(palleteData['palletes'])):
        for key in palleteData['palletes'][i]:
            if(key == selected_pallete):
                currentData = palleteData['palletes'][i]
                config['bgColor'] = currentData[key]['background-color']
                config['fgColors'] = currentData[key]['secondary-colors']

def convert_hex_to_rgb(hexcode):
    stripped_code = hexcode.lstrip('#')
    return tuple(int(stripped_code[i:i+2], 16) for i in (0, 2, 4))


def generate_images(config):

    # Check if output folder exists
    outFolderPath = os.path.join(os.getcwd(), config['outputFolder'])
    if(os.path.exists(outFolderPath) == False):
        os.mkdir(outFolderPath)

    for i in range(config['numImages']):
        currentImage = Image.new('RGB', config['imageSize'], convert_hex_to_rgb(config['bgColor']))
        imgName = 'Image' + str(i) + '.png'
        imgPath = os.path.join(outFolderPath, imgName)
        imageDraw = ImageDraw.Draw(currentImage)

        imageDraw.ellipse((100, 100, 150, 200), fill=convert_hex_to_rgb(config['fgColors'][1]))
        currentImage.save(imgPath, quality=95)
        


generate_images(config)