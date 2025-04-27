from tkinter import *

map_width=1000
map_height=500
window = Tk()
window.title("Meteor Points")
window.geometry("1000x500")
label = Label(window,text="hello tkinter")
bg = PhotoImage(file="world_map4.png")
canvas = Canvas(window, width=map_width, height=map_height)
canvas.create_image(0, 0, anchor=NW, image=bg)
canvas.pack()
canvas.create_text(10,250, anchor="nw", text="Ancient", fill="Orange")
canvas.create_text(10,270, anchor="nw", text="Medieval", fill="Red")
canvas.create_text(10,290, anchor="nw", text="Modern", fill="Green")
canvas.create_text(10,310, anchor="nw", text="Contemporary", fill="Blue")

f = open("meteor_strikes.csv",encoding="utf-8")
fileContents = f.read()
lineList = fileContents.split("\n")

def get_pixel_x(longitude):
    x_pixel = (longitude + 180) * (map_width / 360)
    return(x_pixel)

def get_pixel_y(latitude):
    y_pixel = (85 - latitude) * (map_height / 170)
    return(y_pixel)

def get_meteor_size(mass):
    size = min(6, max(2, mass / 2000))
    return(size)

def get_period_color(year):
    if (year < 500):
        return("Orange")
    elif (year >= 500 and year < 1500):
        return("Red")
    elif (year >= 1500 and year < 1900):
        return("Green")
    elif (year >= 1900):
        return("Blue")

def draw_meteor(latitude,longitude,mass,year,name):
    x = get_pixel_x(longitude)
    y = get_pixel_y(latitude)
    size = get_meteor_size(mass)
    color = get_period_color(year)
    radius = size / 2
    canvas.create_oval(x-radius,y-radius,x+radius,y+radius, outline = color, width = 1)
    if (mass > 10000000):
        canvas.create_text(x,y,text = name,font = ("Arial", 10),fill = 'gold')

def draw_all_meteors():
    for line in lineList:
        lineSplit = line.split(",")
        if (len(line) > 3):
            draw_meteor(float(lineSplit[3]),float(lineSplit[4]),float(lineSplit[1]),int(lineSplit[2]),str(lineSplit[0]))

draw_all_meteors()
window.mainloop()