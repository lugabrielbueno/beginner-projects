from tkinter import *

#FUNCTIONS
def equal():
    result = inputs.get()
    answer.set((result))

def plus():
    answer.set('+')


Janela_inicial = Tk()
Janela_inicial.title('Calculator')
Janela_inicial['bg'] = 'grey'
Janela_inicial.geometry('220x350+350+250')
Janela_inicial.minsize(220,350)
Janela_inicial.maxsize(220,350)
answer = StringVar()


# WIDGETS

inputs = Entry(Janela_inicial,width = 25,borderwidth = 5)
inputs.focus()


bt1 = Button(Janela_inicial,text = '1',command=1,padx=20 ,pady=20)
bt2 = Button(Janela_inicial,text = '2',command=2,padx=20 ,pady=20)
bt3 = Button(Janela_inicial,text = '3',command=3,padx=20 ,pady=20)
bt4 = Button(Janela_inicial,text = '4',command=4,padx=20 ,pady=20)
bt5 = Button(Janela_inicial,text = '5',command=5,padx=20 ,pady=20)
bt6 = Button(Janela_inicial,text = '6',command=6,padx=20 ,pady=20)
bt7 = Button(Janela_inicial,text = '7',command=7,padx=20 ,pady=20)
bt8 = Button(Janela_inicial,text = '8',command=8,padx=20 ,pady=20)
bt9 = Button(Janela_inicial,text = '9',command=9,padx=20 ,pady=20)
bt0 = Button(Janela_inicial,text = '0',command=0,padx=20 ,pady=20)
btdot = Button(Janela_inicial,text = '.',command=1,padx=20 ,pady=20)
btbar = Button(Janela_inicial,text = '/',command = '/',padx=20 ,pady=20)
btplus = Button(Janela_inicial,text = '+',command=plus,padx=20 ,pady=20)
btsub = Button(Janela_inicial,text = '-',command='-',padx=20 ,pady=20)
btequal = Button(Janela_inicial,text = '=',command=equal,padx=20 ,pady=20)
btmult = Button(Janela_inicial,text = '*',command= '*',padx=20 ,pady=20)
btclear = Button(Janela_inicial,text = 'Clear',command = 'C',padx = 88, pady = 20)


#LAYOUT
inputs.grid(row = 0, column = 0,columnspan = 4)
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
btclear.grid(row =5,column = 0 ,  columnspan = 4)

Janela_inicial.mainloop()