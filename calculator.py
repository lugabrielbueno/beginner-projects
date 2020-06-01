from tkinter import *

#FUNCTIONS
def button_value(number):
    current = inputs.get()
    inputs.delete(0,END)
    inputs.insert(0,str(current) + str(number))

def clean():
    inputs.delete(0,END)

def button_add():
    first_number = inputs.get()
    global f_num
    global operation
    operation = 'addition'
    f_num = float(first_number)
    inputs.delete(0,END)

def button_dif():
    first_number = inputs.get()
    global f_num
    global operation
    operation = 'subtraction'
    f_num = float(first_number)
    inputs.delete(0,END)

def button_mult():
    first_number = inputs.get()
    global f_num
    global operation
    operation = 'multiply'
    f_num = float(first_number)
    inputs.delete(0,END)

def button_div():
    first_number = inputs.get()
    global f_num
    global operation
    operation = 'division'
    f_num = float(first_number)
    inputs.delete(0,END) 

def equal():
    second_number = inputs.get()
    inputs.delete(0,END)
    global f_num
    global operation

    if f_num == float or second_number == float:
        if operation == 'addition':
            inputs.insert(0, int(f_num) + int(second_number))
        elif operation == 'subtraction':
            inputs.insert(0, int(f_num) - int(second_number))
        elif operation == 'multiply':
            inputs.insert(0,int(f_num) * int(second_number))
        elif operation == 'division':
            inputs.insert(0,int(f_num) / int(second_number))
    else:
        if operation == 'addition':
            inputs.insert(0, f_num + float(second_number))
        elif operation == 'subtraction':
            inputs.insert(0, f_num - float(second_number))
        elif operation == 'multiply':
            inputs.insert(0,f_num * float(second_number))
        elif operation == 'division':
            inputs.insert(0,f_num / float(second_number))

# Initialize

Janela_inicial = Tk()
Janela_inicial.title('Calculator')
Janela_inicial['bg'] = 'grey'
Janela_inicial.geometry('225x349+350+250')
Janela_inicial.minsize(225,349)
Janela_inicial.maxsize(225,349)
answer = StringVar()


# WIDGETS

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
btdot = Button(Janela_inicial,text = '.',command=lambda: button_value('.'),padx=22 ,pady=20)
btbar = Button(Janela_inicial,text = '/',command = button_div,padx=22 ,pady=20)
btplus = Button(Janela_inicial,text = '+',command=button_add,padx=22 ,pady=20)
btsub = Button(Janela_inicial,text = '-',command=button_dif,padx=25 ,pady=20)
btequal = Button(Janela_inicial,text = '=',command=equal,padx=22 ,pady=20)
btmult = Button(Janela_inicial,text = '*',command= button_mult,padx=25 ,pady=20)
btclear = Button(Janela_inicial,text = 'Clear',command = lambda: clean(),padx = 90, pady = 20)


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