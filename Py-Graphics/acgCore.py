from graphics import *
import acgPallettes

import math, random, sys
from PIL import Image as NewImage

# Function to draw a N-sided polygon
# =======================================================
def NGON(win, centerPoint, radius, numSides, color):

    points = []
    temp = 0
    x = 0
    y = 0

    for i in range(0, numSides):
        temp = math.pi * 2 * i / numSides
        x = centerPoint.getX() + radius * math.cos(temp)
        y = centerPoint.getY() + radius * math.sin(temp)
        points.append(Point(x, y))

    shape = Polygon(points)
    shape.setOutline(color)
    shape.setWidth(2)
    shape.draw(win)

# Function to draw a NGON in a repeated pattern
# =======================================================
def LayerArray(win, pos, radiusStart, layerGap, numSides, numLayers, color):
    rad = radiusStart

    for i in range(0, numLayers):
        layer = NGON(win, pos, rad, numSides, color)
        rad += layerGap

# Function to draw a N-sided polygon, N times in a circle
# =======================================================
def Rings(win, pos, ringRadius, ringSize, numSides, numRings, color):

    temp = 0
    x = 0
    y = 0

    for i in range(0, numRings):
        temp = math.pi * 2  * i / numRings
        x = pos.getX() + ringRadius * math.cos(temp)
        y = pos.getY() + ringRadius * math.sin(temp)
        NGON(win, Point(x, y), ringSize, numSides, color)    

# Function to draw a burst shape
# =======================================================
def Burst(win, pos, radius, width, numSides, color):
    temp = 0
    x = 0
    y = 0
    tempPoints = []

    for i in range(0, numSides):
        temp = math.pi * 2  * i / numSides

        if i % 2 == 0:
            x = pos.getX() + radius * math.cos(temp)
            y = pos.getY() + radius * math.sin(temp)

        else:
            x = pos.getX() + (radius + width) * math.cos(temp)
            y = pos.getY() + (radius + width) * math.sin(temp)

        tempPoints.append(Point(x, y))
    
    layer = Polygon(tempPoints)
    layer.setOutline(color)
    layer.setWidth(2)
    layer.draw(win)

# Generate an array of random values
# =======================================================
def GenerateValues(cp, layerRadius):
    values = []

    # Define generation parameters
    NGON_sizes = [3, 4, 5, 6, 8, 16, 32, 64]
    circle_sizes = [32, 64]
    ring_amts = [4, 6, 8, 12, 16, 32]

    # Add center point
    values.append(cp)

    # Generate Layer Type
    layer_type  = random.randint(0, 100)
    values.append(layer_type)

    # Determine the NGON size
    NGON_index = random.randint(0, len(NGON_sizes)-1)
    NGON_size = NGON_sizes[NGON_index]
    values.append(NGON_size)

    # Determine the circle size
    circle_index = random.randint(0, len(circle_sizes)-1)
    circle_size = circle_sizes[circle_index]
    values.append(circle_size)

    # Determine the number of rings
    ring_index = random.randint(0, len(ring_amts)-1)
    ring_amt = ring_amts[ring_index]
    values.append(ring_amt)

    # Determine Ring Size
    ring_size = random.randint(10, 50)
    values.append(ring_size)

    # Generate Layer Size
    layer_size  = int(layerRadius)
    values.append(layer_size)   

    # Generate Burst Width
    burst_width = int(layer_size + (layer_size * random.uniform(0.1, 0.3)))
    values.append(burst_width)

    # Generate Layer Gap
    layer_gap = int(layer_size + (layer_size * random.uniform(0.1, 0.3)))
    values.append(layer_gap)

    # Generate Layer Repeats
    layer_repeats = random.randint(2, 7)
    values.append(layer_repeats)

    return values

# Draw the given layer
# =======================================================
def DisplayLayer(win, cp, layerRadius, pallette):
    values = GenerateValues(cp, layerRadius)
    layer = []

    randIndex = random.randint(1, 4)
    currentColor = pallette[randIndex]

    '''
        Values Indicies:
        0  - Center Point
        1  - Layer Type
        2  - NGON Size
        3  - Circle Size
        4  - Number of Rings
        5  - Ring Size 
        6  - Layer Size
        7  - Burst Width
        8  - Layer Gap
        9  - Layer Repeats
    '''

    # Draw a NGON
    if values[1] <= 50:
        NGON(win, cp, values[6], values[2], currentColor)

    # Draw a layer array
    elif values[1] > 50 and values[1] <= 70:
        LayerArray(win, cp, values[6], values[8], values[2], values[9], currentColor)

    # Draw a burst
    elif values[1] > 70 and values[1] <= 90:
        Rings(win, cp, values[6], values[5], values[3], values[4], currentColor)

    elif values[1] > 90 and values[1] <= 100:
        Burst(win, cp, values[6], values[7], values[3], currentColor)
        pass

    else:
        pass

    return layer