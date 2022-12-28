"""
    This python class handles the ingestation of configuration files, 
    and constructs the core structure of the Procedural Generation System.
"""
import argparse, os, json
from ErrorLogger import ErrorLogger

error_logger = ErrorLogger()

class ConfigParser:
    def __init__(self, args):
        self.config_file = args.config_file
        self.process_config()

    def process_config(self):
        file_path = os.path.join(os.getcwd(), self.config_file)
        with open(file_path) as json_file:
            data = json.load(json_file)

            # Check the generation parameters
            if 'generation-parameters' in data:
                gen_data = data['generation-parameters']

                # Image Width
                if 'image-width' in gen_data:
                    self.image_width = gen_data['image-width']
                else:
                    error_logger.throwError(1)

                # Image Height
                if 'image-height' in gen_data:
                    self.image_height = gen_data['image-height']
                else:
                    error_logger.throwError(1)

                # Number of Image Samples
                if 'num-samples' in gen_data:
                    self.num_samples = gen_data['num-samples']
                else:
                    error_logger.throwError(1)

                # Number of Image Layers
                if 'num-layers' in gen_data:
                    self.num_layers = gen_data['num-layers']
                else:
                    error_logger.throwError(1)


            else:
                error_logger.throwError(1)



def parse_arguements():
    print('Parsing Arguements.')
    parser = argparse.ArgumentParser('CG')

    # Parse the settings related to the data
    data_settings = parser.add_argument_group('config_settings')
    data_settings.add_argument('--config_file', default='./config.json', help='Path of JSON file containing the generation parameters.')

    return parser.parse_args()

'''
    Function to run the program.
'''
def run():
    args = parse_arguements()
    cp = ConfigParser(args)

if __name__ == '__main__':
    run()