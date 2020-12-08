from graphics import *
import random

'''
    Notes About these Color Pallettes:
    ----------------------------------
    Each color palletes index 0 is the 
    darkest color. They go from dark 
    to light. Each contains five colors

    Color Palettes gathered from:
    color.adobe.com/explore
'''
def getPallette(palletteName):

    pallettes = {   
        'red': ['#440004', '#840008', '#AA000A', '#C4000C', '#D1000C'],
        'orange': ['#E54818', '#FF6702', '#FF7F00', '#FF8E00', '#FF551B'],
        'yellow': ['#F7D200', '#FFFF15', '#FFF200', '#FFE800', '#FFF877'],
        'green': ['#0D4524', '#159B39', '#1D9951', '#24DB64', '#31FF87'],
        'blue': ['#080E33', '#0C154A', '#111E6C', '#192DA1', '#2039CC'], 
        'purple': ['#3C2E59', '#463973', '#7168A6', '#897CA6', '#C6B8D9'],
        'grayscale': ['#232245', '#4D4F53', '#7A7B7C', '#9A9B9C', '#CCCCCC'],
        'nebula': ['#0B1726', '#392359', '#262DA6', '#2932D9', '#1AA3D9']
    }

    if palletteName in pallettes.keys():
        return pallettes[palletteName]

    else:
        return random.choice(list(pallettes.items()))