from tkinter import *

#FUNCTIONS
def button_value(number):
    current = inputs.get()
    inputs.delete(0,END)
    inputs.insert(0,str(current) + str(number))

def clean():
    inputs.delete(0,END)

Janela_inicial = Tk()
Janela_inicial.title('Sistema')
Janela_inicial['bg'] = 'grey'
<<<<<<< Updated upstream
Janela_inicial.geometry('500x300+350+250')
Janela_inicial.minsize(500,300)
=======
Janela_inicial.geometry('225x349+350+250')
Janela_inicial.minsize(225,349)
Janela_inicial.maxsize(225,349)
>>>>>>> Stashed changes
answer = StringVar()


# WIDGETS

<<<<<<< Updated upstream
inputs = Entry(Janela_inicial)
inputs.focus()


label_result = Label(Janela_inicial,textvariable= answer)
bt1 = Button(Janela_inicial,text = '1',command=1)
bt2 = Button(Janela_inicial,text = '2',command=2)
bt3 = Button(Janela_inicial,text = '3',command=3)
bt4 = Button(Janela_inicial,text = '4',command=4)
bt5 = Button(Janela_inicial,text = '5',command=5)
bt6 = Button(Janela_inicial,text = '6',command=6)
bt7 = Button(Janela_inicial,text = '7',command=7)
bt8 = Button(Janela_inicial,text = '8',command=8)
bt9 = Button(Janela_inicial,text = '9',command=9)
bt0 = Button(Janela_inicial,text = '0',command=0)
btdot = Button(Janela_inicial,text = '.',command=1)
btbar = Button(Janela_inicial,text = '/',command = '/')
btplus = Button(Janela_inicial,text = '+',command=plus)
btsub = Button(Janela_inicial,text = '-',command='-')
btequal = Button(Janela_inicial,text = '=',command=equal)
btmult = Button(Janela_inicial,text = '*',command= '*')

=======
inputs = Entry(Janela_inicial,width = 26,borderwidth = 5)
inputs.focus()


bt1 = Button(Janela_inicial,text = '1',command=lambda: button_value(1),padx=20 ,pady=20)
bt2 = Button(Janela_inicial,text = '2',command=lambda: button_value(2),padx=20 ,pady=20)
bt3 = Button(Janela_inicial,text = '3',command=lambda: button_value(3),padx=20 ,pady=20)
bt4 = Button(Janela_inicial,text = '4',command=lambda: button_value(4),padx=20 ,pady=20)
bt5 = Button(Janela_inicial,text = '5',command=lambda: button_value(5),padx=20 ,pady=20)
bt6 = Button(Janela_inicial,text = '6',command=lambda: button_value(6),padx=20 ,pady=20)
bt7 = Button(Janela_inicial,text = '7',command=lambda: button_value(7),padx=20 ,pady=20)
bt8 = Button(Janela_inicial,text = '8',command=lambda: button_value(8),padx=20 ,pady=20)
bt9 = Button(Janela_inicial,text = '9',command=lambda: button_value(9),padx=20 ,pady=20)
bt0 = Button(Janela_inicial,text = '0',command=lambda: button_value(0),padx=20 ,pady=20)
btdot = Button(Janela_inicial,text = '.',command=lambda: button_value(1),padx=22 ,pady=20)
btbar = Button(Janela_inicial,text = '/',command = lambda: button_value(1),padx=22 ,pady=20)
btplus = Button(Janela_inicial,text = '+',command=lambda: button_value(1),padx=22 ,pady=20)
btsub = Button(Janela_inicial,text = '-',command=lambda: button_value(1),padx=25 ,pady=20)
btequal = Button(Janela_inicial,text = '=',command=lambda: button_value(1),padx=22 ,pady=20)
btmult = Button(Janela_inicial,text = '*',command= lambda: button_value(1),padx=25 ,pady=20)
btclear = Button(Janela_inicial,text = 'Clear',command = lambda: clean(),padx = 90, pady = 20)
>>>>>>> Stashed changes


#LAYOUT
inputs.grid(row = 0, column = 0)
bt1.grid(row = 1 ,column = 0)
bt2.grid(row = 1 ,column = 1)
bt3.grid(row = 1 ,column = 2)
btsub.grid(row=1,column = 3)
bt4.grid(row = 2 ,column = 0)
bt5.grid(row = 2 ,column = 1)
bt6.grid(row = 2 ,column = 2)
btmult.grid(row = 2,column = 3)
bt7.grid(row = 3 ,column = 0)
bt8.grid(row = 3 ,column = 1)
bt9.grid(row = 3 ,column = 2)
btplus.grid(row = 3 ,column = 3)
bt0.grid(row = 4 ,column = 0)
btdot.grid(row = 4 ,column = 1)
btbar.grid(row = 4,column =2)
btequal.grid(row=4,column=3)
label_result.grid(row = 5 ,column = 0)

Janela_inicial.mainloop()