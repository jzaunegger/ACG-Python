# NGON

## Description:
* This is a simple drawing function that draws a N-Sided Polygon and returns the layer it is drawn on.


## Parameters:
* img_size: 
  * The size of the image to be drawn. 
  * This tuple value should be the same size as the expected output image.
  * Input Type - Tuple of Ints
    * Examples:
      * (255, 255)
      * (512, 512)
      * (1024, 1024)
      * Any tuple of ints greater than 0, however it should be at least (256, 256).
  
* diameter: 
  * The diameter of the NGON to be drawn. 
  * Input Type - Int
  * Examples:
    * 20, 40, 100, 200, 400
    * Any number greater than 0 and less than the image width or image height.
  
* num_sides: 
  * The number of sides the NGON should have.
  * Input Type - Int
  * Examples:
    * 3, 4, 5, 6, 8 (Common Shapes)
    * 32, 65 (Circle Shapes)
    * Any number greater than 3.
  
* bg_color: 
  * The background color of the NGON image.
  * Input Type - Tuple of 4 Floats
  * Examples:
    * (255.0, 255.0, 255.0, 255.0) (Opaque White)
    * (0.0, 0.0, 0.0, 0.0) (Transparent)
    * (255.0, 0.0, 0.0, 255.0) (Red)
    * (0.0, 255.0, 0.0, 255.0) (Green)
    * (0.0, 0.0, 255.0, 255.0) (Blue)
  
* fg_color: 
  * The outline color of the NGON.

* line_width: 
  * The line width of the NGON outline.

* rotation: 
  * The number of degrees to rotate the NGON.
  
## Usage
    python 
        # Draw a NGON
        layer1 = NGON((500, 500), 250, 64, (0, 0, 0, 0), (255, 255, 255, 255), 2, 0) 


## Examples
    Image example goes here.