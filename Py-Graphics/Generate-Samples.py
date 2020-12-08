from graphics import *
import math, random, sys
from PIL import Image as NewImage
from acgCore import *
from acgPallettes import *

# The main program
# =====================================================================================
'''
    ===================================================================================
    From the command line, enter the following parameters:
    - number of images
    - image width
    - image height
    - num layers
    - dataset name
    - name of output folder
    - name of the color pallete
    ===================================================================================
'''
def inputParameters():
    inputs = []

    # Input for the number of images
    print("Please input the number of images you would like to generate: ")
    numImages = input()
    if(int(numImages) > 0):
        inputs.append(int(numImages))
    else:
        inputs.append(1)

    # Input for the width of the images
    print("Please input the width of the images: ")
    imageWidth = input()
    if(int(imageWidth) > 0):
        inputs.append(int(imageWidth))
    else:
        inputs.append(256)


    # Input for the height of the images
    print("Please input the height of the images: ")
    imageHeight = input()
    if(int(imageHeight) > 0):
        inputs.append(int(imageHeight))
    else:
        inputs.append(256)

    # Calculate the minimum and the maximum size of each layer
    inputs.append(10)
    inputs.append(int(inputs[1] / 2))

    # Input for the number of layers
    print("Please input the number of layers per image: ")
    numLayers = input()
    if(int(numLayers) > 0):
        inputs.append(int(numLayers))
    else:
        inputs.append(3)

    # Input for the output folder
    print("Where would you like us to save these images to: ")
    outputPath = input()

    # Input for the dataset name
    print("What is the name of this set: ")
    datasetName = input()
    
    tempName = os.path.join(outputPath, datasetName)

    # Check if the output folder exists
    if(os.path.exists(tempName)):
        print("The given dataset name is already taken.")
        print("Would you like to overwrite it? Y or N")
        answer = input()

        # Remove Files
        if(answer == "Y" or answer == 'y'):
            for root, dirs, files in  os.walk(tempName):
                for file in files:
                    os.remove(os.path.join(tempName, file))

            inputs.append(outputPath)
            inputs.append(datasetName)

        # Exit the program
        else:
            print("Exiting")
            sys.exit()

    # Account for the output folder not existing yet
    else:

        # Create the folder for the dataset
        if(os.path.exists(outputPath)):
            outParentFolder = os.path.join(os.getcwd(), outputPath)
            outSubfolder = os.path.join(outParentFolder, datasetName)
            os.mkdir(outSubfolder)

            inputs.append(outputPath)
            inputs.append(datasetName)

        # Create the parent folder and the subfolder for the dataset
        else:
            outParentFolder = os.path.join(os.getcwd(), outputPath)
            outSubfolder = os.path.join(outParentFolder, datasetName)
            os.mkdir(outParentFolder)
            os.mkdir(outSubfolder)
            inputs.append(outputPath)
            inputs.append(datasetName)

    pallette = input("Please enter the name of the pallette you would like to use:")
    inputs.append(pallette)

    return inputs

# =====================================================================================
def main():

    # Read in the input parameters and get a color pallete
    inputs = inputParameters()
    pallette = getPallette(inputs[8])

    '''
        inputs[0] - # images
        inputs[1] - img width
        inputs[2] - img height
        inputs[3] - min size
        inputs[4] - max size
        inputs[5] - # layers
        inputs[6] - outfolder
        inputs[7] - dataset name
        inputs[8] - color pallete name
    '''

    # Main Generation Loop
    out1 = os.path.join(os.getcwd(), inputs[6])
    out2 = os.path.join(out1, inputs[7])

    print("Generating Samples")
    print("-------------------------------------------------------")
    for i in range(0, inputs[0], 1):
        # Create the window
        windowSize = (inputs[1], inputs[2])
        win = GraphWin('Alchemic/Magic Circle Generator', windowSize[0], windowSize[1])

        # Draw a background plane
        backgroundPlane = Rectangle(Point(0, 0), Point(windowSize[0], windowSize[1]))
        backgroundPlane.setFill(pallette[0])
        backgroundPlane.setOutline(pallette[0])
        backgroundPlane.draw(win)

        # Determine Center Point, and Layers Object
        centerPoint = Point(windowSize[0] / 2, windowSize[1] / 2)
        layers = []

        # Set the starting radius and step size
        stepSize = (inputs[4] - inputs[3]) / inputs[5]
        currentRadius = inputs[3]

        # Add Layers
        for j in range(0, inputs[5]):
            DisplayLayer(win, centerPoint, currentRadius, pallette)
            currentRadius += stepSize

        # Determine the output name
        fileName = "Image" + str(i) + ".png"
        outfilePath = os.path.join(out2, fileName)
        print("Creating image", fileName)

        # Save the image to the given filename
        win.postscript(file='image.eps', colormode='color', width=inputs[1], height=inputs[2])
        img = NewImage.open('image.eps')
        outsize = (windowSize[0], windowSize[1])
        img = img.resize(outsize)
        img.save(outfilePath, 'png')

        # Close the window
        # win.getMouse()
        win.close()

    # Log info and remove the temporary image file
    print("-------------------------------------------------------")
    print("Generated", inputs[0], "images saved to", out2)
    os.remove('image.eps')

# Execute the program
main()