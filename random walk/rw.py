from tkinter import *
from random_walk_class import RandomWalk

root = Tk()
root.title('Random Walk Graphic')
root.geometry('300x340+450+250')
root.minsize(300,340)
root.maxsize(300,340)


# Functions
select1 = BooleanVar()
select2 = BooleanVar()
select3 = BooleanVar()
select4 = BooleanVar()
select5 = BooleanVar()
select6 = BooleanVar()
select7 = BooleanVar()

selected1 = BooleanVar()
selected2 = BooleanVar()
selected3 = BooleanVar()
selected4 = BooleanVar()
selected5 = BooleanVar()

def points(points):
    global num_points
    num_points = points
    if selected1:
        selected2.set(False)
        selected3.set(False)
        selected4.set(False)
        selected5.set(False)

    if selected2:
        selected1.set(False)
        selected3.set(False)
        selected4.set(False)
        selected5.set(False)

    if selected3:
        selected2.set(False)
        selected1.set(False)
        selected4.set(False)
        selected5.set(False)

    if selected4:
        selected2.set(False)
        selected3.set(False)
        selected1.set(False)
        selected5.set(False)

    if selected5:
        selected2.set(False)
        selected3.set(False)
        selected4.set(False)
        selected1.set(False)

def palettes(color):
    global palette
    palette = color
    if select1:
        select2.set(False)
        select3.set(False)
        select4.set(False)
        select5.set(False)
        select6.set(False)
        select7.set(False)
    if select2:
        select1.set(False)
        select3.set(False)
        select4.set(False)
        select5.set(False)
        select6.set(False)
        select7.set(False)
    if select3:
        select2.set(False)
        select1.set(False)
        select4.set(False)
        select5.set(False)
        select6.set(False)
        select7.set(False)
    if select4:
        select2.set(False)
        select3.set(False)
        select1.set(False)
        select5.set(False)
        select6.set(False)
        select7.set(False)
    if select5:
        select2.set(False)
        select3.set(False)
        select4.set(False)
        select1.set(False)
        select6.set(False)
        select7.set(False)
    if select6:
        select2.set(False)
        select3.set(False)
        select4.set(False)
        select5.set(False)
        select1.set(False)
        select7.set(False)
    if select7:
        select2.set(False)
        select3.set(False)
        select4.set(False)
        select5.set(False)
        select6.set(False)
        select1.set(False)


def go():
    global num_points
    global palette
    ok = RandomWalk(num_points,palette)
    ok.direction()
    ok.ploting()


# Wigets

label1 = Label(text = 'Pallete of colors')
label2 = Label(text = '    ')
label3 = Label(text= 'Number of steps')



rw  = Button(text = 'Random Walk',padx = 100,pady = 40, command = go)
rw1 = Checkbutton(text = 'Inferno',variable = select1,command =lambda: palettes('inferno'))
rw2 = Checkbutton(text = 'Rainbow',variable = select2,command =lambda:palettes('rainbow'))
rw3 = Checkbutton(text = 'Terrain',variable = select3,command =lambda:palettes('terrain'))
rw4 = Checkbutton(text = 'BRG',variable = select4,command =lambda: palettes('brg'))
rw5 = Checkbutton(text = 'Jet',variable = select5,command =lambda: palettes('jet'))
rw6 = Checkbutton(text = 'Magma',variable = select6,command =lambda: palettes('magma'))
rw7 = Checkbutton(text = 'Bone',variable = select7,command =lambda: palettes('bone'))

points1 = Checkbutton(text = '1000',variable = selected1,command =lambda: points(1000))
points5 = Checkbutton(text = '5000',variable = selected2,command =lambda: points(5000))
points10 = Checkbutton(text = '10000',variable = selected3,command =lambda: points(10000))
points25 = Checkbutton(text = '25000',variable = selected4,command =lambda: points(25000))
points50 = Checkbutton(text = '50000',variable = selected5,command =lambda: points(50000))


#Layout

rw.grid(row = 0 , column = 0 ,columnspan = 4)
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
