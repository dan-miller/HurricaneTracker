import turtle

# Creates the Turtle and Screen with a background map
# Original code by Phil Ventura
# http://nifty.stanford.edu/2018/ventura-hurricane-tracker/nifty-hurricanes.html
#
# Creates turtle and screen with map and proper coordinates
# output: returns a tuple with turtle and screen and turtle icon
# 
# Modified by DRF, DGM

"""       DO NOT CHANGE THE CODE IN THIS FUNCTION! (Unless you are attempting EC2)
"""
def hurricane_setup():
    
    # DRF - changed "tkinter" to "Tkinter as tkinter" to run on Windows 10
    # DRF - when using Windows 11 use import tkinter
    import tkinter
    
    # set size of window to size of map
    turtle.setup(965, 600)

    wn = turtle.Screen()
    wn.title("Hurricane Tracker")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    # set the coordinate system to match lat/long
    # DRF - parameters are llx lly urx ury (lower left and upper right)
    turtle.setworldcoordinates(-90, 0, -17.66, 45)
    
    # DRF - Windows only supports gif, pgm, ppm unless you use the PIL library
    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    # Create the turtle, make it look like a hurricane symbol
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    #return turtle, canvas, and background image as Tuple
    return (t, wn, map_bg_img)

def plot_point(t, lat, lon, speed, doTimestamp, date):
    """
    Write your code in this function

    Useful functions for turtle:
    - t.color('colorName') will change the turtle's color
    - t.width(value) will change the turtle pen width (value is a positive integer)
    - t.goto(x, y) will move the turtle to the given x and y position
    - t.dot(radius) will draw a dot at the turtle's current posion with the given radius (positive integer)
    - t.write('some string') will write text to the canvas at the turtle's current position
    """
    
    CAT1 = 74
    CAT2 = 96
    CAT3 = 111
    CAT4 = 130
    CAT5 = 157

    if (speed >= CAT5):
        t.color('red')
        t.width(6)
    elif(speed >= CAT4):
        t.color('orange')
        t.width(5)
    elif(speed >= CAT3):
        t.color('yellow')
        t.width(4)
    elif(speed >=CAT2):
        t.color('green')
        t.width(3)
    elif(speed >= CAT1):
        t.color('blue')
        t.width(2)
    else:
        t.color('white')
        t.width(1)
    
    t.goto(lon, lat)

    if (doTimestamp):
        t.dot(5)
        t.write(date)
    

""" DO NOT CHANGE CODE IN THIS FUNCTION
"""
def hurricane(data):
    (t, wn, map_bg_img) = hurricane_setup()
    t.pendown()
    counter = 0
    for datapoint in data:
        point = datapoint.split('\t')
        print(point)

        # Position the turtle initially
        if counter == 0:
            t.hideturtle()
            t.penup()
            t.goto(float(point[3]), float(point[2]))
            t.pendown()
            t.showturtle()

        writeDate = counter % 8 == 0
        plot_point(t, float(point[2]), float(point[3]), int(point[4]), writeDate, point[0])
        counter+=1

    wn.exitonclick()

""" DO NOT CHANGE CODE IN THIS FUNCTION (Unless you are attempting extra credit)
"""
def main():

    # Ask user for hurricane choice
    print('1 - Major Hurricane DORIAN (2019)\n2 - Hurricane ELSA (2021)\n3 - Major Hurricane FLORENCE (2018)\n4 - Major Hurricane HUGO (1989)\n5 - Major Hurricane IAN (2022)\n6 - Hurricane IRENE (1999)\n7 - Major Hurricane MICHAEL (2018)')
    choice = int(input('Press number, then enter: '))
    
    while not 1 <= choice <= 7:
        choice = input("Try again: ")

    f = None
    if choice == 1:
        f = open('data/Dorian2019.txt')
    elif choice == 2:
        f = open('data/Elsa2021.txt')
    elif choice == 3:
        f = open('data/Florence2018.txt')
    elif choice == 4:
        f = open('data/Hugo1989.txt')
    elif choice == 5:
        f = open('data/Ian2022.txt')
    elif choice == 6:
        f = open('data/Irene1999.txt')
    elif choice == 7:
        f = open('data/Michael2019.txt')

    lines = f.readlines()
    
    # Eat the first three lines of the data file
    data = lines[3:]    
    hurricane(data)

main()
