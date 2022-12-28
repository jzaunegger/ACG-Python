# Circle Generator
Home for the Circle Generator repository. This repository is a series of Python3 scripts and functions that use the Pillow module to generate samples of magic or alchemic circles, as well as many other magic-circle like patterns. This is done by generating series of random numbers with pre-defined drawing patterns to generate new and unique images each generation.

There are more example images that can be viewed in the sources listed below.


These generated circles may also contain various different symbols and letters from the real world, and using special fonts. Characters are supported from the following alphabets.
* Latin  
* Cyrillic 
* Greek
* Coptic
* Arabic
* Devangari
* Thai
* Runic
* Hiragana
* Katakana
* Hangul
    
There is also documentation if you would like to using the drawing components in your own projects. Please see the [Documentation](https://github.com/jzaunegger/ACG-Python/tree/master/docs)

## Usage
To use the scripts I have developed you will need to complete several steps. First you will need to clone the repository, you can download it directly or clone it using git. After cloning the repository, navigate into the ACG-Python folder. Then create a virtual environment and activate it. Once activated you can install the dependencies and start generating images. Just remember to exit the virtual environment when you are done.


create and install the dependencies to a virtual environment. After cloning this repository, run the command:
```bash
    # Clone the repository
    git clone https://github.com/jzaunegger/ACG-Python
    cd ACG-Python
    
    # Create the virtual envivornment
    python3 -r venv /venv
    
    # Activate the virtual environment
    source venv/bin/activate
    
    # Install the dependencies from the requirements
    pip3 -r install requirements.txt
    
    # Deactivate the virtual environment
    deactivate
```

## Structure
The development of this software uses Python as the language following OOP practices and principles.
<hr> 

### Helper Functions
* getCenterPoint
    * Description: Returns the center point of a image as a tuple.
    * Inputs: img_size [A tuple of values]
    * Outputs: A tuple describing the center point.
        * Ex: 
        ```python
            # Example function call in Python
            center_point = getCenterPoint((500, 500))
        ```

* checkPoints
    * Description: Checks if two points are equal.
    * Inputs: Two tuples describing the points.
    * Outputs: A boolean saying if they are equal.
        * Ex: 
        ```python
            # Example function call in Python
            are_equal = checkPoints((500, 500), (250, 250))
        ```
* getDistance
    * Description: Returns the distance between two points.
    * Inputs: Two tuples describing the points.
    * Outputs: A number containing the distance between two points.
        * Ex: 
        ```python
            # Example function call in Python
            distance = getDistance((500, 500), (250, 250))
* getFont
    * Description: Returns a font object with a given style and size.
    * Inputs: A string which is the fonts path, the second is a number setting the font size.
    * Outputs: A pillow font object.
        * Ex: 
        ```python
            # Example function call in Python
            font_1 = getFont('pathToFont', 12)
        ```
* getRandomChar
    * Description: Returns a single lower case English letter.
    * Inputs: A string denoting the case
        * Options:
            * lower
            * upper
    * Outputs: A pillow font object.
        * Ex: 
        ```python
            # Example function call in Python
            char = getRandomChar('upper')
        ```
<hr> 

### Classes
At the base of this whole process is the Circle class. The Circle Class is an object that holds all of the data about a Image being generated. It was hold information like its name, size, color pallete, and all other image related data. It has an array called layers which hold the individual components in each image. This object also holds the functionality to actually save the data to an image format. Most of these classes are for creating elements or features of the images. 


* AlchemicRing
    * This class draws a ring with Alchemic Symbols located at various points around the ring.
    * Parameters
        * img_size - The overall size of the images. 
        * num_points - The number of points that compose the outer ring.
        * diameter - The diameter of the whole ring.
        * font_path - The filepath to the file of the font.
        * font_color - The color to set the text.
        * bg_color - The color of the background.
    * Example: 

* Burst
    * A burst is a a osciallating line that surrounds the magic seal.
    * Parameters:
        * img_size - The width and height dimensions of the image.
        * diameter - The overall width of the layer.
        * burst_height - The width offset between burst peaks and valleys.
        * num_points - The number of points that define the number of tips. If this number is 64,there will be 32 extrusions. 
        * line_width - The width of the lines.
        * fg_color - The color of the lines.
        * bg_color - The color of the background.
    * Example: 

* CharBase
    * Draws a single character at the base of the magic seal.
    * Parameters:
        * 
    * Example: 

* Circle
    * An object that keeps track of image layers and allows users to save the image.
    * Parameters:
        * filename - The name of the file/image being created.
        * img_size - The width and height dimensions of the image.
    * Example: 

* Constellation
    * Plots random points and connects them with lines to form Constellations.
    * Parameters:
        * 
    * Example: 

* LineRing
    * Draws a line in the shape of a ring.
    * Parameters:
        * img_size - The width and height dimensions of the image.
        * diameter - The overall width of the layer.
        * line_height - The width of vertical lines that connect the two rings.
        * num_points - The number of points that define the smoothness of the ring.
        * line_width - The width from the line.
        * fg_color - The color of the lines.
        * bg_color - The color of the background.
    * Example: 

* MaurerRose
    * Draws a MaruerRose.
    * Parameters:
        * 
    * Example: 

* NGON
    * Draws a regular polygon with N points around a fixed point.
    * Parameters:
        * img_size - The width and height dimensions of the image.
        * pos - The position in which this layer should be drawn around.
        * diameter - The overall width of the layer.
        * num_sides - The number of sides for the polygon to have.
        * bg_color - The color of the background.
        * fg_color - The color of the lines and fill.
        * line_width - The width of the lines being drawn.
        * rotation - The degree of rotation to rotate the layer.
        * filled - Boolean variable to set if the polygon is filled.
    * Example: 

* PlanetaryRing
    * Draws a ring with planetary symbols at fixed points around the circle
    * Parameters:
        * 
    * Example: 

* Rings
    * Draws a series of rings.
    * Parameters:
        * img_size - The width and height dimensions of the image.
        * center_point - The point in which the layer will be drawn around.
        * main_diameter - The overall width of the layer.
        * main_radius - The radius of the layer
        * ring_sides - The number of sides each subring will have.
        * ring_diameter - The diameter of each subring. 
        * line_width - The width from the line.
        * fg_color - The color of the lines.
        * bg_color - The color of the background.
        * filled - Boolean variable to set if the polygon is filled.
    * Example: 

* Rose
    * Draws a rose.
    * Parameters:
        * 
    * Example: 

* Rosette
    * Draws a Rosette.
    * Parameters:
        * 
    * Example: 

* TextRing
    * Draws ring with text in it.
    * Parameters:
        * 
    * Example: 

* TextRings
    * Draws a rose.
    * Parameters:
        * 
    * Example: 

* ZodiacRing
    * Draws a rose.
    * Parameters:
        * 
    * Example: 

## Dependecies
* Pillow 
