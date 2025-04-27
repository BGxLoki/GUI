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

longitude = 1
latitude = 0

f = open("meteor_strikes.csv")
fileContents = f.read()
lineList = fileContents.split("\n")

def get_pixel_x(longitude):
    x_pixel = (longitude + 180) * (map_width / 360)
    return x_pixel

def get_pixel_y(latitude):
    y_pixel = (85 - latitude) * (map_height / 170)
    return y_pixel




window.mainloop()

#Hello Cammy

#Si papi