"""
    GUI Componenet of the Circle-Generator.
    This is built using Tkinter for python.

    Author: jzaunegger
"""

from tkinter import *
import json, os

# Class to define the GUI for the Circle-Generator Project.
# This class utilizes tkinter
class GUI(Frame):
    
    #  Initalize the GUI Class
    def __init__(self):
        super().__init__()
        self.initHeader()
        self.initInput()

    def initHeader(self):
        self.master.title('Circle Generator')
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Create the header frame
        self.headerFrame = Frame(self.master)
        self.headerFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        # Display information at the top
        info1 = Text(self.headerFrame)
        infoText1 = 'This application generates images of circle patterns. These circles may contain one of many different languages, geometeric patterns, color schemes, and other features. Using the parameters below you can manipulate the generation patterns '
        infoText2 = 'by setting the image size, number of layers per image, color, and a specific font if you wish.'

        info1.insert(INSERT, infoText1)
        info1.insert(INSERT, infoText2)
        info1.grid(column=0, row=0)


    # Display the input screen for the system
    def initInput(self):
        # Set the input frame configuration
        self.inputFrame = Frame(self.master)
        self.inputFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        
        # Determine the number of images to generate
        numImgLabel = Label(self.inputFrame, text='Number of Images: ', padx=3, pady=3, width=30, justify='left')
        numImgLabel.grid(column=1, row=1)
        self.numImgs = IntVar()
        numImgsEntry = Entry(self.inputFrame, width=4, textvariable=self.numImgs)
        numImgsEntry.grid(column=2, row=1, sticky=(W, E))

        # Determine the number of layers per image
        numLayersLabel = Label(self.inputFrame, text='Number of layers per image: ', padx=3, pady=3, width=30, justify='left')
        numLayersLabel.grid(column=1, row=2)
        self.numLayers = IntVar()
        numLayersEntry = Entry(self.inputFrame, width=2, textvariable=self.numLayers)
        numLayersEntry.grid(column=2, row=2, sticky=(W, E))

        # Determine the width of each image
        imgWidthLabel = Label(self.inputFrame, text='Image Width: ', padx=3, pady=3, width=30, justify='left')
        imgWidthLabel.grid(column=1, row=3)
        self.imgWidth = IntVar()
        imgWidthEntry = Entry(self.inputFrame, width=4, textvariable=self.imgWidth)
        imgWidthEntry.grid(column=2, row=3)

        # Determine the height of each image
        imgHeightLabel = Label(self.inputFrame, text='Image Height: ', padx=3, pady=3, width=30, justify='left')
        imgHeightLabel.grid(column=1, row=4)
        self.imgHeight = IntVar()
        imgHeightEntry = Entry(self.inputFrame, width=4, textvariable=self.imgHeight)
        imgHeightEntry.grid(column=2, row=4)

        # Determine the color pallete
        pallete_names = self.loadPalletes()

        colorLabel = Label(self.inputFrame, text='Color Pallete: ', padx=3, pady=3, width=30, justify='left')
        colorLabel.grid(column=1, row=5)
        self.selectedName = StringVar()
        self.selectedName.set('default')

        color_options = OptionMenu(self.inputFrame, self.selectedName, *pallete_names)
        color_options.grid(column=2, row=5)

    
    # Function to load the names of the palletes from 
    def loadPalletes(self):
        filePath = os.path.join('config', 'palletes.json')
        pathName = os.path.join(os.getcwd(), filePath)
        pallete_names = []

        if(os.path.exists(pathName)):
            with open(pathName) as json_file:
                data = json.load(json_file)
                self.palleteData = data

                for i in range(len(data['palletes'])):
                    for val in data['palletes'][i]:
                        pallete_names.append(val)
        else:
            print("The list of color palletes could not be found. ")
            print("The default color pallete will be used.")

        return pallete_names

# Main Script
def main():
    win = Tk()
    gui = GUI()
    win.geometry("512x512")
    win.mainloop()

# Check to run the main script
if __name__ == '__main__':
    main()