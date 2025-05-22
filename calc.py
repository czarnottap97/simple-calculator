import tkinter as tk
from tkinter import *
#window settings
root = tk.Tk()
root.geometry("400x600")
root.title('Simple calculator')

#global expression
expr = ""
eq = StringVar()
expr_field = Entry(root, textvariable=eq)
expr_field.grid(columnspan=4, ipadx=70)
done = False
checker = ""

# functions used for preessing the buttons
def press(num):
    global expr
    global done
    global checker
    checker = str(num)
    if done == False:
        expr = expr + str(num)
        eq.set(expr)

    elif done == True:
        done = False
        if checker.isdigit() == True:
            expr = ""
            expr = expr + str(num)
            eq.set(expr)
        else:
            expr = expr + str(num)
            eq.set(expr)


# function for clearing the whole field
def clear():
    global expr
    expr = ""
    eq.set("")
#function for erasing a single character from your equation
def erase():
    global expr
    expr = eq.get()[0:-1]
    eq.set(expr)

#function to have your result.
def equal():
    try:

        global expr
        global done
        total = str(eval(expr))
        eq.set(total)
        expr = total
        done = True
    except:
        eq.set("error")
        expr = ""



button1 = tk.Button(root, text='1', command=lambda: press(1), padx=20, pady=20).grid(row=1, column=1)
button2 = tk.Button(root, text='2', command=lambda: press(2), padx=20, pady=20).grid(row=1, column=2)
button3 = tk.Button(root, text='3', command=lambda: press(3), padx=20, pady=20).grid(row=1, column=3)
button4 = tk.Button(root, text='4', command=lambda: press(4), padx=20, pady=20).grid(row=2, column=1)
button5 = tk.Button(root, text='5', command=lambda: press(5), padx=20, pady=20).grid(row=2, column=2)
button6 = tk.Button(root, text='6', command=lambda: press(6), padx=20, pady=20).grid(row=2, column=3)
button7 = tk.Button(root, text='7', command=lambda: press(7), padx=20, pady=20).grid(row=3, column=1)
button8 = tk.Button(root, text='8', command=lambda: press(8), padx=20, pady=20).grid(row=3, column=2)
button9 = tk.Button(root, text='9', command=lambda: press(9), padx=20, pady=20).grid(row=3, column=3)
button0 = tk.Button(root, text='0', command=lambda: press(0), padx=20, pady=20).grid(row=4, column=1)
button_div = tk.Button(root, text='/', command=lambda: press("/"), padx=20, pady=20).grid(row=4, column=2)
button_point = tk.Button(root, text='.', command=lambda: press("."), padx=20, pady=20).grid(row=4, column=3)
button_plus = tk.Button(root, text='+', command=lambda: press("+"), padx=20, pady=20).grid(row=5, column=1)
button_minus = tk.Button(root, text='-', command=lambda: press("-"), padx=20, pady=20).grid(row=5, column=2)
button_multip = tk.Button(root, text='*', command=lambda: press("*"), padx=20, pady=20).grid(row=5, column=3)
button_eq = tk.Button(root, text='=', command=equal, padx=20, pady=20).grid(row=6, column=1)
button_clear = tk.Button(root, text='clear', command=clear, padx=15, pady=15).grid(row=6, column=2)
backsp = tk.Button(root, text='erase', command=erase, padx=15, pady=15).grid(row=6, column=3)

root.mainloop()
