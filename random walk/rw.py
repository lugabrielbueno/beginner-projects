from tkinter import *
from random_walk_class import RandomWalk
from sys import exit
root = Tk()
root.title('Random Walk Graphic')
root.geometry('260x310+450+250')
root.minsize(260,310)
root.maxsize(260,310)


# Functions
pointsvar = IntVar()
colorvar = IntVar()

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

label1 = Label(text = 'Pallete of colors',font= 'Calibri 10 italic')
label2 = Label(text = '      ')
label3 = Label(text= 'Number of steps',font = 'Calibri 10 italic')



rw  = Button(text = 'Random Walk',padx = 30,pady = 20, command = go,borderwidth= 3, font = 'Calibri 12 bold')
exits = Button(text = 'Exit',padx = 20 ,pady = 5, command = exit ,borderwidth = 3,font = 'Calibri 12 bold')
rw1 = Radiobutton(text = 'Inferno',variable = colorvar,value = 1,command =lambda: palettes('inferno'))
rw2 = Radiobutton(text = 'Rainbow',variable = colorvar,value = 2,command =lambda:palettes('rainbow'))
rw3 = Radiobutton(text = 'Terrain',variable = colorvar,value = 3,command =lambda:palettes('terrain'))
rw4 = Radiobutton(text = 'BRG',variable = colorvar,value = 4,command =lambda: palettes('brg'))
rw5 = Radiobutton(text = 'Jet',variable = colorvar,value = 5,command =lambda: palettes('jet'))
rw6 = Radiobutton(text = 'Magma',variable = colorvar,value = 6,command =lambda: palettes('magma'))
rw7 = Radiobutton(text = 'Bone',variable = colorvar,value = 7,command =lambda: palettes('bone'))

points1 = Radiobutton(text = '1000',variable = pointsvar,value = 1 ,command =lambda: points(1000))
points5 = Radiobutton(text = '5000',variable = pointsvar,value = 2 ,command =lambda: points(5000))
points10 =Radiobutton(text = '10000',variable = pointsvar,value = 3 ,command =lambda: points(10000))
points25 =Radiobutton(text = '25000',variable = pointsvar,value = 4 ,command =lambda: points(25000))
points50 =Radiobutton(text = '50000',variable = pointsvar,value = 5 ,command =lambda: points(50000))


#Layout

rw.grid(row = 0 , column = 0,columnspan = 4)
exits.grid(row = 9,column = 2)
label1.grid(row= 1, column = 0,sticky = 'w')
label2.grid(row = 1,column = 1)
label3.grid(row = 1, column = 2,sticky = 'w')
rw1.grid(row = 2, column = 0,sticky = 'w')
rw2.grid(row = 3, column = 0,sticky = 'w')
rw3.grid(row = 4, column = 0,sticky = 'w')
rw4.grid(row = 5, column = 0,sticky = 'w')
rw5.grid(row = 6, column = 0,sticky = 'w')
rw6.grid(row = 7, column = 0,sticky = 'w')
rw7.grid(row = 8, column = 0,sticky = 'w')

points1.grid(row = 2 , column = 2,sticky = 'w')
points5.grid(row = 3 , column = 2,sticky = 'w')
points10.grid(row = 4 , column =2,sticky = 'w')
points25.grid(row = 5 , column = 2,sticky = 'w')
points50.grid(row = 6 , column = 2,sticky = 'w')

root.mainloop()
