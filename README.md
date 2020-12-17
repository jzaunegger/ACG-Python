# Alchemical/Magic Circle Generator (ACG/MCG)
Home for the Magic Circle Generator repository. This repository is a series of Python3 scripts and functions that use the PyGraphics Module developed by John Zelle at Wartburg College. It allows you to generate samples of magic or alchemic circles. This is done by generating series of random numbers with pre-defined drawing patterns to generate new and unique images each generation. So far there are only several options that each layer can take, as well as different chances of each layer being drawn. As time goes on more color pallettes and layer designs will be added resulting in more complex and beautiful patterns. I also have plans to use Generative Adversarial Networks to develop new patterns by feeding in samples generated here. I think it could lead to some interesting results. 

If you would like to learn more about how this project works, please read the documentation file listed [here](https://github.com/jzaunegger).

## Usage
To use the scripts I have developed download or clone this repository, then navigate inside the PyGraphics folder. Then use the following commands, to run the program. After running the command you will need to use the prompts and provide the necessary details to generate the images.

```bash
    # Python Verison 2
    python Generate-Samples.py

    # Python Version 3
    python3 Generate-Samples.py
```

Instead of using the prompt you can also feed in all necessary parameters when you run the program. The parameters and example usuage is shown below. Please note that if you use this method and the output subfolder already exists, the program will automatically delete any .png images in the folder by default.

* Parameters:
  * numSamples - The number of images to generate
  * imgWidth - The width of each image in pixels
  * imgHeight - The height of each image in pixels
  * numLayers - The number of layers in each image
  * baseFolder - The parent output folder
  * subFolder - The child output folder
  * colorScheme - The color scheme for the image


```bash
    # Alternate Python3 Example
    python3 Generate-Samples.py numSamples imgWidth imgHeight numLayers baseFolder subFolder colorScheme
```

## Dependecies
* PyGraphics - A simple and lightweight graphics module for Python3. This module allows users to create window objects, and use several built-in objects to display simple graphics in the window. The default features allow you to draw polygons, circles, lines, texts, and rectangles on the screen. This module can be found at [PyGraphics](https://mcsp.wartburg.edu/zelle/python/)

## License
Please feel free to use and build upon this project any-way you see fit. Please just give credit to where it is to, if you found this project helpful, please link it in something you build with it. Please also give credit to Mr. Zelle, for developing the Python Graphics module, for without whom this project wouldn't exist. All of the fonts used in this application are believed to have a open license, if you are the creator of one of these fonts, please let me know and it will be removed.