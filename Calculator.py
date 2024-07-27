import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk



def clear(): # pou tha mpei sto koumpi clear gia na katharizei to entry
    global result
    result = ""
    var.set(result) #grafw sto entry to result
def equal():
     # pou tha mpei sto koumpi gia na ypologizei to periexomeno tou entry
    try:
        global result
        calculate = eval(result)
        var.set(calculate)
        result = str(calculate)
    except:
        result = 'error'
        var.set(result)



def press(number): # pou tha mpei se ola ta ypolipa koumpia , command = lambda : press (1)-to periexomeno
    global result
    result += str(number)
    var.set(result)#prosthetei keimeno kai to vazei sto entry


win = ThemedTk(theme = "adapta")
win.configure(themebg="adapta")

var = tkinter.StringVar()
result = ""#to periexomeno tou entry

Centry = ttk.Entry(win,font=('Tahoma', ),textvariable=var)
Centry.grid(column=1,row=0,columnspan = 3)

Cbtn =  ttk.Button(win , text = "1",command = lambda: press(1))
Cbtn.grid(column=0,row=1)

Cbtn2 =  ttk.Button(win , text = "2",command = lambda: press(2))
Cbtn2.grid(column=1,row=1)

Cbtn3 =  ttk.Button(win , text = "3",command = lambda: press(3))
Cbtn3.grid(column=2,row=1)

Cbtn4 =  ttk.Button(win , text = "4",command = lambda: press(4))
Cbtn4.grid(column=0,row=2)

Cbtn5 =  ttk.Button(win , text = "5",command = lambda: press(5))
Cbtn5.grid(column=1,row=2)

Cbtn6 =  ttk.Button(win , text = "6",command = lambda: press(6))
Cbtn6.grid(column=2,row=2)

Cbtn7 =  ttk.Button(win , text = "7",command = lambda: press(7))
Cbtn7.grid(column=0,row=3)

Cbtn8 =  ttk.Button(win , text = "8",command = lambda: press(8))
Cbtn8.grid(column=1,row=3)

Cbtn9 =  ttk.Button(win , text = "9",command = lambda: press(9))
Cbtn9.grid(column=2,row=3)

Cbtn0 =  ttk.Button(win , text = "0",command = lambda: press(0))
Cbtn0.grid(column=0,row=4)

Cbtnplus =  ttk.Button(win , text = "+",command = lambda: press("+"))
Cbtnplus.grid(column=4,row=1)

Cbtnminus =  ttk.Button(win , text = "-",command = lambda: press("-"))
Cbtnminus.grid(column=4,row=2)

Cbtnpol =  ttk.Button(win , text = "*",command = lambda: press("*"))
Cbtnpol.grid(column=4,row=3)

Cbtndie =  ttk.Button(win , text = "/",command = lambda: press("/"))
Cbtndie.grid(column=4,row=4)

Cbtndiepar1 =  ttk.Button(win , text = ")",command = lambda: press(")"))
Cbtndiepar1.grid(column=4,row=5)

Cbtndiepar2 =  ttk.Button(win , text = "(",command = lambda: press("("))
Cbtndiepar2.grid(column=2,row=5)

Cbtncoma =  ttk.Button(win , text = ",",command = lambda: press("."))
Cbtncoma.grid(column=0,row=5)

Cbtnclear =  ttk.Button(win , text = "CLEAR",command=clear)
Cbtnclear.grid(column=1,row=4)

Cbtnison =  ttk.Button(win , text = "=",command=equal)
Cbtnison.grid(column=2,row=4)
CbtnDy =  ttk.Button(win , text = "^",command = lambda: press("**"))
CbtnDy.grid(column=1,row=5)
win.title("Calculator")
win.geometry("360x250")













win.mainloop()
