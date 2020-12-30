# Documentation
Here you can find the documentation for the Circle Generator for Python. There are many different components to the circle generation, which all are described here. The components are broken intro several classifications, drawing functions and helper functions.

## Drawing Functions

### Layer Management

- Circle

### Helper Functions

- checkPoints
- getCenterPoint
- getDistance
- getFont
- getRandomChar

### Fonts 

- getFonts
- getFont
- loadFont

### Color Palettes

- addPalette
- getPalette
- loadPalettes
- removePalette
- savePalettes



### Base Layers

- [CharBase]()
  - Draws a single character in the center of the circle, with a given radius, font, font size, font color, and optional rotation.
- [Constellation]()
  - Draws a constellation pattern by randomly plotting points, and connecting each point to its nearest neighbor. 
- [MaurerRose]()
  - Draws a maurer rose pattern from some numerical parameters.
- [Rose]()
  - Draws a rose pattern from some numerical parameters.
- [Rosette]()
  - Draws a rosette by plotting points around a circle, and connecting each point to each other. 
- Star
  - Draws a star by plotting points around a circle and connecting a point to every other point.



### Outer Layers

* [NGON](https://github.com/jzaunegger/ACG-Python/blob/master/docs/NGON.md)
  * Draws a N-Sided Polygon with a given radius, number of sides, line width, line color, with optional rotation.
* [Text Ring]()
  * Draws a ring of N characters with a given radius, number of characters, font, font size, and font color.
* Planetary Ring
* Zodiac Ring
* Alchemic Ring
* Text Rings
* Rings
* Burst
* Line Ring
