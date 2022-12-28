import sys
class ErrorLogger:

    def __init__(self):
        self.name = 'ErrorLogger'

    def throwError(self, number):

        if number == '1':
            print('Error: Missing parameter from configuration file.')
            print('Please provide all necessary information for generation to work properly.')
            print('Please visit the documentation to view a sample config file.')
        else:
            print('Error: Error code unknown.')

        self.endProgram()

    def endProgram(self):
        sys.exit()