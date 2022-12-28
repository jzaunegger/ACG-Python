import math, os, sys, json
from PIL import Image, ImageDraw, ImageFont
from CircleGen import *

config = {
    'image-width': 500,
    'image-height': 500,
    'num-samples': 10,
    'num-layers': 1,
    'color-pallete': 'space',
    'output-folder': 'Dev-Test',
    'generation-name': 'Run-1'
}

'''
    Function to get the list of available color palletes
    from the json data in the config folder. 
'''
def getPalettes():
    file_path = os.path.join(os.getcwd(), 'config', 'palletes.json')
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data


'''
    Load the color palletes from the config dat
'''
def loadColorPalette(config):
    pallete_data = getPalettes()
    pallete_items = pallete_data['palletes']

    for item in pallete_items:
        item_keys = item.keys()
        for key in item_keys:
            if key == config['color-pallete']:
                return item[key]

    return pallete_data['palletes'][0]


'''
    Function that removes any sub-files and directories
    from a given path.
'''
def clearFolder(folder_path):
    sub_files = os.listdir(folder_path)
    for sub_file in sub_files:
        if os.path.isfile(sub_file):
            os.remove(folder_path)

        elif os.path.isdir(sub_file):
            os.rmdir(folder_path)


'''
    Function that creates or clears a given folder.
'''
def checkOutput(config):
    out_folder = os.path.join(os.getcwd(), config['output-folder'])
    if os.path.exists(out_folder) == False:
        os.mkdir(out_folder)
        print("Generating output folder.")
    else:
        clearFolder(out_folder)
        print("Clearing output folder.")

    sub_folder = os.path.join(out_folder, config['generation-name'])
    if os.path.exists(sub_folder) == False:
        os.mkdir(sub_folder)
        print("Creating generation folder.")
    else:
        clearFolder(sub_folder)
        print("Clearing generation folder.")

    return sub_folder

'''
    Function that reads JSON data from a file.
'''
def loadFromJSON(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data

'''
    Function to procedurally generate image parameters, 
    configuration parameters and color palletes.
'''
def GenerateParameters(config, isBase, pallete):
    param_bounds_path = os.path.join(os.getcwd(), 'config', 'gen-param-bounds.json')
    param_bounds = loadFromJSON(param_bounds_path)

    params = {
        'img-size': (config['image-width'], config['image-height']),
        'center_point': (int(config['image-width'] / 2),  int(config['image-height'] / 2)),
        'bg-color': pallete['background-color'],
        'fg-colors' : pallete['secondary-colors'],
        'tran-color' : (0, 0, 0, 0)
    }
    rand_cols = random.choices(pallete['secondary-colors'], weights=[1, 1, 1, 1], k=3)

    # Generate parameters for a base layer
    if isBase == True:
        params['base-choice'] = random.choice(param_bounds['base-options'])
        params['outer-choice'] = None
        params['is-base'] = True
        params['font-size'] = random.choice(param_bounds['font-sizes'])
        params['font-path'] = os.path.join(os.path.join(os.getcwd(), 'fonts', 'Magic-Languages', 'Magi.ttf'))
        params['const-pts'] = random.randint(5, 31)
        params['ngon-sides'] = random.choice(param_bounds['ngon-sizes'])
        params['is-filled'] = random.randint(0, 2)
        params['has-rotation'] = random.randint(0, 2)
        params['rotation'] = random.randint(1, 360)
        params['line-width'] = random.randint(1, 4) 
        params['ring-width'] = random.randint(10, (10 + params['font-size']))
        params['ring-sides'] = random.choice(param_bounds['ngon-sizes'])
        params['sub-ring-diameter'] = params['font-size'] + 10
        params['sub-ring-diameter2'] = (params['sub-ring-diameter'] / 2) + 10
        params['rose-nd'] = param_bounds['rose-values']
        params['maurer-nd'] = ( random.randint(1, 101), random.randint(1, 101) )
        params['line-color'] = rand_cols[0]
        params['font-color'] = rand_cols[1]
        params['fill-color'] = rand_cols[2]
        params['rosette-points'] = random.choice(param_bounds['rosette-points'])
        params['star-points'] = random.choice(param_bounds['star-sizes'])

    # Generate parameters for a outer layer
    else:
        pass

    return params

'''
    Function to generate parameters for a given layer.
'''
def GenerateLayer(params, current_dia):

    # Generate Bases
    if params['is-base'] == True:
        
        # Check if its a Constellation
        if params['base-choice'] == 'constellation':
            return Constellation(params['img-size'], params['const-pts'], current_dia, params['line-width'], params['line-color'], params['tran-color'])

        elif params['base-choice'] == 'char':
            return CharBase(params['img-size'], params['font-path'], params['font-size'], params['font-color'], params['fill-color'], params['tran-color'], params['rotation'], params['is-filled'])

        elif params['base-choice'] == 'maurer-rose':
            
            return MaurerRose(params['img-size'], 32, current_dia, params['line-width'], params['line-color'], params['tran-color'], params['maurer-nd'][0], params['maurer-nd'][1])

        elif params['base-choice'] == 'rose':
            return Rose(params['img-size'], 32, current_dia,  params['line-width'], params['line-color'], params['tran-color'], params['rose-nd'][0][0], params['rose-nd'][0][0])

        elif params['base-choice'] == 'rosette':
            return Rosette(params['img-size'], params['rosette-points'], current_dia, params['line-width'], params['line-color'], params['tran-color'])

        elif params['base-choice'] == 'star':
            return Star(params['img-size'], params['star-points'], current_dia, params['line-width'], params['line-color'], params['tran-color'] )
    
    # Generate Outer Ring
    else:
        pass

'''
    Function to automatically generate image samples
'''
def GenerateSamples(config):
    output_path = checkOutput(config)
    pal = loadColorPalette(config)

    dia = 25

    # Loop through, and create each image
    for i in range(config['num-samples']):
        
        # Create the base Image
        base_image = Image.new('RGB', (config['image-width'], config['image-height']), pal['background-color'] )

        # Create the Magic Circle object
        outfile_name = os.path.join(output_path, 'Sample-' + str(i))
        magic_circle = Circle(outfile_name, (config['image-width'], config['image-height']))

        for j in range(config['num-layers']):

            # Generate a random image
            if j == 0:
                params = GenerateParameters(config, True, pal)
                newLayer = GenerateLayer(params, dia)
                magic_circle.addLayer(newLayer)
            else:
                params = GenerateParameters(config, False, pal)
                newLayer = GenerateLayer(params, dia)
                magic_circle.addLayer(newLayer)

        # Save the image
        magic_circle.saveImage()

        dia += int(config['image-width'] / config['num-layers'])
        
    print("Successfully Generated {} samples.".format(config['num-samples']))

GenerateSamples(config)