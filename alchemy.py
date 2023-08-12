from tkinter import *
from random import randint
window = Tk()
window.geometry('600x600')
class Clay:
    image = PhotoImage(file='elements/free-icon-pottery.png').subsample(4)

class Fire:
    image = PhotoImage(file='elements/free-icon-fire.png').subsample(4)
    def __add__(self, other):
        if isinstance(other, Ground):
            return Clay
class Water:
    image = PhotoImage(file='elements/free-icon-water-drop.png').subsample(4)
class Air:
    image = PhotoImage(file='elements/wind.png').subsample(4)
class Ground:
    image = PhotoImage(file='elements/ground.png').subsample(4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

canvas = Canvas(window, width=600, height=600)
canvas.pack()
elements = [Fire(), Ground(),Water(), Air()]
for elem in elements:
    img = canvas.create_image(randint(50,550), randint(50, 550), image=elem.image)

# Реализация движения объетков
def move (event):
    images_id= canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    canvas.coords(images_id,event.x, event.y)
window.bind('<B1-Motion>', move)

window.mainloop()