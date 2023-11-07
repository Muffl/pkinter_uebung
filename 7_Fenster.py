import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Klickzähler")
root.geometry("400x400")
root.focus()
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.maxsize(width=600, height=600)
root.minsize(width=250, height=250)
root.resizable(width=False, height=True)

result = 0

def incremt_counter():
    global result
    result += 1
    label_result.configure(text=str(result))

def incremt_counter10():
    global result
    result += 10
    label_result.configure(text=str(result))

def incremt_counter_reset():
    global result
    result = 0
    label_result.configure(text=str(result))

label = tk.Label(root, text="Ein Klickzähler mit tkinter")
label.grid(column=0, row=0, columnspan=2)

label_result=ttk.Label(root, text=(result), font="Arial, 25")
label_result.grid(column=0, row=1, columnspan=2)

button_label= ttk.Label(root, text="Klickzähler +1:")
button_label.grid(column=0, row=2, sticky="e")

button =ttk.Button(root, text="Hier klicken", width=20, command = incremt_counter)
button.grid(column=1, row=2, sticky="w")

button2_label= ttk.Label(root, text="Klickzähler +10:")
button2_label.grid(column=0, row=3, sticky="e")

button2 =ttk.Button(root, text="Hier klicken für 2", width=20, command=incremt_counter10)
button2.grid(column=1, row=3, sticky="w")

button3_label= ttk.Label(root, text="Zähler zurücksetzen:")
button3_label.grid(column=0, row=4, sticky="e")

button3 =ttk.Button(root, text="Reset", width=20, command=incremt_counter_reset)
button3.grid(column=1, row=4, sticky="w")

root.mainloop()