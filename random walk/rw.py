from tkinter import *
from random_walk_class import RandomWalk

root = Tk()
root.title('Random Walk Graphic')
root.geometry('260x340+350+350')
root.minsize(260,340)
root.maxsize(260,340)


# Functions

def points(points):
    global num_points
    num_points = points

def palettes(color):
    global palette
    palette = color


def go():
    global num_points
    global palette
    ok = RandomWalk(num_points,palette)
    ok.direction()
    ok.ploting()

# Wigets

label1 = Label(text = 'Pallete of colors')
label2 = Label(text= 'Number of steps')

rw  = Button(text = 'Random Walk',padx = 60,pady = 40, command = go )
rw1 = Checkbutton(text = 'Inferno',command =lambda: palettes('inferno'))
rw2 = Checkbutton(text = 'Rainbow',command =lambda:palettes('rainbow'))
rw3 = Checkbutton(text = 'Terrain',command =lambda:palettes('terrain'))
rw4 = Checkbutton(text = 'BRG',command =lambda: palettes('brg'))
rw5 = Checkbutton(text = 'Jet',command =lambda: palettes('jet'))
rw6 = Checkbutton(text = 'Magma',command =lambda: palettes('magma'))
rw7 = Checkbutton(text = 'Bone',command =lambda: palettes('bone'))
points1 = Checkbutton(text = '1000',command =lambda: points(1000))
points5 = Checkbutton(text = '5000',command =lambda: points(5000))
points10 = Checkbutton(text = '10000',command =lambda: points(10000))
points25 = Checkbutton(text = '25000',command =lambda: points(25000))
points50 = Checkbutton(text = '50000',command =lambda: points(50000))

#Layout

rw.grid(row = 0 , column = 0 ,columnspan = 3)
label1.grid(row= 1, column = 0,sticky = 'w')
label2.grid(row = 1, column = 1,sticky = 'w')
rw1.grid(row = 2, column = 0,sticky = 'w')
rw2.grid(row = 3, column = 0,sticky = 'w')
rw3.grid(row = 4, column = 0,sticky = 'w')
rw4.grid(row = 5, column = 0,sticky = 'w')
rw5.grid(row = 6, column = 0,sticky = 'w')
rw6.grid(row = 7, column = 0,sticky = 'w')
rw7.grid(row = 8, column = 0,sticky = 'w')

points1.grid(row = 2 , column = 1,sticky = 'w')
points5.grid(row = 3 , column = 1,sticky = 'w')
points10.grid(row = 4 , column = 1,sticky = 'w')
points25.grid(row = 5 , column = 1,sticky = 'w')
points50.grid(row = 6 , column = 1,sticky = 'w')

root.mainloop()
