# Install Dependencies
import os
from fontTools.ttLib import TTFont

# Determine the subfolders
currentPath = os.getcwd()
subFolders = os.listdir()

# Create empty list to store font names
fonts = []

# Parse for files
for subFolder in subFolders:
    tempPath = os.path.join(currentPath, subFolder)
    
    # Check if subpath is a folder
    if(os.path.isdir(tempPath)):
        subFiles = os.listdir(tempPath)

        # Check files in the subfolder
        for subFile in subFiles:
            filePath = os.path.join(tempPath, subFile)

            # Check if a font file, then save
            if(subFile.endswith('.ttf')):
                currentFont = TTFont(filePath)
                currentFont.save(filePath)
                fonts.append(subFile)

# Log Status
print("  Sucessfully Installed", len(fonts), "fonts to the system.  ")
print("------------------------------------------------")
for font in fonts:
    print(font)

