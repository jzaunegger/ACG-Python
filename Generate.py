# Import Dependencies
from graphics import *
from CircleGen import *

# Main Script
def main():
    # Create the window
    win = GraphWin('Circle Generator', 512, 512)

    # Draw a background plane
    backgroundPlane = Rectangle(Point(0, 0), Point(512, 512))
    backgroundPlane.setFill('black')
    backgroundPlane.setOutline('black')
    backgroundPlane.draw(win)

    layer1 = NGON(Point(256, 256), 50, 4, 'white')
    layer1.calcPoints()
    layer1.show(win, False)

    layer2 = NGON(Point(256, 256), 50, 4, 'red')
    layer2.calcPoints()
    layer2.rotate(45)
    layer2.show(win, False)

    layer3 = NGON(Point(256, 256), 50, 32, 'white')
    layer3.calcPoints()
    layer3.show(win, False)

    title = Text(Point(256, 100), "Test")
    title.setSize(30)
    title.setFace("arial")
    title.setTextColor("white")
    title.draw(win)

    # Close the window
    win.getMouse()
    win.close()

# Run main script
main()